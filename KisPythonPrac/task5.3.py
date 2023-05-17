def Eq(x, y):
    return lambda row: row[x] == y

def Ne(x, y):
    return lambda row: row[x] != y

def Value(x):
    return x

def Field(x):
    return lambda row: row[x]

def Filter(pred):
    return 0

def Scan(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip().split(',')


def Project(new_schema, parent_schema, parent):
    indices = [parent_schema.index(col) for col in new_schema]
    for row in parent:
        yield [row[i] for i in indices]


Filter(Eq(Field('time'), Value('09:00 AM')), Scan('talks.csv'))
def Print(parent):
    for row in parent:
        print(row)


Print(Filter(Eq(Field('time'), Value('09:00 AM')), Scan('talks.csv')))
