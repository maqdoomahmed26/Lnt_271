import subprocess
import serial
import re
portname = '/dev/ttyS0'
Ref_DO_Low_results = ''
def ret_btn_result():
        # 1️⃣ SEND LnT_DO VALUES (Digital Output)(Table3)
    LnT_DO_Address_List = ['0x3D840C', '0x3D840E', '0x3D8410', '0x3D8412', '0x3D8414', '0x3D8416']
    # LnT_DO_Address_Values = ['1111111111111111',
    #                         '1111111111111111',
    #                         '1111111111111111',
    #                         '1111111111111111', 
    #                         '1111111111111111',
    #                         '1111111111111111']
    LnT_DO_Address_Values = ['0000000000000000',
                             '0000000000000000',
                             '0000000000000000',
                             '0000000000000000',
                             '0000000000000000',
                             '0000000000000000']

    # Convert binary to hex and swap bytes
    hex_values = [hex(int(binary, 2))[2:].zfill(4) for binary in LnT_DO_Address_Values]
    swapped_hex_values = [f"0x{h[2:4]}{h[0:2]}" for h in hex_values]

    # Execute DO commands
    for address, hex_value in zip(LnT_DO_Address_List, swapped_hex_values):
        command = f"/usr/share/vmetoolkit/examples/singleAccess/MasterSgl w 0x39 {address} 16 {hex_value}"
        try:
            subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            print(f"DO Sent: {address} -> {hex_value}")
        except subprocess.CalledProcessError as e:
            print(f"Error sending DO {address}: {e}")


    # 2️⃣ SEND LnT_AO VALUES (Analog Output)
    LnT_AO_Address_List = [
        '0x6D0C6C', '0x6D0C6E', '0x6D0C70', '0x6D0C72', '0x6D0C74', '0x6D0C76',
        '0x6D0C78', '0x6D0C7A', '0x6D0C7C', '0x6D0C7E', '0x6D0C80', '0x6D0C82'
    ]
    LnT_AO_Address_Values = [
        # '-10.00', '-10.00', '-10.00', '-10.00', '-10.00', '-10.00',
        # '-10.00', '-10.00', '-10.00', '-10.00', '-10.00', '-10.00'

        '+00.00', '+00.00', '+00.00', '+00.00', '+00.00', '+00.00',
        '+00.00', '+00.00', '+00.00', '+00.00', '+00.00', '+00.00'

        # '+10.00', '+10.00', '+10.00', '+10.00', '+10.00', '+10.00',
        # '+10.00', '+10.00', '+10.00', '+10.00', '+10.00', '+10.00'
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
                # DI_Ref_Binary = "0111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111101111"
                # DI_Ref_Binary="1100000000000010100000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
                # DI_Ref_Value_Hex = hex(int(DI_Ref_Binary, 2))[2:].upper().zfill(24)
                # DI_Ref_Value_Hex = hex(int(DI_Ref_Binary, 2))[2:].upper().zfill(52)  # Ensure 52-character hex output
                DI_Ref_Value_Hex = hex(int(DI_Ref_Binary, 2))[2:].upper().zfill(52)  # Ensure 52-character hex output

                message = DI_Ref_Value_Hex + "00500" * 48
                ser.write(message.encode())
                print(f"Serial Sent: {message}")
        except serial.SerialException as e:
            print(f"Serial Error: {e}")

    Ref_DI_AI_Writedata(portname)

    # # Read Ref_DI/AI values from serial port
    with serial.Serial(portname, baudrate=115200, timeout=1) as ser:
        while True:

            if ser.in_waiting:
                data = ser.readline().decode('utf-8').strip()
                Ref_DO_High_results = data
                print(f"Received: {data}")
                break

            ###########################################
    LnT_DI_Address_List = [
        '0x4E080C', '0x4E080E', '0x4E0810', '0x4E0812', '0x4E0814',
        '0x4E0816', '0x4E0818', '0x4E081A', '0x4E081C', '0x4E081E',
        '0x4E0820', '0x4E0822', '0x4E0824'
    ]

    # Initialize an array to store the results
    LnT_DI_results = []

    # Regular expression to capture the value after '=' (e.g., 0xc03f)
    pattern = r"=\s*(0x[0-9A-Fa-f]+)"

    # Loop through each address and execute the command
    for address in LnT_DI_Address_List:
        command = f"/usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 {address} 16"
        try:
            # Execute the command
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            
            # Find the match using regular expression
            matches = re.findall(pattern, result.stdout)
            
            # Process each matched value
            for match in matches:
                hex_value = match[2:]  # Remove the '0x' prefix
                
                # Convert the hex value to an integer
                variable = int(hex_value, 16)

                # Extract LSB and MSB using bitwise operations
                LSB = (variable & 0xFF00) >> 8
                MSB = variable & 0x00FF
                
                # Combine MSB and LSB (MSB << 8) | LSB
                combined = (MSB << 8) | LSB
                
                # Convert combined result to binary and format it to 16 bits
                binary_value = format(combined, '016b')
                
                # Add the binary result to the list
                LnT_DI_results.append(binary_value)
            
        except subprocess.CalledProcessError as e:
            LnT_DI_results.append(f"Error for {address}: {e}")
        except Exception as e:
            LnT_DI_results.append(f"Unexpected error for {address}: {e}")

    # Print the collected binary data, joined by commas
    print("LnT DI Values:", ", ".join(LnT_DI_results))
    
            ############################################

    # # READ LnT_DI & LnT_AI VALUES FROM MEMORY ADDRESSES

    # LnT_DI_Address_List = [
    #     '0x4E080C', '0x4E080E', '0x4E0810', '0x4E0812', '0x4E0814',
    #     '0x4E0816', '0x4E0818', '0x4E081A', '0x4E081C', '0x4E081E',
    #     '0x4E0820', '0x4E0822', '0x4E0824'
    # ]

    # # Initialize an array to store the results
    # LnT_DI_results = []
    # # Regular expression to capture the value after '=' (e.g., 0xc03f)
    # pattern = r"=\s*(0x[0-9A-Fa-f]+)"

    # # Loop through each address and execute the command

    # for address in LnT_DI_Address_List:
    #     command = f"/usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 {address} 16"    
    #     try:
    #         # Execute the command
    #         result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    #         # Find the match using regular expression
    #         matches = re.findall(pattern, result.stdout)
            
    #         # Process each matched value
    #         for match in matches:
    #             hex_value = match[2:]  # Remove the '0x' prefix
    #             # Reverse the byte order (e.g., 'c03f' -> '3f0c')
    #             reversed_value = ''.join(reversed([hex_value[i:i+2] for i in range(0, len(hex_value), 2)]))
                
    #             # Convert reversed hexadecimal to integer
    #             int_value = int(reversed_value, 16)
                
    #             # Convert integer to binary and format it to 16 bits
    #             binary_value = format(int_value, '016b')
                
    #             LnT_DI_results.append(binary_value)
            
    #     except subprocess.CalledProcessError as e:
    #         LnT_DI_results.append(f"Error for {address}: {e}")
    #     except Exception as e:
    #         LnT_DI_results.append(f"Unexpected error for {address}: {e}")

    # # Print the collected binary data, joined by commas
    # # print(",".join(LnT_DI_results))

    # print("LnT DI Values:", ", ".join(LnT_DI_results))







    # #LnT_AI_Read_Values Part



    LnT_AI_Address_List = [
        0x6D0C0C, 0x6D0C0E, 0x6D0C10, 0x6D0C12, 0x6D0C14, 0x6D0C16,
        0x6D0C18, 0x6D0C1A, 0x6D0C1C, 0x6D0C1E, 0x6D0C20, 0x6D0C22,
        0x6D0C24, 0x6D0C26, 0x6D0C28, 0x6D0C2A, 0x6D0C2C, 0x6D0C2E,
        0x6D0C30, 0x6D0C32, 0x6D0C34, 0x6D0C36, 0x6D0C38, 0x6D0C3A,
        0x6D0C3C, 0x6D0C3E, 0x6D0C40, 0x6D0C42, 0x6D0C44, 0x6D0C46,
        0x6D0C48, 0x6D0C4A, 0x6D0C4C, 0x6D0C4E, 0x6D0C50, 0x6D0C52,
        0x6D0C54, 0x6D0C56, 0x6D0C58, 0x6D0C5A, 0x6D0C5C, 0x6D0C5E,
        0x6D0C60, 0x6D0C62, 0x6D0C64, 0x6D0C66, 0x6D0C68, 0x6D0C6A,
    ]

    # Regular expression to capture the value after '='
    pattern = r"=\s*(0x[0-9A-Fa-f]+)"

    # Function to execute the command, extract, and reverse hex values
    def fetch_LnT_AI_address_data(address):
        try:
            command = f"/usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 {address} 16"
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
        return "0.00" if -0.01 <= voltage <= 0.01 else f"{voltage:.2f}"

    # Fetch and process data
    LnT_AI_Address_Data = [item for address in LnT_AI_Address_List for item in fetch_LnT_AI_address_data(address)]
    voltages = [code_to_voltage(int(h, 16)) for h in LnT_AI_Address_Data if "Error" not in h]
    formatted_voltages = [format_voltage(v) for v in voltages]

    # Print results
    print(formatted_voltages)
    print (f'Rev. Data :  {Ref_DO_High_results}')
    # Step 1: Take the first 24 hex characters
    hex_24 = Ref_DO_High_results[:24]

    # Step 2: Convert to binary in chunks of 4 hex digits
    merged_binary = ""
    for i in range(0, len(hex_24), 4):
        chunk = hex_24[i:i+4]
        bin_val = bin(int(chunk, 16))[2:].zfill(16)  # 4 hex digits = 16 bits
        merged_binary += bin_val

    # Step 3: Convert merged binary string into a list of integers
    binary_list = [int(bit) for bit in merged_binary]

    # Step 4: Remove last 2 bits
    binary_list = binary_list[:-2]

    print("Final Binary List:", binary_list)
    return binary_list


    # # RESULTS

    # [maqdoom@localhost ~]$ python All_Files.py
    # DO Sent: 0x3D840C -> 0xffff
    # DO Sent: 0x3D840E -> 0xffff
    # DO Sent: 0x3D8410 -> 0xffff
    # DO Sent: 0x3D8412 -> 0xffff
    # DO Sent: 0x3D8414 -> 0xffff
    # DO Sent: 0x3D8416 -> 0xffff
    # AO Sent: 0x6D0C6C -> 0x000C (+05.00V)
    # AO Sent: 0x6D0C6E -> 0x000C (+05.00V)
    # AO Sent: 0x6D0C70 -> 0x000C (+05.00V)
    # AO Sent: 0x6D0C72 -> 0x000C (+05.00V)
    # AO Sent: 0x6D0C74 -> 0x000C (+05.00V)
    # AO Sent: 0x6D0C76 -> 0x000C (+05.00V)
    # AO Sent: 0x6D0C78 -> 0x000C (+05.00V)
    # AO Sent: 0x6D0C7A -> 0x000C (+05.00V)
    # AO Sent: 0x6D0C7C -> 0x000C (+05.00V)
    # AO Sent: 0x6D0C7E -> 0x000C (+05.00V)
    # AO Sent: 0x6D0C80 -> 0x000C (+05.00V)
    # AO Sent: 0x6D0C82 -> 0x000C (+05.00V)

    # Serial Sent: FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF004500045000450004500045000450004500045000450004500045000450004500045000450004500045000450004500045000450004500045000450004500045000450004500045000450004500045000450004500045000450004500045000450004500045000450004500045000450004500045000450

    # Received: 000000000000000000000003004980049800497004980049700497004970049700500005000050000500

    # LnT DI Values: 1111111111111111, 1111111111111111, 1111111111111111, 1111111111111111, 1111111111111111, 1111111111111111, 1111111111111111, 1111111111111111, 1111111111111111, 1111111111111111, 1111111111111111, 1111111111111111, 0000111111111111

    # ['4.50', '4.50', '4.50', '4.50', '4.50', '4.50', '4.50', '4.50', '4.49',
    #  '4.50', '4.50', '4.50', '4.50', '4.50', '4.49', '4.49', '4.50', '4.49', 
    # '4.49', '4.49', '4.49', '4.49', '4.49', '4.49', '4.49', '4.49', '4.49', 
    # '4.50', '4.49', '4.49', '4.49', '4.49', '4.50', '4.50', '4.50', '4.50', 
    # '4.50', '4.50', '4.50', '4.50', '4.50', '4.50', '4.50', '4.50', '4.50', '4.50', '4.50', '4.50']




#Getting RESULT   (Display in Ref_DO_High_results Column)

# Ref_DO_High_results = 000000000000000000000003000000000000000000000000000000000000000000000000000000000000

#   Separate digital value and analog value from Ref_DO_High_results
#  AO_0V_Result = 000000000000000000000003
# 000000000000000000000000000000000000000000000000000000000000

#RESULT   (Display in Ref DO High Column)
# Ref_DI_High_results : [0000000000000000,0000000000000000,0000000000000000,
#                        0000000000000000,0000000000000000,1100000000000000]
