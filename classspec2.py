# -*- coding: UTF-8 -*-
class First(object):
    def __init__(self, name):
        print(name)

class Two(First):
    def __init__(self, parent, name):
        First.__init__(self, parent)
        print(name)


first = First('Это класс First')
two = Two('Это класс Two', 'А это инициализируем First из Two')