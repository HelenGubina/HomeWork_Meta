class LoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        try:
            for i in attrs:
                ind_name = i.find(f"_{name}")
                if ind_name >= 0:
                    name_atr = i[len(name)+1:len(i)]
                    if len(name_atr) > 2 and name_atr[0:2] == "__":
                        raise NameError
        except NameError:
            print("Cannot have attribute names starting with  __")
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=LoggingMeta):
    __cls_attr1 = "atr"
