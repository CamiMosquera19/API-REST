from rest_framework import routers
from dataset1.api import BdataViewSet
from .api import ProjectViewSet

routers = routers.DefaultRouter()

routers.register('api/projects', ProjectViewSet, 'projects' )
routers.register('api/dataset1', BdataViewSet, 'dataset1' )

urlpatterns = routers.urls
