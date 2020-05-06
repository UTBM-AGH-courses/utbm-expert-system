class Equation:
    def __init__(self, name, premisse, conclusion):
        self.name = name
        self.premisse = premisse
        self.conclusion = conclusion

    def __str__(self):
        return self.name + ' : ' + str(self.premisse) + ' => ' + self.conclusion

    def isPremisseEmpty(self):
        return not self.premisse

class System:
    def __init__(self, eq):
        self.eq = eq

class Hypothese:
    def __init__(self, hyp):
        self.hyp = hyp

class Fact:
    def __init__(self, fact):
        self.fact = fact

    def __str__(self):
        return self.fact




facts = [Fact('A'), Fact('B')]
eq1 = Equation('eq1', ['A', 'B'], 'X')
eq2 = Equation('eq2', ['D', 'E'], 'Z')
system = System([eq1,eq2])

for f in facts:
    for eq in system.eq:
        if f.fact in eq.premisse:
            eq.premisse.remove(f.fact)
            if eq.isPremisseEmpty():
                facts.append(Fact(eq.conclusion))

print(facts)
