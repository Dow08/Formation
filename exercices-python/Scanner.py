import socket
# definir la cible et les ports à tester 
#on utilise 127.0.0.1 comme ( localhost) pour scanner t'as propore machine en toute sécurité.

ip_cible = "127.0.0.1"
ports_a_tester = [21,22,23,25,80,443,8080]

print("---debut du scan---")

# crée une boucle pour tester chaque port  de notre liste un par un for port in ports_a_tester:
#initialisation du canal  de communication ( le socket)
for port in ports_a_tester:
    print(f"test du port {port}")
    canal = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = famille d'adresse ipv4, 
#SOCK_STREAM = type de socket pour le protocole TCP
    canal.settimeout(1)
# on definit un délai d'attente maximum d'une seconde 
#sans ça, le scripte bloquera trop longtemps sur u port filtré. canal.settimout(1)
    resultat = canal.connect_ex((ip_cible, port))
    if resultat == 0:
        print(f"le port {port} est ouvert")
    else:
        print(f"le port {port} est fermé")
    canal.close()
 

