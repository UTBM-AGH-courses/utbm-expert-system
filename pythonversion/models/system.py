# System of the exprt system
class System:
    # ctor
    def __init__(self, eqs):
        self.__eqs = eqs

    # Get the system
    def get_system(self):
        return self.__eqs

    # Display string
    def __str__(self):
        str_eq = ""
        for eq in self.__eqs:
            str_eq += "|" + str(eq) + '\n'
        return str_eq