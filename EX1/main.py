from mixins import Horodatable, Validable, Historisable, Serializable

class Document(Horodatable, Validable, Historisable, Serializable):
    def __init__(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu
        self.archiver_action("Création du document")

    def data_dict(self):
        return {
            "titre": self.titre,
            "contenu": self.contenu,
            "taille": len(self.contenu)
        }

    def sauvegarder(self):
        try:
            self.valider()
            ts = self.obtenir_horodatage()
            print(f"[LOG] Sauvegarde effectuée à {ts}")
            
            self.archiver_action("Sauvegarde effectuée")
            print(f"Document '{self.titre}' sauvegardé avec succès.")
            
        except ValueError as e:
            self.archiver_action(f"Échec sauvegarde : {e}")
            print(e)

if __name__ == "__main__":
    doc = Document("Rapport Annuel", "Ceci est le contenu du rapport financier.")

    doc.sauvegarder()
    
    print("\n--- Test de l'extension Serializable (JSON) ---")
    print(doc.to_json())

    print("\n--- Test de l'extension Historisable ---")
    doc.afficher_historique()