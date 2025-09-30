import subprocess
import serial
import re

portname = '/dev/ttyS0'  # Update as needed

def ret_btn_result():
    """
    Sends DI reference data (all 0's), reads DI Low values from VME,
    processes the response, and returns a flattened list of 32 bits.
    """

    # --- Send DI Reference Data over Serial ---
    def Ref_DI_AI_Writedata(portname):
        try:
            with serial.Serial(portname, baudrate=115200, timeout=1) as ser:

                DI_Ref_Binary = "0"* 32 + "1"*176
                # DI_Ref_Binary = "0100000000000000000000000000010011111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
               
                DI_Ref_Value_Hex = hex(int(DI_Ref_Binary, 2))[2:].upper().zfill(52)

                message = DI_Ref_Value_Hex + "00000" * 48
                ser.write(message.encode())
                print(f"Serial Sent: {message}")
        except serial.SerialException as e:
            print(f"Serial Error: {e}")

    Ref_DI_AI_Writedata(portname)

    # --- Read back any response (optional, if device sends) ---
    with serial.Serial(portname, baudrate=115200, timeout=1) as ser:
        if ser.in_waiting:
            data = ser.readline().decode('utf-8').strip()
            print(f"Serial Received: {data}")

    # --- VME Addresses to Read ---
    LnT_DI_Address_List = ['0x9D8202', '0x9D8402']

    # --- Collect DI Low Results ---
    LnT_DI_Low_results = []
    pattern = r"=\s*(0x[0-9A-Fa-f]+)"   # Extract hex after '='

    for address in LnT_DI_Address_List:
        command = f"sshpass -p 'test123' ssh test@192.168.2.100 " \
                  f"/usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 {address} 16"

        try:
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            matches = re.findall(pattern, result.stdout)

            for match in matches:
                hex_value = match[2:]           # strip '0x'
                hex_value = hex_value.zfill(4)  # make sure 16-bit always (e.g. "0180")

                # --- Byte swap (e.g. "0180" -> "8001") ---
                swapped = hex_value[2:4] + hex_value[0:2]

                int_value = int(swapped, 16)
                binary_value = format(int_value, '016b')
                LnT_DI_Low_results.append(binary_value)

                print(f"Raw from VME: {match}")
                print(f"zfill:        {hex_value}")
                print(f"Swapped:      {swapped}")
                print(f"Binary:       {binary_value}")

        except subprocess.CalledProcessError as e:
            LnT_DI_Low_results.append(f"Error for {address}: {e}")
        except Exception as e:
            LnT_DI_Low_results.append(f"Unexpected error for {address}: {e}")

    print("LnT DI Low Values:", ", ".join(LnT_DI_Low_results))

    # --- Flatten into 32 bits ---
    bit_list = []
    for value in LnT_DI_Low_results:
        bit_list.extend([int(bit) for bit in value[::-1]])

    return bit_list
