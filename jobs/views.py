from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.pagination import PageNumberPagination
from .pagination import JobPostPagination
from rest_framework import viewsets
from .models import JobPost
from .serializers import JobPostSerializer

from django.db.models import Q

from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import JobPost
from .serializers import JobPostSerializer


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

        # Optional filters
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
            jobs = jobs.order_by('-posted_at')  # Default to newest first

        paginator = JobPostPagination()
        paginated_jobs = paginator.paginate_queryset(jobs, request)
        serializer = JobPostSerializer(paginated_jobs, many=True)
        return paginator.get_paginated_response(serializer.data)

    if request.method == 'POST':
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
        try:
            serializer = JobPostSerializer(job, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
