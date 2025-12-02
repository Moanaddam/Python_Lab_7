from datetime import datetime
from mixins import ValidationMixin, HistoriqueMixin, JournalisationMixin

class Tache(ValidationMixin, HistoriqueMixin, JournalisationMixin):
    def __init__(self, titre, description):
        self.valider_titre(titre)
        self.titre = titre
        self.description = description
        self.date_creation = datetime.now()
        
        self.journaliser(f"Création de la tâche '{self.titre}'")

    def mettre_a_jour(self, nouvelle_description):
        self.sauvegarder_etat(self.description)
        self.description = nouvelle_description
        self.journaliser("Mise à jour de la description")

if __name__ == "__main__":
    try:
        tache = Tache("Rédiger le rapport", "Version brouillon")
        
        print(f"Description actuelle : {tache.description}")
        
        tache.mettre_a_jour("Version finale corrigée")
        print(f"Description après maj : {tache.description}")
        
        tache.mettre_a_jour("Version finale validée par le manager")
        
        tache.afficher_historique()

        tache_erreur = Tache("", "Description")

    except ValueError as e:
        print(f"\nErreur détectée : {e}")