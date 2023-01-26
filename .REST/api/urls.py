from rest_framework import routers
from .views import EventViewSet, FoodViewSet

router = routers.DefaultRouter()
router.register('api/events', EventViewSet, 'events')
router.register('api/catering', FoodViewSet, 'catering')

urlpatterns = router.urls