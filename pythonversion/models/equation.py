class Equation:
    def __init__(self, premisse, conclusion):
        self.__premisse = premisse
        self.__conclusion = conclusion

    def get_premisse(self):
        return self.__premisse

    def get_conclusion(self):
        return self.__conclusion
    

    def is_premisse_empty(self):
        return not self.__premisse

    def __str__(self):
        return  '^'.join(map(str, self.__premisse)) + ' => ' + self.__conclusion
