
import sys
sys.path.insert(0, './models')

from hypothese import *
from system import *
from equation import *

hypotheses = [Hypothese('A'), Hypothese('B')]
eq1 = Equation(['A', 'B'], 'X')
eq2 = Equation(['D', 'E'], 'Z')
system = System([eq1,eq2])

print('## System : ')
print(system)
print('## Hypotheses : ')
print(hypotheses)
print('\n')
for h in hypotheses:
    for eq in system.eqs:
        if h.hyp in eq.premisse:
            eq.premisse.remove(h.hyp)
            if eq.is_premisse_empty():
                hypotheses.append(Hypothese(eq.conclusion))
print('## Result : ')
print('Hypotheses : ')
print(hypotheses)
print('System : ')
print(system)
