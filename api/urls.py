from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from . import views 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from rest_framework.routers import DefaultRouter


schema_view = get_schema_view(
   openapi.Info(
      title="API Doc",
      default_version='v1',
      description="Restaurants",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@manohar.borana"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
   path('Iteamsdata',views.IteamsData.as_view(),name='Iteams-data')
]        

# router = DefaultRouter()
# router.register(r'restaurants', RestaurantViewSet, basename='restaurants')
# urlpatterns = router.urls