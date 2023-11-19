import requests 
import time
import json
import pandas

class ExtractUrlArticle :
    
    
    """
    Classe définissant différentes fonctions permettant l'extraction d'articles de presse dans différents pays en lien 
    avec le bombardement de l'hôpital Al Haly dans la bande de Gaza. 
    
    Utilisation de l'API NewsAPI (free account).
    
    """
    
    #NEWS_API_KEY = '466865b857ab4cffbc850e21bb4ccdfc'
    
    def __init__(self):
        pass
        
    
    #*****************************************************
    # Articles Français 
    #*****************************************************
        
    def ExtractArticleFr(self):
        """
        Extrait des urls d'articles en français liés aux mots clés "Israël Hôpital" sur une plage de dates spécifiée.
        Cette fonction effectue une requête à l'API News pour récupérer des articles en français
        qui mentionnent "Israël Hôpital" sur une plage de dates donnée, puis elle filtre les
        articles pour ne conserver que ceux contenant ces termes dans leur titre. 
        Args:
            Aucun argument nécessaire. Les paramètres de la requête sont définis à l'intérieur
            de la fonction.
        Returns:
            La liste des urls d'articles filtrés .
        """
        # Paramètres de la requête
        from_date = "2023-10-17"
        to_date = "2023-10-20"
        q = "Israël Hôpital"
        language = "fr"
        
        # Construction de l'URL
        url = (
            "https://newsapi.org/v2/everything?q={}&from={}&to={}&language={}&sortBy=popularity&apiKey=466865b857ab4cffbc850e21bb4ccdfc"
        ).format(q, from_date, to_date, language)
        
        # Récupération de la réponse
        response = requests.get(url)
        
        # Traitement de la réponse
        articles = response.json()["articles"]
        
        # Filtrage des articles
        filtered_articles = []
        for article in articles:
            if "Israël" in article["title"] and "hôpital" in article["title"]:
                filtered_articles.append(article)
        
        return pandas.DataFrame(filtered_articles)
            
    
    #*****************************************************
    # Articles Allemand 
    #*****************************************************        
    def ExtractArticleDe(self):
        """
        Extrait des URLs d'articles en allemand liés aux mots clés "Israel Krankenhaus" sur une plage de dates spécifiée.
    
        Cette fonction effectue une requête à l'API News pour récupérer des articles en allemand
        qui mentionnent "Israel Krankenhaus" sur une plage de dates donnée, puis elle filtre les
        articles pour ne conserver que ceux contenant ces termes dans leur titre. Les URLs des articles
        filtrés sont renvoyées sous forme de liste.
    
        Args:
            Aucun argument nécessaire. Les paramètres de la requête sont définis à l'intérieur
            de la fonction.
    
        Returns:
            Une liste d'URLs d'articles filtrés en allemand.
    
        """
        # Paramètres de la requête
        from_date = "2023-10-17"
        to_date = "2023-10-20"
        q = "Israel Krankenhaus"
        language = "de"
        
        # Construction de l'URL
        url = (
            "https://newsapi.org/v2/everything?q={}&from={}&to={}&language={}&sortBy=popularity&apiKey=466865b857ab4cffbc850e21bb4ccdfc"
        ).format(q, from_date, to_date, language)
        
        # Récupération de la réponse
        response = requests.get(url)
        
        # Traitement de la réponse
        articles = response.json()["articles"]
        
        # Filtrage des articles
        filtered_articles = []
        for article in articles:
            if "Israel" in article["title"] and "Krankenhaus" in article["title"]:
                filtered_articles.append(article)
        
        return filtered_articles
                
    #*****************************************************
    # Articles Anglais 
    #*****************************************************             
    def ExtractArticleEn(self):
        """
        Extrait des URLs d'articles en anglaus liés aux mots clés "Israel Hospital" sur une plage de dates spécifiée.
    
        Cette fonction effectue une requête à l'API News pour récupérer des articles en anglais
        qui mentionnent "Israel Hospital" sur une plage de dates donnée, puis elle filtre les
        articles pour ne conserver que ceux contenant ces termes dans leur titre. Les URLs des articles
        filtrés sont renvoyées sous forme de liste.
    
        Args:
            Aucun argument nécessaire. Les paramètres de la requête sont définis à l'intérieur
            de la fonction.
    
        Returns:
            Une liste d'URLs d'articles filtrés en anglais.
    
        """
        # Paramètres de la requête
        from_date = "2023-10-17"
        to_date = "2023-10-20"
        q = "Israel Hospital"
        language = "en"
        
        # Construction de l'URL
        url = (
            "https://newsapi.org/v2/everything?q={}&from={}&to={}&language={}&sortBy=popularity&apiKey=466865b857ab4cffbc850e21bb4ccdfc"
        ).format(q, from_date, to_date, language)
        
        # Récupération de la réponse
        response = requests.get(url)
        
        # Traitement de la réponse
        articles = response.json()["articles"]
        
        # Filtrage des articles
        filtered_articles = []
        for article in articles:
             if "aljazeera" not in article["url"] :
                 filtered_articles.append(article)
        return filtered_articles
    
    #*****************************************************
    # Articles Iranien 
    #*****************************************************  
    def ExtractArticleFa(self):
        """
        Extrait des URLs d'articles en Iranien liés aux mots clés "اسرائیل بیمارستان" signifiant "Israel" et "Hopital" 
        sur une plage de dates spécifiée.
    
        Cette fonction effectue une requête à l'API News pour récupérer des articles en Iranien
        qui mentionnent "اسرائیل بیمارستان" sur une plage de dates donnée, puis elle filtre les
        articles pour ne conserver que ceux contenant ces termes dans leur titre. Les URLs des articles
        filtrés sont renvoyées sous forme de liste.
    
        Args:
            Aucun argument nécessaire. Les paramètres de la requête sont définis à l'intérieur
            de la fonction.
    
        Returns:
            Une liste d'URLs d'articles filtrés en Iranien.
    
        """
        # Paramètres de la requête
        from_date = "2023-10-17"
        to_date = "2023-10-20"
        q = "اسرائیل بیمارستان"
        language = "fa"
        
        # Construction de l'URL
        url = (
            "https://newsapi.org/v2/everything?q={}&from={}&to={}&language={}&sortBy=popularity&apiKey=466865b857ab4cffbc850e21bb4ccdfc"
        ).format(q, from_date, to_date, language)
        
        # Récupération de la réponse
        response = requests.get(url)
        
        # Traitement de la réponse
        articles = response.json()["articles"]
        
        # Filtrage des articles
        filtered_articles = []
        for article in articles:
            if "اسرائیل" in article["title"] and "بیمارستان" in article["title"]:
                filtered_articles.append(article)
        
        return filtered_articles
    
    #*****************************************************
    # Articles Arabie Saoudite 
    #*****************************************************         
    def ExtractArticleAr(self):
        """
        Extrait des URLs d'articles en Arabie Saoudite liés aux mots clés "إسرائيل مستشفى" signifiant "Israel" et "Hopital" 
        sur une plage de dates spécifiée.
    
        Cette fonction effectue une requête à l'API News pour récupérer des articles en Arabie Saoudite
        qui mentionnent "إسرائيل مستشفى" sur une plage de dates donnée, puis elle filtre les
        articles pour ne conserver que ceux contenant ces termes dans leur titre. Les URLs des articles
        filtrés sont renvoyées sous forme de liste.
    
        Args:
            Aucun argument nécessaire. Les paramètres de la requête sont définis à l'intérieur
            de la fonction.
    
        Returns:
            Une liste d'URLs d'articles filtrés en Arabie Saoudite.
    
        """
        # Paramètres de la requête
        from_date = "2023-10-17"
        to_date = "2023-10-20"
        q = "إسرائيل مستشفى"
        language = "ar"
        
        # Construction de l'URL
        url = (
            "https://newsapi.org/v2/everything?q={}&from={}&to={}&language={}&sortBy=popularity&apiKey=466865b857ab4cffbc850e21bb4ccdfc"
        ).format(q, from_date, to_date, language)
        
        # Récupération de la réponse
        response = requests.get(url)
        
        # Traitement de la réponse
        articles = response.json()["articles"]
        
        # Filtrage des articles
        filtered_articles = []
        for article in articles:
            if "إسرائيل" in article["title"] and "مستشفى" in article["title"]:
                filtered_articles.append(article)
        
        return filtered_articles
    
