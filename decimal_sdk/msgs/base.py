class BaseMsg:
    type: str

    def get_value(self):
        return self.__dict__()["value"]

    def get_type(self):
        return self.type
