import requests
# si module not found installer avec pip install requests
# 1. Configuration de base
url_cible = "http://www.google.com"
# Liste de mots à tester
mots_a_tester = ["upload", "admin", "login", "test", "root", "password", "secret", "backup", "config", "debug", "dev", "staging", "prod", "demo", "old", "new", "v1", "v2", "v3", "v4", "v5"]

print(f"--- Lancement du fuzzer sur {url_cible} ---")

# 2. La boucle de test
for mot in mots_a_tester:
    url_complete = url_cible + "/" + mot
    
    try:
        # On tente de se connecter à l'URL
        reponse = requests.get(url_complete, timeout=5)
        
        # Si le serveur répond 200, c'est que la page existe
        if reponse.status_code == 200:
            print(f"[+] TROUVÉ : {url_complete}")
        else:
            # On affiche quand même pour voir que ça travaille
            print(f"[-] Absent : {mot}")
            
    except requests.exceptions.RequestException:
        # Si le site ne répond pas du tout (erreur de connexion)
        print(f"[!] Erreur de connexion au serveur {url_cible}")
        break 