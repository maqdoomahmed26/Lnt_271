from django.contrib import admin
from django.urls import path, include
from main import views
from rest_framework.routers import DefaultRouter
from main.db_data import *
from main.All_Cards_Detection import *
# Registering API routes
router = DefaultRouter()

router.register(r'dg_input', LnTDIGITAL_INPUTViewSet, basename='dg_input')
router.register(r'dg_output', LnTDIGITAL_OUTPUTViewSet, basename='dg_output')
router.register(r'an_input', LnTANALOG_INPUTViewSet, basename='an_input')
router.register(r'an_output', LnTANALOG_OUTPUTViewSet, basename='an_output')
router.register(r'lntmain', LnTMainViewSet, basename='lntmain')

router.register(r'dg_input_Ref', LnTDIGITAL_INPUTViewSet, basename='dg_input_Ref')
router.register(r'dg_input_LnT', LnTDIGITAL_INPUTViewSet, basename='dg_input_LnT')

router.register(r'dg_output_Ref', LnTDIGITAL_OUTPUTViewSet, basename='dg_output_Ref')
router.register(r'dg_output_LnT', LnTDIGITAL_OUTPUTViewSet, basename='dg_output_LnT')

router.register(r'an_input_Ref', LnTANALOG_INPUTViewSet, basename='an_input_Ref')
router.register(r'an_input_LnT', LnTANALOG_INPUTViewSet, basename='an_input_LnT')

router.register(r'an_output_Ref', LnTANALOG_OUTPUTViewSet, basename='an_output_Ref')
router.register(r'an_output_LnT', LnTANALOG_OUTPUTViewSet, basename='an_output_LnT')


  
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/btn_DI_High_process_data/', views.btn_DI_High_process_data, name='btn_DI_High_process_data'),
    path('api/btn_DI_Low_process_data/', views.btn_DI_Low_process_data, name='btn_DI_Low_process_data'),
    path('api/btn_AI_0_V_process_data/', views.btn_AI_0_V_process_data, name='btn_AI_0_V_process_data'),
    path('api/btn_AI_N_10_V_process_data/', views.btn_AI_N_10_V_process_data, name='btn_AI_N_10_V_process_data'),
    path('api/btn_AI_P_10_V_process_data/', views.btn_AI_P_10_V_process_data, name='btn_AI_P_10_V_process_data'),
    
    path('api/btn_DO_High_process_data/', views.btn_DO_High_process_data, name='btn_DO_High_process_data'),
    path('api/btn_DO_Low_process_data/', views.btn_DO_Low_process_data, name='btn_DO_Low_process_data'),

    path('api/btn_AO_0_V_process_data/', views.btn_AO_0_V_process_data, name='btn_AO_0_V_process_data'),
    path('api/btn_AO_N_10_V_process_data/', views.btn_AO_N_10_V_process_data, name='btn_AO_N_10_V_process_data'),
    path('api/btn_AO_P_10_V_process_data/', views.btn_AO_P_10_V_process_data, name='btn_AO_P_10_V_process_data'),
    
    path('save_data/', views.save_data, name='save_data'),
    path('delete_data/', views.delete_data, name='delete_data'),
    
    path('receive_test_data/', views.receive_test_data, name='receive_test_data'),
    path('detectcard/', views.detectcard, name='detectcard'),

    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path("LnT_Main_Details/", views.LnT_Main_Details, name="LnT_Main_Details"),
    path("LnT_Test/", views.LnT_Test, name="LnT_Test"),
    path('LnT_SSC_Card/', views.LnT_SSC_Card, name='LnT_SSC_Card'),
    path('get_board_id/', views.get_board_id, name='get_board_id'),

    path('get_ReadN1_id/', views.get_ReadN1_id, name='get_ReadN1_id'),
    path('get_ReadN2_id/', views.get_ReadN2_id, name='get_ReadN2_id'),
    path('get_ReadN3_id/', views.get_ReadN3_id, name='get_ReadN3_id'),
    path('get_ReadN4_id/', views.get_ReadN4_id, name='get_ReadN4_id'),
    path('get_ReadN5_id/', views.get_ReadN5_id, name='get_ReadN5_id'),
    path('get_ReadN6_id/', views.get_ReadN6_id, name='get_ReadN6_id'),
    path('get_ReadN7_id/', views.get_ReadN7_id, name='get_ReadN7_id'),
    path('get_ReadN8_id/', views.get_ReadN8_id, name='get_ReadN8_id'),

    path('get_Loopback_Test/', views.get_Loopback_Test, name='get_Loopback_Test'),

]

