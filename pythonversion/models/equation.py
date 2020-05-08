class Equation:
    def __init__(self, premisse, conclusion):
        self.premisse = premisse
        self.conclusion = conclusion

    def __str__(self):
        return str(self.premisse) + ' => ' + self.conclusion

    def is_premisse_empty(self):
        return not self.premisse
