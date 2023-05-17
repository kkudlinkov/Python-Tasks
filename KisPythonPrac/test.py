def Value(x):
    return x

def Project(new_schema, parent_schema, parent):
    # Создается список индексов столбцов в parent, которые соответствуют именам столбцов в new_schema
    indices = [parent_schema.index(col) for col in new_schema]
    for row in parent:
        yield [row[i] for i in indices]


def Scan(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip().split(',')


def Print(parent):
    for row in parent:
        print(row)


def Eq(x, y):
    return lambda row: row[x] == y


def Ne(x, y):
    return lambda row: row[x] != y


def Filter(pred, parent):
    for row in parent:
        if pred(row):
            yield row


if __name__ == '__main__':
    # select room, title from talks.csv where time='09:00 AM'
    filename = 'talks.csv'
    pred = Eq(1, '09:00 AM')
    filtered = Filter(pred, filename)
    result = Project(['room', 'title'], ['time', 'room', 'speaker', 'title'], Filter(Eq(1, '09:00 AM'), Scan('talks.csv')))
    Print(result)

