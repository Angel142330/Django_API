from django.urls import path,include
from . import views
from rest_framework import routers  

router=routers.DefaultRouter()
router.register(r'programador',views.ProgramadorViewSet, 'programadores')

# urlpatterns = [
#     path('api/',include(router.urls)),
# ]

urlpatterns= router.urls