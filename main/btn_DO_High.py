import subprocess
import serial

portname = '/dev/ttyS0'
Ref_DO_High_results = ''


def defval():
    """
    Convert first 7 hex digits from Ref_DO_High_results to binary list
    (with last 2 bits removed).
    """
    global Ref_DO_High_results
    hex_24 = Ref_DO_High_results[:7]

    merged_binary = ""
    for i in range(0, len(hex_24), 4):
        chunk = hex_24[i:i+4]
        bin_val = bin(int(chunk, 16))[2:].zfill(16)
        merged_binary += bin_val

    binary_list = [int(bit) for bit in merged_binary]

    # Remove last 2 bits
    binary_list = binary_list[:-2]

    return binary_list


def ret_btn_result():
    """
    Send DO commands via SSH, then write DI/AI reference values to serial,
    and finally read response from serial.
    """
    LnT_DO_Address_List = ['0x9D8602', '0x9D8604']
    LnT_DO_Address_Values = ['1111111111111111',
                             '1111111111111111']

    # Convert binary to hex and swap bytes
    hex_values = [hex(int(binary, 2))[2:].zfill(4) for binary in LnT_DO_Address_Values]
    swapped_hex_values = [f"0x{h[2:4]}{h[0:2]}" for h in hex_values]

    # Execute DO commands
    for address, hex_value in zip(LnT_DO_Address_List, swapped_hex_values):
        command = f"sshpass -p 'test123' ssh test@192.168.2.100 " \
                  f"/usr/share/vmetoolkit/examples/singleAccess/MasterSgl w 0x39 {address} 16 {hex_value}"
        try:
            subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            print(f"DO Sent: {address} -> {hex_value}")
        except subprocess.CalledProcessError as e:
            print(f"Error sending DO {address}: {e}")

    def Ref_DI_AI_Writedata(portname):
        try:
            with serial.Serial(portname, baudrate=115200, timeout=1) as ser:
                DI_Ref_Binary = "1" * 208
                DI_Ref_Value_Hex = hex(int(DI_Ref_Binary, 2))[2:].upper().zfill(52)
                message = DI_Ref_Value_Hex + ("00000" * 48)
                ser.write(message.encode())
                print(f"Serial Sent: {message}")
        except serial.SerialException as e:
            print(f"Serial Error: {e}")

    Ref_DI_AI_Writedata(portname)

    # Read Ref_DI/AI values from serial port
    global Ref_DO_High_results
    with serial.Serial(portname, baudrate=115200, timeout=1) as ser:
        while True:
            if ser.in_waiting:
                data = ser.readline().decode('utf-8').strip()
                Ref_DO_High_results = data
                print(f"Received: {data}")
                break

    hex_24 = Ref_DO_High_results[:24]

    merged_binary = ""
    for i in range(0, len(hex_24), 4):
        chunk = hex_24[i:i+4]
        bin_val = bin(int(chunk, 16))[2:].zfill(16)
        merged_binary += bin_val

    binary_list = [int(bit) for bit in merged_binary]

    # Remove last 2 bits
    binary_list = binary_list[:-2]

    print("Final Binary List:", binary_list)
    return binary_list
