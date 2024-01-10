class Biostar2User:
    def __init__(self, **kwargs):
        """
            Pour initialiser les attributs d'un utilisateur Suprema, on utilise une boucle setattr.
            Pourquoi ?
                Il y a beaucoup de variables et cela prendrait beaucoup de lignes pour les initialiser.
            Comment connaître la liste des attributs ?
                Se référer à la documentation de BioStar2 et regarder le fichier json exemple. Tous les attribus de
                cette classe sont les entrées du dictionnaire User

            Lien vers la doc des utilisateurs Suprema
            https://bs2api.biostar2.com/#0b54ae8b-6744-44dd-8556-8001ae3139ff
        """
        self.session_id = kwargs.pop('session_id')
        data_user = kwargs.pop('user')
        for key, value in data_user.items():
            setattr(self, key, value)