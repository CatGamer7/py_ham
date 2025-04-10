from .simple_value import Simple_Value


class Non_Positive_Value(Simple_Value):

    def __init__(self, in_value: int):
        if in_value > 0:
            raise AttributeError("expected non-positive integer")
        
        super().__init__(in_value)
