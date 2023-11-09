class LoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"{name}  has been created ")
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=LoggingMeta):
    pass
