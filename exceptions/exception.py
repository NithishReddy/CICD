class InvalidInput(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.message = kwargs.get("message")
    
    def __str__(self):
        return self.message
    
class DivisionByZero(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.message = kwargs.get("message")
    
    def __str__(self):
        return self.message