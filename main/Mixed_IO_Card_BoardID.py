import subprocess
import re

# SSH command
command = "sshpass -p 'test123' ssh test@192.168.2.100 /usr/share/vmetoolkit/examples/singleAccess/MasterSgl r 0x39 0x9d8002 16"

# Execute command
result = subprocess.getoutput(command)

# Example output: "read at VME address  0x9d8002 = 0x809d"
match = re.search(r'0x([0-9a-fA-F]+)\s*=\s*0x([0-9a-fA-F]+)', result)

if match:
    addr = match.group(1).lower()
    value = match.group(2).lower().zfill(4)  # Ensure 4 digits
    high_byte = value[:2]
    low_byte = value[2:]
    
    # Combine to get final format: 0x9d8002 = 0x9d80
    formatted = f"0x{addr} = 0x{low_byte}{high_byte}"
    print(formatted)
else:
    print("Failed to parse the output.")