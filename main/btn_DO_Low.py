import subprocess
import serial
import re

portname = '/dev/ttyS0'
Ref_DO_Low_results = ''   # keep same name

def ret_btn_result():
    """
    Sends DO values, writes DI reference, reads DO Low results from serial,
    processes them into a binary list, and returns it.
    """

    global Ref_DO_Low_results

    # --- 1️⃣ SEND DO VALUES TO VME ---
    LnT_DO_Address_List = ['0x9D8602', '0x9D8604']
    LnT_DO_Address_Values = ['0000000000000000', '0000000000000000']  # example values

    # Convert binary to hex and swap byte order
    hex_values = [hex(int(binary, 2))[2:].zfill(4) for binary in LnT_DO_Address_Values]
    swapped_hex_values = [f"0x{h[2:4]}{h[0:2]}" for h in hex_values]

    for address, hex_value in zip(LnT_DO_Address_List, swapped_hex_values):
        command = f"sshpass -p 'test123' ssh test@192.168.2.100 " \
                  f"/usr/share/vmetoolkit/examples/singleAccess/MasterSgl w 0x39 {address} 16 {hex_value}"
        try:
            subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            print(f"DO Sent: {address} -> {hex_value}")
        except subprocess.CalledProcessError as e:
            print(f"Error sending DO {address}: {e}")

    # --- 2️⃣ SEND DI REFERENCE DATA ---
    def Ref_DI_AI_Writedata(portname):
        try:
            with serial.Serial(portname, baudrate=115200, timeout=1) as ser:
                DI_Ref_Binary = "1" * 208
                DI_Ref_Value_Hex = hex(int(DI_Ref_Binary, 2))[2:].upper().zfill(52)
                message = DI_Ref_Value_Hex + "00000" * 48
                ser.write(message.encode())
                print(f"Serial Sent: {message}")
        except serial.SerialException as e:
            print(f"Serial Error: {e}")

    Ref_DI_AI_Writedata(portname)

    # --- 3️⃣ READ Ref_DO_Low_results FROM SERIAL ---
    with serial.Serial(portname, baudrate=115200, timeout=1) as ser:
        while True:
            if ser.in_waiting:
                Ref_DO_Low_results = ser.readline().decode('utf-8').strip()
                print(f"Received: {Ref_DO_Low_results}")
                break

    # --- 4️⃣ PROCESS Ref_DO_Low_results ---
    hex_24 = Ref_DO_Low_results[:24]   # first 24 hex chars (digital)
    merged_binary = ""

    for i in range(0, len(hex_24), 4):
        chunk = hex_24[i:i+4]
        bin_val = bin(int(chunk, 16))[2:].zfill(16)
        merged_binary += bin_val

    # Convert to list of integers
    binary_list = [int(bit) for bit in merged_binary]

    # Trim last 2 unused bits
    binary_list = binary_list[:-2]

    print("Final Binary List:", binary_list)
    return binary_list
