# Equation of a System (coposed of an array of Premisse (premisse.py) and a Conclusion (conclusion.py))
class Equation:
    # ctor
    def __init__(self, premisses, conclusion):
        self.__premisses = premisses
        self.__conclusion = conclusion

    # Get the string array of premisses
    def get_premises(self):
        return list(map(str, self.__premisses))

    # Get the string value of the conclusion
    def get_conclusion(self):
        return str(self.__conclusion)

    # Mark the conclusion
    def mark_conclusion(self):
        self.__conclusion.mark()

    # Mark a premise according the prem_text
    def mark_premise(self, prem_text):
        for prem in self.__premisses:
            if prem.get_value() == prem_text:    
                prem.mark()
    
    # Return true if all premise are marked. 
    def are_premises_marked(self):
        prem_mark = 0
        for prem in self.__premisses:
            if prem.is_mark():
                prem_mark += 1
        return prem_mark == len(self.__premisses)

    # Display string
    def __repr__(self):
        return  ' ^ '.join(map(str, self.__premisses)) + ' => ' + str(self.__conclusion)
