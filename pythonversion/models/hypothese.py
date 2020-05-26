# Hypothese of the expert system
class Hypothese:
    # ctor
    def __init__(self, hyp):
        self.__hyp = hyp

    # Get the string value of the hypothese
    def get_hypothese(self):
        return self.__hyp

    # Display string
    def __repr__(self):
        return self.__hyp
