from mixins import Serializable, Historisable, Journalisable, Horodatable, Exportable

class Contrat(Serializable, Historisable, Journalisable, Horodatable, Exportable):
    def __init__(self, id, description):
        Historisable.__init__(self)
        Horodatable.__init__(self)
        self.id = id
        self.description = description

    def modifier(self, nouvelle_desc):
        self.journaliser(f"Modification du contrat {self.id}")
        self.enregistrer_etat()
        self.description = nouvelle_desc
        self.mettre_a_jour_timestamp()

class Client(Serializable, Historisable, Journalisable, Horodatable, Exportable):
    def __init__(self, nom, email):
        Historisable.__init__(self)
        Horodatable.__init__(self)
        self.nom = nom
        self.email = email

    def changer_email(self, nouvel_email):
        self.journaliser(f"Changement email client {self.nom}")
        self.enregistrer_etat()
        self.email = nouvel_email
        self.mettre_a_jour_timestamp()

if __name__ == "__main__":
    print("--- Test Classe Contrat ---")
    c = Contrat(1, "Initial")
    c.modifier("Révisé")
    
    print(f"JSON: {c.to_json()}")
    print(f"CSV:  {c.to_csv()}")
    print(f"XML:  {c.to_xml()}")

    print("\n--- Test Classe Client ---")
    cl = Client("Alice", "alice@test.com")
    cl.changer_email("alice.new@test.com")
    
    print(f"JSON: {cl.to_json()}")
    print(f"Historique: {cl.historique}")