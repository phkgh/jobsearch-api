from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

# ✅ Split the import to safely catch issues
from jobs.views import JobPostViewSet
from jobs.views import ResumeScoreView

router = DefaultRouter()
router.register('jobs', JobPostViewSet, basename='jobpost')


def homepage(request):
    return JsonResponse({"message": "Welcome to the JobSearch API"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume-score/', ResumeScoreView.as_view(), name='resume-score'),
    path('', homepage),
    path('api/', include(router.urls)),
]
