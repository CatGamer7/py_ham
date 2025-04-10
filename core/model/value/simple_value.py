from .base_value import Base_Value


class Simple_Value(Base_Value):

    value: int

    def __init__(self, in_value: int):
        self.value = in_value

    def __str__(self):
        return str(self.value)
    
    def __call__(self) -> int:
        return self.value

    def expected_value(self) -> float:
        return float(self.value)
    
    def get_value(self) -> int:
        return self.value
    