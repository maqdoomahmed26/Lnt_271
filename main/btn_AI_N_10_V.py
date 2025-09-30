import subprocess
import serial
import re

portname = '/dev/ttyS0'
def ret_btn_result():
    # return ["-10.00"]    * 12
    
    # 3️⃣ SERIAL COMMUNICATION FOR DI/AI VALUES

    def Ref_DI_AI_Writedata(portname):
        try:
            with serial.Serial(portname, baudrate=115200, timeout=1) as ser:
                DI_Ref_Binary = "1" * 208
                DI_Ref_Value_Hex = hex(int(DI_Ref_Binary, 2))[2:].upper().zfill(52)  # Ensure 52-character hex output

                message = DI_Ref_Value_Hex + "11000" * 48
                ser.write(message.encode())
                print(f"Serial Sent: {message}")
        except serial.SerialException as e:
            print(f"Serial Error: {e}")

    Ref_DI_AI_Writedata(portname)

    # Read Ref_DI/AI values from serial port
    with serial.Serial(portname, baudrate=115200, timeout=1) as ser:
        while True:

            if ser.in_waiting:
                data = ser.readline().decode('utf-8').strip()
                print(f"Received: {data}")
                break

    # # READ LnT_DI & LnT_AI VALUES FROM MEMORY ADDRESSES

   
    # #LnT_AI_Read_Values Part

    LnT_AI_Address_List = [0x9D8A02, 0x9D8A04, 0x9D8A06, 0x9D8A08, 0x9D8A0A,
                       0x9D8A0C, 0x9D8A0E, 0x9D8A10, 0x9D8A12, 0x9D8A14,
                       0x9D8A16, 0x9D8A18]

    # Regular expression to capture the value after '='
    pattern = r"=\s*(0x[0-9A-Fa-f]+)"

    # Function to execute the command, extract, and reverse hex values
    def fetch_LnT_AI_address_data(address):
        try:
            # command = f"sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0x9d8002 16"
            command = f"sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 {address} 16"
            # command = f"/usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 {address} 16"
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            matches = re.findall(pattern, result.stdout)
            
            # Ensure values are 4 digits long (e.g., 0x80 → 0x0080)
            return [f"0x{''.join(reversed([m[2:].zfill(4)[i:i+2] for i in range(0, len(m[2:].zfill(4)), 2)]))}" for m in matches]
        
        except subprocess.CalledProcessError as e:
            return [f"Error for {address}: {e}"]

    # Function to convert code to voltage
    def code_to_voltage(value):
        if (value & 0x8000) == 0x8000:
            value = (value ^ 0xFFFF) + 1
            return -((value / 32768) * 10.0)
        return (value / 32768) * 10.0

    # Function to format voltage
    def format_voltage(voltage):
        # return "-10.00" if -0.01 <= voltage <= 0.01 else f"{voltage:+06.2f}"
        return f"{voltage:+06.2f}"
    # Fetch and process data
    LnT_AI_Address_Data = [item for address in LnT_AI_Address_List for item in fetch_LnT_AI_address_data(address)]
    voltages = [code_to_voltage(int(h, 16)) for h in LnT_AI_Address_Data if "Error" not in h]
    Lnt_AI_N_10V_Result = [format_voltage(v) for v in voltages]

    # Print results
    print(Lnt_AI_N_10V_Result)

    return Lnt_AI_N_10V_Result

#RESULT   (Display in LnT AI 0V Column)

# Lnt_AI_N_10V_Result = [00.00, 00.00, 00.00, 00.00, 00.00, 00.00,
#                     00.00, 00.00, 00.00, 00.00, 00.00, 00.00,
#                     00.00, 00.00, 00.00, 00.00, 00.00, 00.00,
#                     00.00, 00.00, 00.00, 00.00, 00.00, 00.00,
#                     00.00, 00.00, 00.00, 00.00, 00.00, 00.00,
#                     00.00, 00.00, 00.00, 00.00, 00.00, 00.00,
#                     00.00, 00.00, 00.00, 00.00, 00.00, 00.00,
#                     00.00, 00.00, 00.00, 00.00, 00.00, 00.00]

