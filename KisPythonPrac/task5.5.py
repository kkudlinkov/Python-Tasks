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
    left_fields = next(left)
    right_fields = next(right)
    # Объединяем поля из левой и правой таблиц
    join_fields = left_fields + [field for field in right_fields if field not in left_fields]
    yield join_fields
    # Проходимся по строкам из левой таблицы
    for left_row in left:
        # Проходимся по строкам из правой таблицы
        for right_row in right:
            # Проверяем условие соединения
            if all(left_row[left_fields.index(field)] == right_row[right_fields.index(field)]
                   for field in left_fields):
                # Если условие выполняется, объединяем строки из левой и правой таблиц
                join_row = left_row + [right_row[right_fields.index(field)] for field in right_fields
                                       if field not in left_fields]
                yield join_row


Print(Filter(Ne(Field('title1'), Field('title2')),
             Join(Project(['time', 'room', 'title1'], ['time', 'room', 'title'], Scan('talks.csv')),
                  Project(['time', 'room', 'title2'], ['time', 'room', 'title'], Scan('talks.csv')))))
