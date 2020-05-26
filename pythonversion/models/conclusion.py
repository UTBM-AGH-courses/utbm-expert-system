from .equation_element import EquationElement

# Conclusion of an equation (ex: C is the conclusion of A^B=>C)
class Conclusion(EquationElement):
    def __init__(self, conc):
        super().__init__(conc)