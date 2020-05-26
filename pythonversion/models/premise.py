from .equation_element import EquationElement

# Premise of an equation (ex: A is one of the premises of A^B=>C)
class Premise(EquationElement):
    def __init__(self, prem):
        super().__init__(prem)