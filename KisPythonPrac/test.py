def Value(x):
    def execute(fields, row):
        return x
    return execute


def Field(name):
    def execute(fields, row):
        return row[fields.index(name)]
    return execute


def Eq(x, y):
    def execute(fields, row):
        return x(fields, row) == y(fields, row)
    return execute


def Ne(x, y):
    def execute(fields, row):
        return x(fields, row) != y(fields, row)
    return execute


def Filter(pred, parent):
    fields = next(parent)
    yield fields
    for row in parent:
        if pred(fields, row):
            yield row


def Project(new_schema, old_schema, parent):
    # Создается список индексов столбцов в parent, которые соответствуют именам столбцов в new_schema
    fields = next(parent)
    yield new_schema
    indices = [fields.index(col) for col in old_schema if col in fields]
    for row in parent:
        yield [row[i] for i in indices]


def Print(parent):
    for row in parent:
        print(row)


def Scan(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip().split(',')


Print(Project(['room', 'title'], ['room', 'title'],
        Filter(Eq(Field('time'), Value('09:00 AM')), Scan('talks.csv'))))
