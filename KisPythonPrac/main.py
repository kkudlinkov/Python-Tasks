'Реализуйте генератор Project(new_schema, parent_schema, parent), который выполняет операцию проекции.'
'Пример использования:'

def Project(new_schema, parent_schema, parent):
    for i in parent:
        yield {new_schema[j]: i[parent_schema[j]] for j in range(len(parent_schema))}


def Scan(filename):
    with open(filename) as f:
        s = f.readline()
        for line in f:
            yield line.split(', ')

'файл talks.csv включает в себя столбцы tid,time,title,room.'

'Вызов функции Project:'
for i in Project(['tid', 'title'], ['tid', 'title', 'room'], Scan('talks.csv')):
    print(i)
