
            # new_list replace LnT_DI_Values_Rx

            # new_list = [
            #             '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', 
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #             '1', '1', '1', '1'
            #         ]
            
            # # formatted_voltages replace LnT_AI_Values_Rx

            # formatted_voltages=['4.50', '4.50', '4.50', '4.50', '4.50', '4.50', '4.50', '4.50', '4.49',
            #                     '4.50', '4.50', '4.50', '4.50', '4.50', '4.49', '4.49', '4.50', '4.49', 
            #                     '4.49', '4.49', '4.49', '4.49', '4.49', '4.49', '4.49', '4.49', '4.49', 
            #                     '4.50', '4.49', '4.49', '4.49', '4.49', '4.50', '4.50', '4.50', '4.50', 
            #                     '4.50', '4.50', '4.50', '4.50', '4.50', '4.50', '4.50', '4.50', '4.50', 
            #                     '4.50', '4.50', '4.50']
            
            # # value_dg_output replace Ref_DO_Values_Rx
            # value_dg_output=[
            #                 '1', '0', '1', '1', '0', '1', '0', '1', '1', '1',
            #                 '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #                 '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #                 '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #                 '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #                 '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #                 '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #                 '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #                 '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #                 '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
            #                 '1', '1', '1', '1'
            #                 ]
            
            # # value_an_output replace Ref_AO_Values_Rx
            # value_an_output=['+03.50', '+03.50', '+03.50', '+03.50', '+03.50', '+03.50', 
            #                  '+03.50', '+03.50', '+03.49','+03.50', '+03.50', '+03.50']
            # return JsonResponse({
            #                         "status": "success", 
            #                         "value_dg_input": new_list, 
            #                         "value_an_input": formatted_voltages,
            #                         "value_dg_output": value_dg_output,  # Now a list                                  
            #                         "value_an_output": value_an_output
            #                         })








            # Print results
            # print(formatted_voltages)


            # LnT_AI_Address_List = [
            #     0x6D0C0C, 0x6D0C0E, 0x6D0C10, 0x6D0C12, 0x6D0C14, 0x6D0C16,
            #     0x6D0C18, 0x6D0C1A, 0x6D0C1C, 0x6D0C1E, 0x6D0C20, 0x6D0C22,
            #     0x6D0C24, 0x6D0C26, 0x6D0C28, 0x6D0C2A, 0x6D0C2C, 0x6D0C2E,
            #     0x6D0C30, 0x6D0C32, 0x6D0C34, 0x6D0C36, 0x6D0C38, 0x6D0C3A,
            #     0x6D0C3C, 0x6D0C3E, 0x6D0C40, 0x6D0C42, 0x6D0C44, 0x6D0C46,
            #     0x6D0C48, 0x6D0C4A, 0x6D0C4C, 0x6D0C4E, 0x6D0C50, 0x6D0C52,
            #     0x6D0C54, 0x6D0C56, 0x6D0C58, 0x6D0C5A, 0x6D0C5C, 0x6D0C5E,
            #     0x6D0C60, 0x6D0C62, 0x6D0C64, 0x6D0C66, 0x6D0C68, 0x6D0C6A,
            # ]

            # # Regular expression to capture the value after '='
            # pattern = r"=\s*(0x[0-9A-Fa-f]+)"

            # # Function to execute the command, extract, and reverse hex values
            # def fetch_LnT_AI_address_data(address):
            #     try:
            #         command = f"/usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 {address} 16"
            #         result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            #         matches = re.findall(pattern, result.stdout)
            #         return [f"0x{''.join(reversed([m[2:][i:i+2] for i in range(0, len(m[2:]), 2)]))}" for m in matches]
            #     except subprocess.CalledProcessError as e:
            #         return [f"Error for {address}: {e}"]

            # # Function to convert code to voltage
            # def code_to_voltage(value):
            #     if (value & 0x8000) == 0x8000:
            #         value = (value ^ 0xFFFF) + 1
            #         return -((value / 32768) * 10.0)
            #     return (value / 32768) * 10.0

            # # Function to format voltage
            # def format_voltage(voltage):
            #     return "0.00" if -0.01 <= voltage <= 0.01 else f"{voltage:.2f}"

            # # Fetch and process data
            # LnT_AI_Address_Data = [item for address in LnT_AI_Address_List for item in fetch_LnT_AI_address_data(address)]
            # voltages = [code_to_voltage(int(h, 16)) for h in LnT_AI_Address_Data if "Error" not in h]
            # formatted_voltages = [format_voltage(v) for v in voltages]

            # # Print results
            # # print(", ".join(LnT_AI_Address_Data))
            # # print(voltages)
            # print(formatted_voltages)






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