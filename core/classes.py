from dimanify import *

class класс:
    def __init__(self, class_name, base_class=None):
        if not isinstance(class_name, str):
            raise TypeError("Название класса должно быть строкой")
        self.class_name = class_name
        self.base_class = base_class
        self.attributes = {}

    def унаследовать(self, base_class):
        if not isinstance(base_class, type):
            raise TypeError("Наследуемый класс должен быть типом")
        self.base_class = base_class

    def добавить_атрибут(self, attribute_name, attribute_value):
        if not isinstance(attribute_name, str):
            raise TypeError("Название атрибута должно быть строкой")
        self.attributes[attribute_name] = attribute_value

    def создать(self):
        if self.base_class is None:
            new_class = type(self.class_name, (), self.attributes)
        else:
            if not issubclass(self.base_class, object):
                raise TypeError("Нельзя наследоваться от класса, не являющегося объектом")
            new_class = type(self.class_name, (self.base_class,), self.attributes)
        return new_class
