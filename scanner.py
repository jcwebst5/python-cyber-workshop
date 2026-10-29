import socket

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
     
     ports = [21, 22, 80, 443, 8000]
     for port in ports:
          scanner_socket = socket.socket()
          scanner_socket.settimeout(1)
          address = (target, port)

          try:

               scanner_socket.connect(address)
               print(f"Success -> Port {port} is OPEN")

          except:
               print(f"Failure -> Port {port} is CLOSED")
               
          scanner_socket.close()

else: 
     is_valid = False
     print("Invalid IP address")
    

