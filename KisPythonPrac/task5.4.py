def Project(new_schema, parent_schema, parent):
    # Создается список индексов столбцов в parent, которые соответствуют именам столбцов в new_schema
    indices = [parent_schema.index(col) for col in new_schema]
    for row in parent:
        yield [row[i] for i in indices]

def Scan(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.split(',')

def Print(parent):
    for row in parent:
        print(row)

Print(Project(['tid', 'title'], ['tid', 'time', 'title', 'room'], Scan('talks.csv')))
