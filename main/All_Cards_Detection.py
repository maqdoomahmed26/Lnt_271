from django.http import JsonResponse
from django.shortcuts import render
import subprocess
import re
# Card detection function
def detect_card(card_type, command):
    return " detected: "
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
        output = result.stdout
        vme_address = output[output.index('0x') : output.index('0x') + 8]
        value = output[output.index('= 0x') + 2 : len(output) -1 ]
        vme_address = vme_address.upper()
        value = value.upper()
        if card_type == 'DI' and vme_address == '0X970002' and value == '0X84E':
            return " detected: "
        elif card_type == 'DO' and vme_address == '0X9D8002' and value == '0X843D':
            return " detected: "
        elif card_type == 'AIO' and vme_address == '0X8D0002' and value == '0XC6D':
            return " detected: "
        else:
            return f"No {card_type} data found."

    except subprocess.CalledProcessError as e:
        return f"Error running {card_type} detection command: {e}"

# View to handle the AJAX detection request
def detect(card_type):
    commands = {
        "DO": "/usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0X970002 16",
        "DI": "/usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0X9D8002 16",
        "AIO": "/usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0x8D0002 16"
    }

    if card_type in commands:
        result = detect_card(card_type, commands[card_type])
        return JsonResponse({"message": result})
    else:
        return JsonResponse({"message": "Invalid card type"})
