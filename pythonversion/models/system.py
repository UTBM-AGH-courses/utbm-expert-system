class System:
    def __init__(self, eqs):
        self.eqs = eqs

    def __str__(self):
        str_eq = ""
        for eq in self.eqs:
            str_eq += "|" + str(eq) + '\n'
        return str_eq