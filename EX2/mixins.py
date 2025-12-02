import json
from datetime import datetime

class Serializable:
    def to_json(self):
        return json.dumps(self.__dict__, default=str)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

class Historisable:
    def __init__(self):
        self.historique = []

    def enregistrer_etat(self):
        if not hasattr(self, 'historique'):
            self.historique = []
        etat_copie = self.__dict__.copy()
        if 'historique' in etat_copie:
            del etat_copie['historique']
        self.historique.append((str(datetime.now()), etat_copie))

class Journalisable:
    def journaliser(self, message):
        print(f"[Journal] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {message}")

class Horodatable:
    def __init__(self):
        self.date_derniere_maj = str(datetime.now())

    def mettre_a_jour_timestamp(self):
        self.date_derniere_maj = str(datetime.now())

class Exportable:
    def to_csv(self):
        valeurs = [str(v) for k, v in self.__dict__.items() if k != 'historique']
        return ",".join(valeurs)

    def to_xml(self):
        xml_str = "<objet>"
        for k, v in self.__dict__.items():
            if k != 'historique':
                xml_str += f"<{k}>{v}</{k}>"
        xml_str += "</objet>"
        return xml_str