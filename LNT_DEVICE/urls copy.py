from django.contrib import admin
from django.urls import path, include
from main import views
from rest_framework.routers import DefaultRouter

# Registering API routes
router = DefaultRouter()
router.register(r'products', views.ProductViewSet)

router.register(r'dg_input', views.LnTDIGITAL_INPUTViewSet, basename='dg_input')
router.register(r'dg_output', views.LnTDIGITAL_OUTPUTViewSet, basename='dg_output')
router.register(r'an_input', views.LnTANALOG_INPUTViewSet, basename='an_input')
router.register(r'an_output', views.LnTANALOG_OUTPUTViewSet, basename='an_output')
router.register(r'lntmain', views.LnTMainViewSet, basename='lntmain')
  
urlpatterns = [
    path('api/products/bulk_update/', views.ProductViewSet.as_view({'put': 'bulk_update'}), name='bulk_update'),
    path('api/get_dg_input_check/', views.get_dg_input_check, name='get_dg_input_check'),
    path('api/get_dg_output_check/', views.get_dg_output_check, name='get_dg_output_check'),
    path('api/process_data/', views.process_data, name='process_data'),
    path('api/fetch_data/', views.fetch_data, name='fetch_data'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path("LnT_Test/", views.LnT_Test, name="LnT_Test"),
]
