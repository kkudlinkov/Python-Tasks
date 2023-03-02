#   E211    #
with open ('file') as f:
    txt = f.read()

for i in range (1, 1000):
    pass

#   E225    #
age = 10
if age>15:
    print("Hello")

#   E231    #
world = 1,2,3


#   E251    #
def func(key1 = 'val1', key2 = 'val2'):
    return key1, key2

#   E302    #
def func1():
    pass


#   E701    #
if 10 > 5: x = 10

#   E702    #
#Несколько инструкций не должны находиться в одной строке, разделенные точкой с запятой.
#Они должны быть на своих собственных отдельных линиях
#from gevent import monkey; monkey.patch.all()

#   E711 and E712    #
#Сравнения с одноэлементными объектами, такими как True, False и None, должны выполняться с использованием идентификатора,
#а не равенства. Используйте “есть” или “не является”
var = True
if var != True:
    print("var is not equal to True")
if var == None:
    print("var is equal to None")
