from rest_framework import serializers
from .models import *


class LnTMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = LnTMain
        fields = '__all__'

  
class LnTDIGITAL_INPUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = LnTDIGITAL_INPUT
        fields = ['sln','channel','lnt_val', 'exp_val', 'ref_val','status','lnt_val_H', 'exp_val_H','ref_val_H','status_H','address']


class LnTDIGITAL_OUTPUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = LnTDIGITAL_OUTPUT
        fields = ['sln','channel','lnt_val', 'exp_val', 'ref_val','status','lnt_val_H', 'exp_val_H','ref_val_H','status_H','address']


class LnTANALOG_INPUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = LnTANALOG_INPUT
        fields = ['sln','channel','lnt_val_N_10', 'exp_val_N_10','ref_val_N_10','status_N_10','lnt_val','exp_val','ref_val','status','lnt_val_P_10', 'exp_val_P_10','ref_val_P_10','status_P_10','address']


class LnTANALOG_OUTPUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = LnTANALOG_OUTPUT
        fields = ['sln','channel','lnt_val_N_10','exp_val_N_10','ref_val_N_10','status_N_10','lnt_val','exp_val','ref_val','status','lnt_val_P_10','exp_val_P_10','ref_val_P_10','status_P_10','address']
class LnT_DI_TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LnT_DI_Test
        fields = ['R1','R2','R3','R4','R5','R6','R7','R8','R9','R10','R11','R12','R13','R14','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12']        

class LnT_DO_TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LnT_DO_Test
        # fields = ['R1','R2','R3','R4']
        fields = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11', 'R12', 'R13', 'R14', 'R15', 'R16', 'R17', 'R18', 'R19', 'R20', 'R21', 'R22', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20']

class LnT_AIO_TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LnT_AIO_Test
        fields = ['AIO_R1','AIO_R2','AIO_R3','AIO_R4', 'AIO_LED16']