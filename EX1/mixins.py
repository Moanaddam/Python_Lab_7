import json
from datetime import datetime
from abc import ABC, abstractmethod

class Horodatable:
    def obtenir_horodatage(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Validable:
    def valider(self):
        if not getattr(self, "titre", None):
            raise ValueError("Erreur de validation : Le titre est manquant.")
        print("Validation OK")

class Historisable:
    def archiver_action(self, action):
        if not hasattr(self, '_historique'):
            self._historique = []
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entree = f"[{timestamp}] {action}"
        self._historique.append(entree)
    
    def afficher_historique(self):
        print(f"--- Historique de '{getattr(self, 'titre', 'Inconnu')}' ---")
        if hasattr(self, '_historique'):
            for ligne in self._historique:
                print(ligne)
        else:
            print("Aucun historique.")

class Serializable(ABC):
    @abstractmethod
    def data_dict(self):
        pass

    def to_json(self):
        return json.dumps(self.data_dict(), indent=4, ensure_ascii=False)