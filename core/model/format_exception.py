class Format_Exception(AttributeError):
    token = str

    def __init__(self, token: str, reason: str, *args, name = ..., obj = ...):
        super().__init__(*args, name=name, obj=obj)
