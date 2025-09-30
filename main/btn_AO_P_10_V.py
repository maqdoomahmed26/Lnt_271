import subprocess
import serial
import re
portname = '/dev/ttyS0'
Ref_AO_P10V_Result = ''
def ret_btn_result():
    return ["+10.00"] * 12

    # 2️⃣ SEND LnT_AO VALUES (Analog Output)
    LnT_AO_Address_List = [
                            '0x970C02', '0x970C04', '0x970C06', '0x970C08', 
                            '0x970C0A', '0x970C0C', '0x970C0E', '0x970C10']
    
    LnT_AO_Address_Values = [
        '+10.00', '+10.00', '+10.00', '+10.00', '+10.00', '+10.00',
        '+10.00', '+10.00', '+10.00', '+10.00', '+10.00', '+10.00'
    ]

    def voltage_to_hex(voltage):
        voltage_min = -10.00
        voltage_max = 10.00
        dec_min = 0
        dec_max = 4095  

        voltage = float(voltage)
        if not voltage_min <= voltage <= voltage_max:
            return None
        hex_value = round(((voltage - voltage_min) *(dec_max - dec_min) / (voltage_max - voltage_min)) + dec_min)
        return f"0x{hex_value:04X}"

    def swap_bytes(hex_value):
        return f"0x{hex_value[4:]}{hex_value[2:4]}"

    # Execute AO commands
    for address, voltage in zip(LnT_AO_Address_List, LnT_AO_Address_Values):
        hex_output = voltage_to_hex(voltage)
        if hex_output:
            shifted_output = swap_bytes(hex_output)
            command = f"/usr/share/vmetoolkit/examples/singleAccess/MasterSgl w 0x39 {address} 16 {shifted_output}"
            try:
                subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
                print(f"AO Sent: {address} -> {shifted_output} ({voltage}V)")
            except subprocess.CalledProcessError as e:
                print(f"Error sending AO {address}: {e}")

    # 3️⃣ SERIAL COMMUNICATION FOR DI/AI VALUES

    def Ref_DI_AI_Writedata(portname):
        try:
            with serial.Serial(portname, baudrate=115200, timeout=1) as ser:
                DI_Ref_Binary = "1" * 208
                DI_Ref_Value_Hex = hex(int(DI_Ref_Binary, 2))[2:].upper().zfill(52)  # Ensure 52-character hex output

                message = DI_Ref_Value_Hex + "00000" * 48
                ser.write(message.encode())
                print(f"Serial Sent: {message}")
        except serial.SerialException as e:
            print(f"Serial Error: {e}")

    Ref_DI_AI_Writedata(portname)

    # Read Ref_DI/AI values from serial port
    with serial.Serial(portname, baudrate=115200, timeout=1) as ser:
        while True:

            if ser.in_waiting:
                Ref_AO_P10V_Result = ser.readline().decode('utf-8').strip()
                print(f"Received: {Ref_AO_P10V_Result}")
                break
        
    def parse_voltage_string(data):
        # Step 1: Remove first 24 characters
        trimmed = data[24:]
        
        # Step 2: Process in 5-character blocks
        voltages = []
        for i in range(0, len(trimmed), 5):
            block = trimmed[i:i+5]
            if len(block) < 5:
                break  # skip incomplete blocks
            sign = '-' if block[0] == '1' else '+'
            integer_part = block[1:3]
            decimal_part = block[3:]
            voltage_str = f"{sign}{integer_part}.{decimal_part}"
            voltages.append(voltage_str)
            
        return voltages
    result = parse_voltage_string(Ref_AO_P10V_Result)
    return result

#Getting RESULT   (Display in Ref AO -10V Column)

#   Ref_AO_P10V_Result = FFFFFFFFFFFFFFFFFFFFFFFF110001100011000110001100011000110001100011000110001100011000

#   Separate digital value and analog value from Ref_AO_P10V_Result
#  Ref_AO_P10V_Result = FFFFFFFFFFFFFFFFFFFFFFFF
# 11000 11000 11000 11000 11000 11000 11000 11000 11000 11000 11000 11000

#RESULT   (Display in Ref AO -10V Column)

# Ref_AO_P10V_Result = [+10.00, +10.00, +10.00, +10.00, +10.00, +10.00, 
#                     +10.00, +10.00, +10.00, +10.00, +10.00, +10.00]

