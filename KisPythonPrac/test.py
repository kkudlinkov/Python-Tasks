def Join(left, right):
    # находим индекс общего столбца
    left_header = next(left)
    right_header = next(right)
    common_col = left_header.index('tid')  # здесь tid - имя общего столбца
    # формируем новый заголовок таблицы
    new_header = left_header + right_header[1:]
    yield new_header
    # проходимся по строкам таблицы left и ищем соответствующие строки из таблицы right
    for left_row in left:
        left_key = left_row[common_col]
        for right_row in right:
            right_key = right_row[0]
            yield left_row + right_row[1:]
            break


def Project(new_schema, parent_schema, parent):
    # Создается список индексов столбцов в parent, которые соответствуют именам столбцов в new_schema
    indices = [parent_schema.index(col) for col in new_schema]
    for row in parent:
        yield [row[i] for i in indices]


def Print(parent):
    for row in parent:
        print(row)


def Scan(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip().split(',')


Print(Join(Project(['tid', 'title'], ['tid', 'time', 'title', 'room'], Scan('talks.csv')),
           Project(['tid', 'time', 'room'], ['tid', 'time', 'title', 'room'], Scan('talks.csv'))))
