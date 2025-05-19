from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import JobPost
from .serializers import JobPostSerializer, ResumeScoreSerializer
from .pagination import JobPostPagination


class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


@api_view(['GET', 'POST'])
def job_list_create(request):
    if request.method == 'GET':
        jobs = JobPost.objects.all()

        location = request.query_params.get('location')
        company = request.query_params.get('company')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')

        if location:
            jobs = jobs.filter(location__icontains=location)
        if company:
            jobs = jobs.filter(company__icontains=company)
        if search:
            jobs = jobs.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )

        if ordering in ['salary', '-salary', 'posted_at', '-posted_at']:
            jobs = jobs.order_by(ordering)
        else:
            jobs = jobs.order_by('-posted_at')

        paginator = JobPostPagination()
        paginated_jobs = paginator.paginate_queryset(jobs, request)
        serializer = JobPostSerializer(paginated_jobs, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = JobPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def job_detail_update_delete(request, id):
    job = get_object_or_404(JobPost, pk=id)

    if request.method == 'GET':
        serializer = JobPostSerializer(job)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = JobPostSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ResumeScoreView(APIView):
    def post(self, request):
        serializer = ResumeScoreSerializer(data=request.data)
        if serializer.is_valid():
            resume = serializer.validated_data['resume']
            job_desc = serializer.validated_data['job_description']

            keywords = ['python', 'django', 'rest', 'sql', 'api', 'postgre']
            resume_lower = resume.lower()
            job_desc_lower = job_desc.lower()
            matched_keywords = [
                kw for kw in keywords if kw in resume_lower and kw in job_desc_lower]
            score = int((len(matched_keywords) / len(keywords)) * 100)

            return Response({
                'score': score,
                'match_summary': f"{len(matched_keywords)} of {len(keywords)} key terms matched: {', '.join(matched_keywords)}"
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
