from rest_framework.routers import DefaultRouter
from .views import JobPostViewSet
from .views import ResumeScoreView


router = DefaultRouter()
router.register('jobs', JobPostViewSet, basename='jobpost')

urlpatterns = router.urls
