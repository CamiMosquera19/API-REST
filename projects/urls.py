from rest_framework import routers
from dataset1.api import BdataViewSet
from evacolombia.api import EVAColombiaViewSet
from agroandfarming.api import AgroAndFarmingViewSet
from .api import ProjectViewSet

routers = routers.DefaultRouter()

routers.register('api/projects', ProjectViewSet, 'projects' )
routers.register('api/dataset1', BdataViewSet, 'dataset1' )
#routers.register('api/agroandfarming', AgroAndFarmingViewSet, 'agroandfarming' )
routers.register('api/evacolombia', EVAColombiaViewSet, 'evacolombia')

urlpatterns = routers.urls
