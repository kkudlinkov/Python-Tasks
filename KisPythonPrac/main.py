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


def Join(left, right):
    # Find the index of the common column
    left_header = next(left)
    right_header = next(right)
    # Form a new header for the joined table
    new_header = left_header + right_header
    yield new_header
    # Iterate over the rows of the left table and find matching rows in the right table
    for left_row in left:
        for right_row in right:
            if left_row[common_column_index] == right_row[0]:
                yield left_row + right_row[1:]


Print(Filter(Ne(Field('title1'), Field('title2')),
             Join(Project(['time', 'room', 'title1'], ['time', 'room', 'title'], Scan('talks.csv')),
                  Project(['time', 'room', 'title2'], ['time', 'room', 'title'], Scan('talks.csv')))))
