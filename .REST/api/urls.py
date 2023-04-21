from rest_framework import routers
from .views import EventViewSet, FoodViewSet, PointsViewSet, GaleryViewSet

router = routers.DefaultRouter()
router.register('api/events', EventViewSet, 'events')
router.register('api/catering', FoodViewSet, 'catering')
router.register('api/galery', GaleryViewSet, 'galery')
router.register('api/points', PointsViewSet, 'points')

urlpatterns = router.urls