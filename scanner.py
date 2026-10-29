target = input("Enter target IP: ")
print(f"Scanning target: {target}")

octets = target.split(".")

if len(octets) == 4:
    print("IP has 4 octets")
else:
    print("Invalid IP address")

for octet in octets:
    if octet.isdigit():
        octet_number = int(octet)
        if 0 <= octet_number <= 255:
            print("Valid octet")
        else:
            print("Invalid octet")
else: 
    print("Invalid IP format")

