    
print('''
      
$$$$$$$\                       $$\                                                                      
$$  __$$\                      $$ |                                                                     
$$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\          $$$$$$$\  $$$$$$$\ $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\ 
$$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|        $$  _____|$$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$  ____/ $$ /  $$ |$$ |  \__| $$ |          \$$$$$$\  $$ /      $$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |      $$ |  $$ |$$ |       $$ |$$\        \____$$\ $$ |     $$  __$$ |$$ |  $$ |$$   ____|$$ |       
$$ |      \$$$$$$  |$$ |       \$$$$  |      $$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |      
\__|       \______/ \__|        \____/       \_______/  \_______|\_______|\__|  \__| \_______|\__|
|                                                                                                |
|--------------------------------------------Coded by alpisaoglu--------------------------------------|''')

print("\nGithub: https://github.com/alpisaoglu\n")

import socket
import time
import sys

def scanHost(ip_address, startPort, endPort):
    print("Scan Start %s" % ip_address)
    start_time = time.time()  
    # Port taramasının başladığı zaman
    tcp_scan(ip_address, startPort, endPort)
    end_time = time.time()  
    #Port taramasının bittiği zaman
    elapsed_time = end_time - start_time 
    #Port taraması süresinin hesapladığı zaman. 
    print("Scan completed in %d seconds" % elapsed_time)
    

def tcp_scan(ip_address, startPort, endPort):
    try:
        for port in range(startPort, endPort):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #Sock_Stream parametresi TCP taraması yapar. Eğer UDP taraması gerçekleştirilmek isteniyorsa ##socket.SOCK_DGRAM## kullanılmalıdır. 
            result = s.connect_ex((ip_address, port))
            if result == 0:
                # Neden 0? Çünjü ##connect_ex## eğer port açık değilse 1 değeri döndürdüğünden dolayı. Eğer sonuç 0 eşitse port açık olduğunu yazdırıyoruz.
                print("%d is open" % port)
                s.close()
    except Exception:
        sys.exit()

def main():
    ip_address = str(input("IP ADDRESS :"))
    startPort = int(input("PORT START :"))
    endPort = int(input("PORT END :"))
    scanHost(ip_address, startPort, endPort)

main()
