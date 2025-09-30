from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import json
from .db_data import *
from .models import *
from main.serialier import *
from urllib.parse import parse_qs
import subprocess
import re

def home(request):
    # insert_def_data()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            
            # Redirect to a system URL (replace 'system_url' with the actual URL)
            return redirect('LnT_Main_Details')  # You can use named URL patterns or actual paths
            
        else:
            # Add an error message if login failed
            messages.error(request, 'Invalid username or password')

    return render(request, 'main/login.html')

def LnT_Main_Details(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'submit':
            LTMainDetails.objects.all().delete()
                # Create a new instance if it doesn't exist
            det = LTMainDetails(
                product_description=request.POST.get('txtPD'),
                cat_no=request.POST.get('txtCatNo'),
                serial_no = request.POST.get('txtSerialNo'),
                manufacturing_date=request.POST.get('txtManf'),
                project_name=request.POST.get('txtProjectName'),
                project_no=request.POST.get('txtProjectNo'),
                customer_name=request.POST.get('txtCustomerName'),
                customer_reference_no=request.POST.get('txtCustReferenceNo'),
                bill_of_material=request.POST.get('txtBillofMaterial'),
                ga_assembly_instruction=request.POST.get('txtGA_Assembly'),
                test_instruction=request.POST.get('txtTestInstruction'),
                manufacturing=request.POST.get('txtManufacturing'),
                date1=request.POST.get('Date1'),
                quality_control_review=request.POST.get('txtQuality_Control'),
                date2=request.POST.get('Date2'),
                customer_inspection=request.POST.get('txtCustomerInspection'),
                date3=request.POST.get('Date3'),
                tested_by1 = request.POST.get('txtTestedBy1')
            )
            det.save()

            return redirect('LnT_Test')  # Replace with your actual URL name or route
        elif action == 'ssc_test':
        
            return redirect('LnT_SSC_Card') 
    return render(request, 'contains/LnT_Main_Details.html')  # This should point to your HTML template

def LnT_SSC_Card(request):
    if request.method == 'POST':
        action = request.POST.get('normalsave')
        if action == 'normalsave':
            obseredval1 = request.POST.get('txtReadN1')
            obseredval2 = request.POST.get('txtReadN2')
            obseredval3 = request.POST.get('txtReadN3')
            obseredval4 = request.POST.get('txtReadN4')
            obseredval5 = request.POST.get('txtReadN5')
            obseredval6 = request.POST.get('txtReadN6')
            obseredval7 = request.POST.get('txtReadN7')
            obseredval8 = request.POST.get('txtReadN8')

            status1 = request.POST.get('DropdownN1')
            status2 = request.POST.get('DropdownN2')
            status3 = request.POST.get('DropdownN3')
            status4 = request.POST.get('DropdownN4')
            status5 = request.POST.get('DropdownN5')
            status6 = request.POST.get('DropdownN6')
            status7 = request.POST.get('DropdownN7')
            status8 = request.POST.get('DropdownN8')
            
            ssccard = LnTSscCard.objects.create(
                type = action,
                obseredval1 = obseredval1,
                obseredval2 = obseredval2,
                obseredval3 = obseredval3,
                obseredval4 = obseredval4,
                obseredval5 = obseredval5,
                obseredval6 = obseredval6,
                obseredval7 = obseredval7,
                obseredval8 = obseredval8,
                status1 = status1,
                status2 = status2,
                status3 = status3,
                status4 = status4,
                status5 = status5,
                status6 = status6,
                status7 = status7,
                status8 = status8


            
            )
            ssccard.save()
    return render(request, 'contains/LnT_SSC_Card.html')

def get_ReadN1_id(request):
    if request.method == "GET":  
        command1 = "sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl w 0x39 0x077026 16 0xff10"
        subprocess.getoutput(command1) 

        command = "sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0x077000 16"
        result = subprocess.getoutput(command)
        match = re.search(r'0x([0-9a-fA-F]+)\s*=\s*0x([0-9a-fA-F]+)', result)

        if match:
            addr = match.group(1).lower()
            value = match.group(2).lower().zfill(4)   # e.g. "3412"

            # Swap bytes
            high_byte = value[:2]   # "34"
            low_byte = value[2:]    # "12"
            hex_value = f"{low_byte}{high_byte}"  # "1234"

            # Convert hex string to decimal
            decimal_value = int(hex_value, 16)   # 4660

            return JsonResponse({
                "ReadN1_id_hex": f"0x{hex_value}", 
                "ReadN1_id_dec": decimal_value
            })
        else:
            return JsonResponse({"0x077000": "Failed to read value"})
        
def get_ReadN2_id(request):
    if request.method == "GET":      
        command1 = "sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl w 0x39 0x077026 16 0xff10"
        subprocess.getoutput(command1) 

        command = "sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0x077004 16"
        result = subprocess.getoutput(command)
        match = re.search(r'0x([0-9a-fA-F]+)\s*=\s*0x([0-9a-fA-F]+)', result)
        if match:
            addr = match.group(1).lower()
            value = match.group(2).lower().zfill(4)   # e.g. "3412"

            # Swap bytes
            high_byte = value[:2]   # "34"
            low_byte = value[2:]    # "12"
            hex_value = f"{low_byte}{high_byte}"  # "1234"

            # Convert hex string to decimal
            decimal_value = int(hex_value, 16)   # 4660

            return JsonResponse({
                "ReadN2_id_hex": f"0x{hex_value}", 
                "ReadN2_id_dec": decimal_value
            })
        else:
            return JsonResponse({"0x077004": "Failed to read value"})
        
def get_ReadN3_id(request):
    if request.method == "GET":        
        command = "sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0x077008 16"
        result = subprocess.getoutput(command)
        match = re.search(r'0x([0-9a-fA-F]+)\s*=\s*0x([0-9a-fA-F]+)', result)
        if match:
            addr = match.group(1).lower()
            value = match.group(2).lower().zfill(4)   # e.g. "3412"

            # Swap bytes
            high_byte = value[:2]   # "34"
            low_byte = value[2:]    # "12"
            hex_value = f"{low_byte}{high_byte}"  # "1234"

            # Convert hex string to decimal
            decimal_value = int(hex_value, 16)   # 4660

            return JsonResponse({
                "ReadN3_id_hex": f"0x{hex_value}", 
                "ReadN3_id_dec": decimal_value
            })
        else:
            return JsonResponse({"0x077008": "Failed to read value"})
        
def get_ReadN4_id(request):
    if request.method == "GET":        
        command = "sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0x07700c 16"
        result = subprocess.getoutput(command)
        match = re.search(r'0x([0-9a-fA-F]+)\s*=\s*0x([0-9a-fA-F]+)', result)
        if match:
            addr = match.group(1).lower()
            value = match.group(2).lower().zfill(4)   # e.g. "3412"

            # Swap bytes
            high_byte = value[:2]   # "34"
            low_byte = value[2:]    # "12"
            hex_value = f"{low_byte}{high_byte}"  # "1234"

            # Convert hex string to decimal
            decimal_value = int(hex_value, 16)   # 4660

            return JsonResponse({
                "ReadN4_id_hex": f"0x{hex_value}", 
                "ReadN4_id_dec": decimal_value
            })
        else:
            return JsonResponse({"0x07700c": "Failed to read value"})

def get_ReadN5_id(request):
    if request.method == "GET":        
        command = "sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0x077010 16"
        result = subprocess.getoutput(command)
        match = re.search(r'0x([0-9a-fA-F]+)\s*=\s*0x([0-9a-fA-F]+)', result)
        if match:
            addr = match.group(1).lower()
            value = match.group(2).lower().zfill(4)   # e.g. "3412"

            # Swap bytes
            high_byte = value[:2]   # "34"
            low_byte = value[2:]    # "12"
            hex_value = f"{low_byte}{high_byte}"  # "1234"

            # Convert hex string to decimal
            decimal_value = int(hex_value, 16)   # 4660

            return JsonResponse({
                "ReadN5_id_hex": f"0x{hex_value}", 
                "ReadN5_id_dec": decimal_value
            })
        else:
            return JsonResponse({"0x077010": "Failed to read value"})       

def get_ReadN6_id(request):
    if request.method == "GET":        
        command = "sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0x077014 16"
        result = subprocess.getoutput(command)
        match = re.search(r'0x([0-9a-fA-F]+)\s*=\s*0x([0-9a-fA-F]+)', result)
        if match:
            addr = match.group(1).lower()
            value = match.group(2).lower().zfill(4)   # e.g. "3412"

            # Swap bytes
            high_byte = value[:2]   # "34"
            low_byte = value[2:]    # "12"
            hex_value = f"{low_byte}{high_byte}"  # "1234"

            # Convert hex string to decimal
            decimal_value = int(hex_value, 16)   # 4660

            return JsonResponse({
                "ReadN6_id_hex": f"0x{hex_value}", 
                "ReadN6_id_dec": decimal_value
            })
        else:
            return JsonResponse({"0x077014": "Failed to read value"}) 
        
def get_ReadN7_id(request):
    if request.method == "GET":        
        command = "sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0x077018 16"
        result = subprocess.getoutput(command)
        match = re.search(r'0x([0-9a-fA-F]+)\s*=\s*0x([0-9a-fA-F]+)', result)
        if match:
            addr = match.group(1).lower()
            value = match.group(2).lower().zfill(4)   # e.g. "3412"

            # Swap bytes
            high_byte = value[:2]   # "34"
            low_byte = value[2:]    # "12"
            hex_value = f"{low_byte}{high_byte}"  # "1234"

            # Convert hex string to decimal
            decimal_value = int(hex_value, 16)   # 4660

            return JsonResponse({
                "ReadN7_id_hex": f"0x{hex_value}", 
                "ReadN7_id_dec": decimal_value
            })
        else:
            return JsonResponse({"0x077018": "Failed to read value"})          

def get_ReadN8_id(request):
    if request.method == "GET":        
        command = "sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0x07701c 16"
        result = subprocess.getoutput(command)
        match = re.search(r'0x([0-9a-fA-F]+)\s*=\s*0x([0-9a-fA-F]+)', result)
        if match:
            addr = match.group(1).lower()
            value = match.group(2).lower().zfill(4)   # e.g. "3412"

            # Swap bytes
            high_byte = value[:2]   # "34"
            low_byte = value[2:]    # "12"
            hex_value = f"{low_byte}{high_byte}"  # "1234"

            # Convert hex string to decimal
            decimal_value = int(hex_value, 16)   # 4660

            return JsonResponse({
                "ReadN8_id_hex": f"0x{hex_value}", 
                "ReadN8_id_dec": decimal_value
            })
        else:
            return JsonResponse({"0x07701c": "Failed to read value"})         

#Loopback Test

# def get_Lopback_Test(request):
#     if request.method == "GET":  
#         # Step 1: Write command
#         command1 = "sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl w 0x39 0x077028 16 0x00c0"
#         subprocess.getoutput(command1) 

#         # Step 2: Read command
#         command = "sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0x077022 16"
#         result = subprocess.getoutput(command)

#         # Step 3: Extract hex value from output
#         match = re.search(r'0x([0-9a-fA-F]+)\s*=\s*0x([0-9a-fA-F]+)', result)

#         if match:
#             addr = match.group(1).lower()
#             value = match.group(2).lower().zfill(4)   # e.g. "50c0"

#             # Swap bytes
#             high_byte = value[:2]   # "50"
#             low_byte  = value[2:]   # "c0"
#             hex_value = f"{low_byte}{high_byte}"  # "c050"

#             # Take only right-side byte (low_byte) → binary
#             right_byte_dec = int(low_byte, 16)
#             right_byte_bin = bin(right_byte_dec)[2:].zfill(8)

#             return JsonResponse({
#                 "Loopback_hex": f"0x{hex_value}", 
#                 "Loopback_hex_Binary": right_byte_bin
#             })
#         else:
#             return JsonResponse({"0x077022": "Failed to read value"})



def get_Loopback_Test(request):
    if request.method == "GET":  
        # Step 1: Write command
        command1 = (
            "sshpass -p 'test123' ssh test@192.168.2.100 "
            "/usr/share/vmetoolkit/examples/singleAccess/MasterSgl w 0x39 0x077028 16 0x00c0"
        )
        subprocess.getoutput(command1) 

        # Step 2: Read command
        command = (
            "sshpass -p 'test123' ssh test@192.168.2.100 "
            "/usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0x077022 16"
        )
        result = subprocess.getoutput(command)
        print("---- Running get_Loopback_Test ----")
        print("SSH raw result:", result)

        # Step 3: Extract hex value
        match = re.search(r'0x([0-9a-fA-F]+)\s*=\s*0x([0-9a-fA-F]+)', result)

        if match:
            value = match.group(2).lower().zfill(4)   # e.g. "5000" or "50c0"
            print("Raw value:", value)

            # Break into 2 bytes
            high_byte = value[:2]   # "50"
            low_byte  = value[2:]   # "00"

            # Decide which byte to use (ignore "00")
            if low_byte != "00":
                chosen_byte = low_byte
            else:
                chosen_byte = high_byte

            # Convert chosen byte to binary
            chosen_dec = int(chosen_byte, 16)
            chosen_bin = bin(chosen_dec)[2:].zfill(8)   # e.g. "01010000"

            print("Chosen byte:", chosen_byte)
            print("Binary value:", chosen_bin)

            return JsonResponse({
                "RawValue": value,
                "ChosenByte": chosen_byte,
                "RightByte_Binary": chosen_bin
            })

        else:
            print("❌ Failed to match regex on SSH result")
            return JsonResponse({"error": "Failed to read value"})

def LnT_Test(request):
    

    main_details = LTMainDetails.objects.first()
    return render(request, 'contains/LnT_Test.html', {
        'main_details': main_details
    })

from .btn_DI_High import ret_btn_result as btn_DI_High_ret_btn_result
@csrf_exempt  # Disable CSRF for simplicity (use proper security in production)
def btn_DI_High_process_data(request):
  if request.method == "POST":
        result = btn_DI_High_ret_btn_result()
        return JsonResponse({
                        "status": "success",
                        "result": result
                        })

from .btn_DI_Low import ret_btn_result as btn_DI_Low_ret_btn_result
@csrf_exempt  # Disable CSRF for simplicity (use proper security in production)
def btn_DI_Low_process_data(request):
    if request.method == "POST":
        result = btn_DI_Low_ret_btn_result()
    return JsonResponse({
                        "status": "success",
                        "result": result
                        })
    
from .btn_AI_0_V import  ret_btn_result as btn_AI_0_V_ret_btn_result
@csrf_exempt  # Disable CSRF for simplicity (use proper security in production)
def btn_AI_0_V_process_data(request):
    if request.method == "POST":
        result = btn_AI_0_V_ret_btn_result()
    return JsonResponse({
                        "status": "success",
                        "result": result
                        })

from .btn_AI_N_10_V import ret_btn_result as btn_AI_N_10_V_ret_btn_result
@csrf_exempt  # Disable CSRF for simplicity (use proper security in production)
def btn_AI_N_10_V_process_data(request):
    if request.method == "POST":
        result = btn_AI_N_10_V_ret_btn_result()
    return JsonResponse({
                        "status": "success",
                        "result": result
                        })
    
from .btn_AI_P_10_V import ret_btn_result as btn_AI_P_10_V_ret_btn_result
@csrf_exempt  # Disable CSRF for simplicity (use proper security in production)
def btn_AI_P_10_V_process_data(request):
    if request.method == "POST":
        result = btn_AI_P_10_V_ret_btn_result()
    return JsonResponse({
                        "status": "success",
                        "result": result
                        })

from .btn_DO_High import ret_btn_result as btn_DO_High_ret_btn_result
@csrf_exempt  # Disable CSRF for simplicity (use proper security in production)
def btn_DO_High_process_data(request):
    if request.method == "POST":
        result = btn_DO_High_ret_btn_result()
    return JsonResponse({
                        "status": "success",
                        "result": result
                        })

from .btn_DO_Low import ret_btn_result as btn_DO_Low_ret_btn_result
@csrf_exempt  # Disable CSRF for simplicity (use proper security in production)
def btn_DO_Low_process_data(request):
    if request.method == "POST":
        result = btn_DO_Low_ret_btn_result()
    return JsonResponse({
                        "status": "success",
                        "result": result
                        })

from .btn_AO_0_V import  ret_btn_result as btn_AO_0_V_ret_btn_result
@csrf_exempt  # Disable CSRF for simplicity (use proper security in production)
def btn_AO_0_V_process_data(request):
    if request.method == "POST":
        result = btn_AO_0_V_ret_btn_result()
    return JsonResponse({
                        "status": "success",
                        "result": result
                        })

from .btn_AO_N_10_V import ret_btn_result as btn_AO_N_10_V_ret_btn_result
@csrf_exempt  # Disable CSRF for simplicity (use proper security in production)
def btn_AO_N_10_V_process_data(request):
    if request.method == "POST":
        result = btn_AO_N_10_V_ret_btn_result()
    return JsonResponse({
                        "status": "success",
                        "result": result
                        })
    
from .btn_AO_P_10_V import ret_btn_result as btn_AO_P_10_V_ret_btn_result
@csrf_exempt  # Disable CSRF for simplicity (use proper security in production)
def btn_AO_P_10_V_process_data(request):
    if request.method == "POST":
        result = btn_AO_P_10_V_ret_btn_result()
    return JsonResponse({
                        "status": "success",
                        "result": result
                        })

    
@csrf_exempt  # Only for testing, use @csrf_protect in production
def receive_test_data(request):
    if request.method == "POST":
        data = request.POST.dict()
        # Do something with data...
        return JsonResponse({"status": "success", "received": data})
    return JsonResponse({"status": "error", "message": "Invalid request"})
from .All_Cards_Detection import detect
@csrf_exempt  # Only for testing, use @csrf_protect in production
def detectcard(request):
    if request.method == "POST":
        data = json.loads(request.body)
        card_name = request.POST.get('card_name', None)
        card_name = data.get('card_name',None)
        result = detect(card_name)
        # result =" detected: "
        
        if b"detected:" in result.content:
            return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error", "message": "Invalid request"})

def save_data(request):
    if request.method == 'POST':
        # Save the hidden field value (hidden_field_1, hidden_field_2)
        data = json.loads(request.body)
        form_data_str = data.get("formData", "")
        form_entries = form_data_str.split("&")[1:]  # Skip CSRF token

        parsed_data = {}
        for entry in form_entries:
            if "=" in entry:
                key, value = entry.split("=", 1)
                parsed_data[key] = value

        print('Create a new LnTMain entry')
        sr_no = LTMainDetails.objects.filter(id__gte=0).first()
        serial_value = sr_no.serial_no if sr_no else None
        lntmain = LnTMain.objects.create(reportType="All",serial_no = serial_value)

        print(' Save AIO data')
        aio = LnT_AIO_Test.objects.create(
            lntmain=lntmain,
            AIO_R1 = parsed_data.get("AIO_R1"),
            AIO_R2 = parsed_data.get("AIO_R2"),
            AIO_R3 = parsed_data.get("AIO_R3"),
            AIO_R4 = parsed_data.get("AIO_R4"),
            AIO_R5 = parsed_data.get("AIO_R5"),
            AIO_R6 = parsed_data.get("AIO_R6"),
            AIO_R7 = parsed_data.get("AIO_R7"),
            AIO_R8 = parsed_data.get("AIO_R8"),
            AIO_R9 = parsed_data.get("AIO_R9"),
            AIO_R10 = parsed_data.get("AIO_R10"),
            AIO_R11 = parsed_data.get("AIO_R11"),
            AIO_R12 = parsed_data.get("AIO_R12"),
            AIO_R13 = parsed_data.get("AIO_R13"),
            AIO_R14 = parsed_data.get("AIO_R14"),
            AIO_R15 = parsed_data.get("AIO_R15"),
            AIO_R16 = parsed_data.get("AIO_R16"),
            AIO_R17 = parsed_data.get("AIO_R17"),
            AIO_R18 = parsed_data.get("AIO_R18"),
            AIO_R19 = parsed_data.get("AIO_R19"),
            AIO_R20 = parsed_data.get("AIO_R20"),
            AIO_R21 = parsed_data.get("AIO_R21"),
            AIO_R22 = parsed_data.get("AIO_R22"),
            AIO_R23 = parsed_data.get("AIO_R23"),
            AIO_R24 = parsed_data.get("AIO_R24"),
            AIO_R25 = parsed_data.get("AIO_R25"),
            AIO_R26 = parsed_data.get("AIO_R26"),

            AIO_V1 = parsed_data.get("AIO_V1"),
            AIO_V2 = parsed_data.get("AIO_V2"),
            AIO_V3 = parsed_data.get("AIO_V3"),
            AIO_V4 = parsed_data.get("AIO_V4"),
            AIO_V5 = parsed_data.get("AIO_V5"),
            AIO_V6 = parsed_data.get("AIO_V6"),
            AIO_V7 = parsed_data.get("AIO_V7"),
            AIO_V8 = parsed_data.get("AIO_V8"),
            AIO_V9 = parsed_data.get("AIO_V9"),
            AIO_V10 = parsed_data.get("AIO_V10"),
            AIO_V11 = parsed_data.get("AIO_V11"),
            AIO_V12 = parsed_data.get("AIO_V12"),
            AIO_V13 = parsed_data.get("AIO_V13"),
            AIO_V14 = parsed_data.get("AIO_V14"),
            AIO_V15 = parsed_data.get("AIO_V15"),
            AIO_V16 = parsed_data.get("AIO_V16"),
            AIO_V17 = parsed_data.get("AIO_V17"),
            AIO_V18 = parsed_data.get("AIO_V18"),
            AIO_V19 = parsed_data.get("AIO_V19"),
            AIO_V20 = parsed_data.get("AIO_V20"),
            AIO_V21 = parsed_data.get("AIO_V21"),
            AIO_V22 = parsed_data.get("AIO_V22"),
            AIO_V23 = parsed_data.get("AIO_V23"),
            AIO_V24 = parsed_data.get("AIO_V24"),

            AIO_LED1 = parsed_data.get("AIO_LED1"),
            AIO_LED2 = parsed_data.get("AIO_LED2"),
            AIO_LED3 = parsed_data.get("AIO_LED3"),
            AIO_LED4 = parsed_data.get("AIO_LED4"),
            AIO_LED5 = parsed_data.get("AIO_LED5"),
            AIO_LED6 = parsed_data.get("AIO_LED6"),
            AIO_LED7 = parsed_data.get("AIO_LED7"),
            AIO_LED8 = parsed_data.get("AIO_LED8"),
            AIO_LED9 = parsed_data.get("AIO_LED9"),
            AIO_LED10 = parsed_data.get("AIO_LED10"),
            AIO_LED11 = parsed_data.get("AIO_LED11"),
            AIO_LED12 = parsed_data.get("AIO_LED12"),
            AIO_LED13 = parsed_data.get("AIO_LED13"),
            AIO_LED14 = parsed_data.get("AIO_LED14"),
            AIO_LED15 = parsed_data.get("AIO_LED15"),
            AIO_LED16 = parsed_data.get("AIO_LED16"),
        )  

        print('Save DO data')
        do = LnT_DO_Test.objects.create(
            lntmain=lntmain,
            R1=parsed_data.get("DO_saved_R1"),
            R2=parsed_data.get("DO_saved_R2"),
            R3=parsed_data.get("DO_saved_R3"),
            R4=parsed_data.get("DO_saved_R4"),
            R5=parsed_data.get("DO_saved_R5"),
            R6=parsed_data.get("DO_saved_R6"),
            R7=parsed_data.get("DO_saved_R7"),
            R8=parsed_data.get("DO_saved_R8"),
            R9=parsed_data.get("DO_saved_R9"),
            R10=parsed_data.get("DO_saved_R10"),
            R11=parsed_data.get("DO_saved_R11"),
            R12=parsed_data.get("DO_saved_R12"),
            R13=parsed_data.get("DO_saved_R13"),
            R14=parsed_data.get("DO_saved_R14"),
            R15=parsed_data.get("DO_saved_R15"),
            R16=parsed_data.get("DO_saved_R16"),
            R17=parsed_data.get("DO_saved_R17"),
            R18=parsed_data.get("DO_saved_R18"),
            R19=parsed_data.get("DO_saved_R19"),
            R20=parsed_data.get("DO_saved_R20"),
            R21=parsed_data.get("DO_saved_R21"),
            
            V1=parsed_data.get("DO_saved_V1"),
            V2=parsed_data.get("DO_saved_V2"),
            V3=parsed_data.get("DO_saved_V3"),
            V4=parsed_data.get("DO_saved_V4"),
            V5=parsed_data.get("DO_saved_V5"),
            V6=parsed_data.get("DO_saved_V6"),
            V7=parsed_data.get("DO_saved_V7"),
            V8=parsed_data.get("DO_saved_V8"),
            V9=parsed_data.get("DO_saved_V9"),
            V10=parsed_data.get("DO_saved_V10"),
            V11=parsed_data.get("DO_saved_V11"),
            V12=parsed_data.get("DO_saved_V12"),
            V13=parsed_data.get("DO_saved_V13"),
            V14=parsed_data.get("DO_saved_V14"),
            V15=parsed_data.get("DO_saved_V15"),
            V16=parsed_data.get("DO_saved_V16"),
            V17=parsed_data.get("DO_saved_V17"),
            V18=parsed_data.get("DO_saved_V18"),
            V19=parsed_data.get("DO_saved_V19"),
            V20=parsed_data.get("DO_saved_V20"),
            checkbox_26=parsed_data.get("DO_saved_26"),
            checkbox_27=parsed_data.get("DO_saved_27"),
            checkbox_28=parsed_data.get("DO_saved_28"),
            checkbox_29=parsed_data.get("DO_saved_29"),
            checkbox_30=parsed_data.get("DO_saved_30"),
            checkbox_31=parsed_data.get("DO_saved_31"),
            checkbox_32=parsed_data.get("DO_saved_32"),
            checkbox_33=parsed_data.get("DO_saved_33"),
            checkbox_34=parsed_data.get("DO_saved_34"),
            checkbox_35=parsed_data.get("DO_saved_35"),
            checkbox_36=parsed_data.get("DO_saved_36"),
            checkbox_37=parsed_data.get("DO_saved_37"),
            checkbox_38=parsed_data.get("DO_saved_38"),
            checkbox_39=parsed_data.get("DO_saved_39"),
            checkbox_40=parsed_data.get("DO_saved_40"),
            checkbox_41=parsed_data.get("DO_saved_41")
        )

        print('Save DI data')
        di = LnT_DI_Test.objects.create(
            lntmain=lntmain,
            R1=parsed_data.get("DI_saved_R1"),
            R2=parsed_data.get("DI_saved_R2"),
            R3=parsed_data.get("DI_saved_R3"),
            R4=parsed_data.get("DI_saved_R4"),
            R5=parsed_data.get("DI_saved_R5"),
            R6=parsed_data.get("DI_saved_R6"),
            R7=parsed_data.get("DI_saved_R7"),
            R8=parsed_data.get("DI_saved_R8"),
            R9=parsed_data.get("DI_saved_R9"),
            R10=parsed_data.get("DI_saved_R10"),
            R11=parsed_data.get("DI_saved_R11"),
            R12=parsed_data.get("DI_saved_R12"),
            R13=parsed_data.get("DI_saved_R13"),
            R14=parsed_data.get("DI_saved_R14"),
            R15=parsed_data.get("DI_saved_R15"),
            R16=parsed_data.get("DI_saved_R16"),
            R17=parsed_data.get("DI_saved_R17"),
            R18=parsed_data.get("DI_saved_R18"),
            R19=parsed_data.get("DI_saved_R19"),
            R20=parsed_data.get("DI_saved_R20"),
            R21=parsed_data.get("DI_saved_R21"),
            R22=parsed_data.get("DI_saved_R22"),
            R23=parsed_data.get("DI_saved_R23"),
            R24=parsed_data.get("DI_saved_R24"),
            R25=parsed_data.get("DI_saved_R25"),
            R26=parsed_data.get("DI_saved_R26"),
            R27=parsed_data.get("DI_saved_R27"),
            R28=parsed_data.get("DI_saved_R28"),
            R29=parsed_data.get("DI_saved_R29"),
            R30=parsed_data.get("DI_saved_R30"),
            R31=parsed_data.get("DI_saved_R31"),
            R32=parsed_data.get("DI_saved_R32"),
            R33=parsed_data.get("DI_saved_R33"),
            R34=parsed_data.get("DI_saved_R34"),
            R35=parsed_data.get("DI_saved_R35"),
            R36=parsed_data.get("DI_saved_R36"),
            R37=parsed_data.get("DI_saved_R37"),
            R38=parsed_data.get("DI_saved_R38"),
            R39=parsed_data.get("DI_saved_R39"),
            R40=parsed_data.get("DI_saved_R40"),
            R41=parsed_data.get("DI_saved_R41"),
            R42=parsed_data.get("DI_saved_R42"),
            R43=parsed_data.get("DI_saved_R43"),
            R44=parsed_data.get("DI_saved_R44"),
            R45=parsed_data.get("DI_saved_R45"),
            R46=parsed_data.get("DI_saved_R46"),
            R47=parsed_data.get("DI_saved_R47"),
            R48=parsed_data.get("DI_saved_R48"),


            V1=parsed_data.get("DI_saved_V1"),
            V2=parsed_data.get("DI_saved_V2"),
            V3=parsed_data.get("DI_saved_V3"),
            V4=parsed_data.get("DI_saved_V4"),
            V5=parsed_data.get("DI_saved_V5"),
            V6=parsed_data.get("DI_saved_V6"),
            V7=parsed_data.get("DI_saved_V7"),
            V8=parsed_data.get("DI_saved_V8"),
            V9=parsed_data.get("DI_saved_V9"),
            V10=parsed_data.get("DI_saved_V10"),
            V11=parsed_data.get("DI_saved_V11"),
            V12=parsed_data.get("DI_saved_V12"),
            checkbox_26=parsed_data.get("DI_saved_26"),
            checkbox_27=parsed_data.get("DI_saved_27"),
            checkbox_28=parsed_data.get("DI_saved_28"),
            checkbox_29=parsed_data.get("DI_saved_29"),
            checkbox_30=parsed_data.get("DI_saved_30"),
            checkbox_31=parsed_data.get("DI_saved_31"),
            checkbox_32=parsed_data.get("DI_saved_32"),
            checkbox_33=parsed_data.get("DI_saved_33"),
            checkbox_34=parsed_data.get("DI_saved_34"),
            checkbox_35=parsed_data.get("DI_saved_35"),
            checkbox_36=parsed_data.get("DI_saved_36"),
            checkbox_37=parsed_data.get("DI_saved_37"),
            checkbox_38=parsed_data.get("DI_saved_38"),
            checkbox_39=parsed_data.get("DI_saved_39"),
            checkbox_40=parsed_data.get("DI_saved_40"),
            checkbox_41=parsed_data.get("DI_saved_41")
        )

        print('Save the Digital Input data (from Table 1)')
        for i in range(0, 31):  # We have two rows in this example
            LnTDIGITAL_INPUT.objects.create(
                lntmain=lntmain,  # Link to the LnTMain entry
                sln = data['dg_input'][i]['sln'],
                channel = data['dg_input'][i]['channel'],
                lnt_val = data['dg_input'][i]['lnt_val'],
                exp_val = data['dg_input'][i]['exp_val'],
                ref_val = data['dg_input'][i]['ref_val'],
                status = data['dg_input'][i]['status'],
                lnt_val_H = data['dg_input'][i]['lnt_val_H'],
                exp_val_H = data['dg_input'][i]['exp_val_H'],
                ref_val_H = data['dg_input'][i]['ref_val_H'],
                status_H = data['dg_input'][i]['status_H'],
                address = data['dg_input'][i]['address']
            ).save()
        print('Saving DO')
        for i in range(0, 27):  # We have two rows in this example
            LnTDIGITAL_OUTPUT.objects.create(
                lntmain=lntmain,  # Link to the LnTMain entry
                sln = data['dg_output'][i]['sln'],
                channel = data['dg_output'][i]['channel'],
                lnt_val = data['dg_output'][i]['lnt_val'],
                exp_val = data['dg_output'][i]['exp_val'],
                ref_val = data['dg_output'][i]['ref_val'],
                status = data['dg_output'][i]['status'],

                lnt_val_H = data['dg_output'][i]['lnt_val_H'],
                exp_val_H = data['dg_output'][i]['exp_val_H'],
                ref_val_H = data['dg_output'][i]['ref_val_H'],
                status_H = data['dg_output'][i]['status_H'],
                address = data['dg_output'][i]['address']
            )
        print('Saving AI')
        for i in range(0, 11):  # We have two rows in this example
            LnTANALOG_INPUT.objects.create(
                lntmain=lntmain,  # Link to the LnTMain entry
                sln = data['an_input'][i]['sln'],
                channel = data['an_input'][i]['channel'],
                lnt_val = data['an_input'][i]['lnt_val'],
                exp_val = data['an_input'][i]['exp_val'],
                ref_val = data['an_input'][i]['ref_val'],
                status = data['an_input'][i]['status'],

                lnt_val_N_10 = data['an_input'][i]['lnt_val_N_10'],
                exp_val_N_10 = data['an_input'][i]['exp_val_N_10'],
                ref_val_N_10 = data['an_input'][i]['ref_val_N_10'],                
                status_N_10 = data['an_input'][i]['status_N_10'],

                lnt_val_P_10 = data['an_input'][i]['lnt_val_P_10'],
                exp_val_P_10 = data['an_input'][i]['exp_val_P_10'],
                ref_val_P_10 = data['an_input'][i]['ref_val_P_10'],
                status_P_10 = data['an_input'][i]['status_P_10'],
                address = data['an_input'][i]['address']
            )
        print('Saving AO')
        for i in range(0, 7):  # We have two rows in this example
            LnTANALOG_OUTPUT.objects.create(
                lntmain=lntmain,  # Link to the LnTMain entry
                sln = data['an_output'][i]['sln'],
                channel = data['an_output'][i]['channel'],
                lnt_val = data['an_output'][i]['lnt_val'],
                exp_val = data['an_output'][i]['exp_val'],
                ref_val = data['an_output'][i]['ref_val'],
                status = data['an_output'][i]['status'],

                lnt_val_N_10 = data['an_output'][i]['lnt_val_N_10'],
                exp_val_N_10 = data['an_output'][i]['exp_val_N_10'],
                ref_val_N_10 = data['an_output'][i]['ref_val_N_10'],
                status_N_10 = data['an_output'][i]['status_N_10'],

                lnt_val_P_10 = data['an_output'][i]['lnt_val_P_10'],
                exp_val_P_10 = data['an_output'][i]['exp_val_P_10'],
                ref_val_P_10 = data['an_output'][i]['ref_val_P_10'],
                status_P_10 = data['an_output'][i]['status_P_10'],
                address = data['an_output'][i]['address']
            )
        
        return JsonResponse({'status': 'success', 'message': 'Data saved successfully!', 'serial_no':lntmain.serial_no})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def delete_data(request):
    if request.method == 'POST':
        # Save the hidden field value (hidden_field_1, hidden_field_2)
        data = json.loads(request.body)
        
        print('delete LnTMain entry')
        LTMainDetails.objects.filter(serial_no=data['serialNo']).delete()
        main = LnTMain.objects.filter(serial_no=data['serialNo'])
        mainid = -1
        for rec in main:
            mainid = rec.id
            print(' Delete AIO data')
            LnT_AIO_Test.objects.filter(lntmain_id = rec.id).delete()
            print('Delete DO data')
            LnT_DO_Test.objects.filter(lntmain_id = rec.id).delete()
            print('Delete DI data')
            LnT_DI_Test.objects.filter(lntmain_id = rec.id).delete()
            print('Delete DI Table data')
            LnTDIGITAL_INPUT.objects.filter(lntmain_id = rec.id).delete()
            print('Delete DO Table data')
            LnTDIGITAL_OUTPUT.objects.filter(lntmain_id = rec.id).delete()
            print('Delete AI Table data')
            LnTANALOG_INPUT.objects.filter(lntmain_id = rec.id).delete()
            print('Delete AO Table data')
            LnTANALOG_OUTPUT.objects.filter(lntmain_id = rec.id).delete()

        print('Delete Main Table data')
        LnTMain.objects.filter(id = mainid).delete()
        return JsonResponse({"status": "success"}) # This should point to your HTML template
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def get_board_id(request):
    if request.method == "GET":
        # command = "sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0x9d8002 16"
        command = "sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0x077024 16"
        
        result = subprocess.getoutput(command)

        match = re.search(r'0x([0-9a-fA-F]+)\s*=\s*0x([0-9a-fA-F]+)', result)

        if match:
            addr = match.group(1).lower()
            value = match.group(2).lower().zfill(4)
            high_byte = value[:2]
            low_byte = value[2:]
            formatted = f"0x{addr} = 0x{low_byte}{high_byte}"
            return JsonResponse({"board_id": formatted})
        else:
            return JsonResponse({"board_id": "Failed to read value"})



