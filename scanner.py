target = input("Enter target IP: ")
print(f"Scanning target: {target}")

octets = target.split(".")
is_valid = True

if len(octets) == 4:
    for octet in octets:
            if octet.isdigit():
                octet_number = int(octet)
                if 0 <= octet_number <= 255:
                     pass
                else:
                    is_valid = False
else:
     is_valid = False
     
if is_valid:
     print("Valid IP address")
else: 
     is_valid = False
     print("Invalid IP address")
    

