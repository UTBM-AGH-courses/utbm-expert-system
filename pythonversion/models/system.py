class System:
    def __init__(self, eqs):
        self.__eqs = eqs

    def get_system(self):
        return self.__eqs

    def __str__(self):
        str_eq = ""
        for eq in self.__eqs:
            str_eq += "|" + str(eq) + '\n'
        return str_eq