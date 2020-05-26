import re
from .file_processor import FileProcessor
from models.hypothese import Hypothese

class HypotheseFileProcessor(FileProcessor):
    # Retourne un tableau contenant l'ensemble des hypothèses (public)
    def get_hypotheses(self):
        return list(map(HypotheseFileProcessor.__instance, re.split(",", self.get_stream().read())))

    # Instancie l'hypothèse (private)
    def __instance(h):
        return Hypothese(h)
