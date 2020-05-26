# Common logic of a Conclusion and a Premisse
class EquationElement:
    # ctor
    def __init__(self, value):
        self.__value = value
        self.__is_mark = False

    # Mark an element as true
    def mark(self):
        self.__is_mark = not self.__is_mark

    # Check if an element is marked
    def is_mark(self):
        return self.__is_mark
    
    # Get the value to string
    def get_value(self):
        return self.__value

    # Print the value (ex: A or -A- if it's marked)
    def __str__(self):
        if (self.__is_mark):
            return '-' + self.__value + '-'
        else:
            return self.__value