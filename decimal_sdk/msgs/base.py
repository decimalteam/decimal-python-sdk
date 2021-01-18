class BaseMsg:
    type: str
    value: object

    def get_value(self):
        return self.type
