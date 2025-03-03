

from rest_framework import routers
from .api import BdataViewSet

routers = routers.DefaultRouter()

routers.register('api/dataset1',BdataViewSet, 'dataset1' )

urlpatterns = routers.urls