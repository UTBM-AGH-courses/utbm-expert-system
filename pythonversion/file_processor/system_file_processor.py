import re
from .file_processor import FileProcessor
from models.equation import Equation
from models.system import System
from models.conclusion import Conclusion
from models.premise import Premise

class SystemFileProcessor(FileProcessor):
    # Retourne le système étudié (public)
    def get_system(self):
        return System(list(map(SystemFileProcessor.__instance, re.split("\s", self.get_stream().read()))))

    # Instancie les prémisses (private)
    def __premise_instance(p):
        return Premise(p)

    # Instancie une équation du système (private)
    def __instance(e):
        conclusion = re.split("=>", e)[-1]
        premises = list(map(SystemFileProcessor.__premise_instance, re.split("\^", re.split("=>", e)[0])))
        return Equation(premises, Conclusion(conclusion))
