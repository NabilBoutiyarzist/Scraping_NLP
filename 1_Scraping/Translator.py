import requests 

class Translator :
    """
    Classe definissant une fonction permettant la traduction de texte via l'API Deepl
    """
    def __init__(self):
       pass
        
    def traduction(self,text):
        AUTH_KEY = "8864b9f3-3698-e71f-09dc-423e0a7923e0:fx"
         # Langue cible
        TARGET_LANG = "FR"
         # En-tête d'autorisation
        headers = {
           "Authorization": f"DeepL-Auth-Key {AUTH_KEY}"
        }
         # Données à envoyer
        data = {
           "text": text,
           "target_lang": TARGET_LANG
           }
         # Envoi de la requête POST
        response = requests.post("https://api-free.deepl.com/v2/translate", headers=headers, data=data)
        # Vérification du code de réponse HTTP
        if response.status_code == 200:
           translations = response.json()["translations"]
           translated_text = translations[0]["text"]
           print(translated_text)
        else:
        # Une erreur est survenue
           print(f"Erreur lors de la traduction : {response.status_code}")
           
         
    
