class CamelCase(type):
    def __new__(cls, name, bases, attrs):
        try:
            if name[0].lower() == name[0]:
                raise NameError
        except NameError:
            print("Class name not in CamelCase")
        return super().__new__(cls, name, bases, attrs)


class myClass(metaclass=CamelCase):
    pass
