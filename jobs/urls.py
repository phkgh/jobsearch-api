from rest_framework.routers import DefaultRouter
from .views import JobPostViewSet

router = DefaultRouter()
router.register('jobs', JobPostViewSet, basename='jobpost')

urlpatterns = router.urls
