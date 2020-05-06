from fact import *
from hypothese import *
from system import *
from equation import *

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
