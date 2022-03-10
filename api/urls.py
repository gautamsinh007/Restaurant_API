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
   path('apioverview/',views.Apioverview.as_view(),name='api-overview'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
   path('res_data_id/<int:id>',views.ResDataWithID.as_view(),name='data_with_id'),
   path('res_data/',views.RestData.as_view(),name='all-data'),
   path('cat_data_id/<int:id>',views.CatDataWithId.as_view(),name='cat_data_with_id'),
   path('cat_data/',views.CatData.as_view(),name='cat-all-data'),
   path('iteam_data_id/<int:id>',views.IteamWithID.as_view(),name='iteam_data_with_id'),
   path('iteam_data/',views.IteamData.as_view(),name='iteam-all-data'),
   path('All_Items_with_res_cat/',views.All_Items_with_res_cat.as_view(),name='All_Items_with_res_cat'),
   path('restaurants_list_contain_iteam/', views.RestaurantList.as_view(), name='restaurants'),
   path('Restaurant_details_with_count/<int:id>', views.Restaurant_details_with_count.as_view(), name='Restaurant_details_with_count'),
   path('Iteam_order_by_price/', views.Iteam_order_by_price.as_view(), name='Iteam_order_by_price'),
   path('Res_Greater_500/', views.Res_Greater_500.as_view(), name='Res_Greater_500'),
   path('all_iteam_wich_cat_using_res/<int:id>', views.all_iteam_wich_cat_using_res.as_view(), name='all_iteam_wich_cat_using_res'),
]        

# router = DefaultRouter()
# router.register(r'restaurants', RestaurantViewSet, basename='restaurants')
# urlpatterns = router.urls