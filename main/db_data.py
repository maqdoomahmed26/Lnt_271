from .models import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from main.serialier import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
import datetime
class LnTMainViewSet(viewsets.ModelViewSet):
    queryset = LnTMain.objects.all()
    serializer_class = LnTMainSerializer

    @action(detail=False, methods=['post'])
    def save_data(self, request):
        """Handles saving or updating data for all related models"""
        sr_no = LTMainDetails.objects.filter(id__gte=0).first()
        serial_value = sr_no.serial_no if sr_no else None
        main_instance = LnTMain.objects.create(reportType="All",serial_no = serial_value)
        
        # Save Digital Input
        dg_input_data = request.data.get("dg_input", [])
        for dg in dg_input_data:
            dg["lntmain"] = main_instance
            if "id" in dg and dg["id"]:  # Update if ID exists
                dg_instance = get_object_or_404(LnTDIGITAL_INPUT, id=dg["id"])
                dg_instance.__dict__.update(dg)
                dg_instance.save()
            else:  # Create new record
                LnTDIGITAL_INPUT.objects.create(**dg)

        # Save Digital Output
        dg_output_data = request.data.get("dg_output", [])
        for do in dg_output_data:
            do["lntmain"] = main_instance
            if "id" in do and do["id"]:
                do_instance = get_object_or_404(LnTDIGITAL_OUTPUT, id=do["id"])
                do_instance.__dict__.update(do)
                do_instance.save()
            else:
                LnTDIGITAL_OUTPUT.objects.create(**do)

        # Save Analog Input
        an_input_data = request.data.get("an_input", [])
        for ai in an_input_data:
            ai["lntmain"] = main_instance
            if "id" in ai and ai["id"]:
                ai_instance = get_object_or_404(LnTANALOG_INPUT, id=ai["id"])
                ai_instance.__dict__.update(ai)
                ai_instance.save()
            else:
                LnTANALOG_INPUT.objects.create(**ai)

        # Save Analog Output
        an_output_data = request.data.get("an_output", [])
        for ao in an_output_data:
            ao["lntmain"] = main_instance
            if "id" in ao and ao["id"]:
                ao_instance = get_object_or_404(LnTANALOG_OUTPUT, id=ao["id"])
                ao_instance.__dict__.update(ao)
                ao_instance.save()
            else:
                LnTANALOG_OUTPUT.objects.create(**ao)

        return Response({"serial_no": main_instance.serial_no}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def fetch_data(self, request):
        """Fetch all related data based on serial_no"""
        serial_no = request.query_params.get("serial_no")
        if not serial_no:
            return Response({"error": "serial_no is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            main_instance = LnTMain.objects.filter(serial_no=serial_no).latest('id')
        except LnTMain.DoesNotExist:
            main_instance = get_object_or_404(LnTMain, id=0)
        data = {
            "main_id": main_instance.id,
            "dg_input": LnTDIGITAL_INPUTSerializer(LnTDIGITAL_INPUT.objects.filter(lntmain=main_instance), many=True).data,
            "dg_input_board": LnT_DI_TestSerializer(LnT_DI_Test.objects.filter(lntmain=main_instance), many=True).data,
            "dg_output": LnTDIGITAL_OUTPUTSerializer(LnTDIGITAL_OUTPUT.objects.filter(lntmain=main_instance), many=True).data,
            "dg_output_board": LnT_DO_TestSerializer(LnT_DO_Test.objects.filter(lntmain=main_instance), many=True).data,
            "an_input": LnTANALOG_INPUTSerializer(LnTANALOG_INPUT.objects.filter(lntmain=main_instance), many=True).data,
            "an_output": LnTANALOG_OUTPUTSerializer(LnTANALOG_OUTPUT.objects.filter(lntmain=main_instance), many=True).data,
            "AIO_board": LnT_AIO_TestSerializer(LnT_AIO_Test.objects.filter(lntmain=main_instance), many=True).data,
        }
        return Response(data, status=status.HTTP_200_OK)
    
class LnTDIGITAL_INPUTViewSet(viewsets.ModelViewSet):
    
    
    serializer_class = LnTDIGITAL_INPUTSerializer

    def get_queryset(self):
        queryset = LnTDIGITAL_INPUT.objects.all()
        main_id = self.request.query_params.get('lntmain_id', None)
        if main_id is not None:
            queryset = queryset.filter(lntmain__id=main_id)
        else:
            queryset = queryset.filter(lntmain__id= -1)
        return queryset



class LnTDIGITAL_OUTPUTViewSet(viewsets.ModelViewSet):
    
    serializer_class = LnTDIGITAL_OUTPUTSerializer
    def get_queryset(self):
        queryset = LnTDIGITAL_OUTPUT.objects.all()
        main_id = self.request.query_params.get('lntmain_id', None)
        if main_id is not None:
            queryset = queryset.filter(lntmain__id=main_id)
        else:
            queryset = queryset.filter(lntmain__id= -1)
        return queryset
    
class LnTANALOG_INPUTViewSet(viewsets.ModelViewSet):
    
    serializer_class = LnTANALOG_INPUTSerializer
    def get_queryset(self):
        queryset = LnTANALOG_INPUT.objects.all()
        main_id = self.request.query_params.get('lntmain_id', None)
        if main_id is not None:
            queryset = queryset.filter(lntmain__id=main_id)
        else:
            queryset = queryset.filter(lntmain__id= -1)
        return queryset
    
class LnTANALOG_OUTPUTViewSet(viewsets.ModelViewSet):
    
    serializer_class = LnTANALOG_OUTPUTSerializer
    def get_queryset(self):
        queryset = LnTANALOG_OUTPUT.objects.all()
        main_id = self.request.query_params.get('lntmain_id', None)
        if main_id is not None:
            queryset = queryset.filter(lntmain__id=main_id)
        else:
            queryset = queryset.filter(lntmain__id= -1)
        return queryset
    
 
def insert_def_data():
    mm  = LnTMain.objects.create(id = 0,date = datetime.datetime.now())
    nn  = LTMainDetails.objects.create(id = 1)
    nn.save()

    # Slot3
    DI_add1  = '0x9D8202'
    DI_add2  = '0x9D8402'
    DI_name = ''
    DI_Address = ''
    for i in range (33):
        if i ==0:
            continue
        if i >= 1 and i <= 16 :
            DI_Address = DI_add1
            DI_name = 'DI_GO'
        elif i >= 17 and i <= 32 :
            DI_Address = DI_add2
            DI_name = 'DI_28O'                            
        LnTDIGITAL_INPUT.objects.create(
            lntmain = mm,
            date = datetime.datetime.now(),
            sln = i,
            channel = f'{DI_name}{i}',
            lnt_val = '',
            exp_val = '',
            ref_val ='',
            status = '',
            lnt_val_H = '',
            exp_val_H = '',
            ref_val_H ='',
            status_H = '',
            address = DI_Address,
            data_on = ''
        )

# Slot4
    DO_add1  = '0x9D8602'
    DO_add2  = '0x9D8604'
    DO_Address = ''
    for i in range (29):
        if i ==0:
            continue
        if i >= 1 and i <= 16 :
            DO_Address = DO_add1
        elif i >= 17 and i <= 29 :
            DO_Address = DO_add2
                 
        LnTDIGITAL_OUTPUT.objects.create(
            lntmain = mm,
            date = datetime.datetime.now(),
            sln = i,
            channel = f'DO{i}',
            lnt_val = '',
            exp_val = '',
            ref_val ='',
            status = '',
            lnt_val_H = '',
            exp_val_H = '',
            ref_val_H ='',
            status_H = '',
            address = DO_Address,
            data_on = ''
        )


     # Unique addresses for each value
    AI_addresses = [
                    '0x9D8A02', '0x9D8A04', '0x9D8A06', '0x9D8A08', '0x9D8A0A',
                    '0x9D8A0C', '0x9D8A0E', '0x9D8A10', '0x9D8A12', '0x9D8A14',
                    '0x9D8A16', '0x9D8A18']

    # Iterate over each address and create the corresponding object
    for i, AI_add in enumerate(AI_addresses, start=1):
        LnTANALOG_INPUT.objects.create(
            lntmain=mm,
            date=datetime.datetime.now(),
            sln=i,
            channel=f'AI{i}',  # Channel names like 'AI1', 'AI2', etc.
            lnt_val='',
            exp_val='',
            ref_val='',
            status='',
            lnt_val_N_10 = '',
            exp_val_N_10 = '',
            ref_val_N_10 = '',
            status_N_10 = '',
            lnt_val_P_10 = '',
            exp_val_P_10 = '',
            ref_val_P_10 = '',
            status_P_10 = '',
            
            address=AI_add,  # Convert to hex string if needed
            data_on=''
        )

       # Unique addresses for each value
    AO_addresses = ['0x9D8C02', '0x9D8C04', '0x9D8C06', '0x9D8C08', 
                    '0x9D8C0A', '0x9D8C0C', '0x9D8C0E', '0x9D8C10']

    # Iterate over each address and create the corresponding object
    for i, AO_add in enumerate(AO_addresses, start=1):
        LnTANALOG_OUTPUT.objects.create(
            lntmain=mm,
            date=datetime.datetime.now(),
            sln=i,
            channel=f'AO{i}',  # Channel names like 'AO1', 'AOI2', etc.
            lnt_val='',
            exp_val='',
            ref_val='',
            status='',
            lnt_val_N_10 = '',
            exp_val_N_10 = '',
            ref_val_N_10 = '',
            status_N_10 = '',
            lnt_val_P_10 = '',
            exp_val_P_10 = '',
            ref_val_P_10 = '',
            status_P_10 = '',
            address=AO_add,  # Convert to hex string if needed
            data_on=''
        )   
