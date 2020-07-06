from rest_framework import routers

from .views import MedViewSet
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('meds', MedViewSet, 'meds')
router.register('users', UserViewSet, 'users')
# router.register('<The URL prefix>', <The viewset class>, '<The URL name>')

urlpatterns = router.urls