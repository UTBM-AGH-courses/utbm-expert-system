# Import modules
from models.hypothese import Hypothese
from models.system import System
from models.equation import Equation
from file_processor.hypothese_file_processor import HypotheseFileProcessor
from file_processor.system_file_processor import SystemFileProcessor

# Open the hypotheses file
hypotheseIO = HypotheseFileProcessor("hypotheses.txt")
# Get the hypotheses
hypotheses = hypotheseIO.get_hypotheses()

# Open the system file
systemIO = SystemFileProcessor("system.txt")
# Get the system
system = systemIO.get_system()

# Core logic
for h in hypotheses:
    for eq in system.get_system():
        if h.get_hypothese() in eq.get_premises():
            eq.mark_premise(h.get_hypothese())
            if eq.are_premises_marked():
                hypotheses.append(Hypothese(eq.get_conclusion()))
                eq.mark_conclusion()

# Display result
print('######## Results ######## ')
print()
print('### System ###')
print(system)
print('### True elements ###')
print(hypotheses)
