from datetime import datetime

class ValidationMixin:
    def valider_titre(self, titre):
        if not titre or not isinstance(titre, str) or not titre.strip():
            raise ValueError("Le titre est obligatoire et ne peut pas être vide.")

class HistoriqueMixin:
    def initialiser_historique(self):
        if not hasattr(self, 'historique'):
            self.historique = []

    def sauvegarder_etat(self, description_actuelle):
        self.initialiser_historique()
        entree = {
            "date": datetime.now(),
            "contenu": description_actuelle
        }
        self.historique.append(entree)

    def afficher_historique(self):
        self.initialiser_historique()
        print(f"--- Historique des modifications ---")
        for entree in self.historique:
            print(f"Date: {entree['date']} | Ancienne description: {entree['contenu']}")

class JournalisationMixin:
    def journaliser(self, action):
        print(f"[JOURNAL {datetime.now()}] Action: {action}")