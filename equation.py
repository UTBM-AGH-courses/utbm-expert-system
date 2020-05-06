class Equation:
    def __init__(self, name, premisse, conclusion):
        self.name = name
        self.premisse = premisse
        self.conclusion = conclusion

    def __str__(self):
        return self.name + ' : ' + str(self.premisse) + ' => ' + self.conclusion

    def isPremisseEmpty(self):
        return not self.premisse
