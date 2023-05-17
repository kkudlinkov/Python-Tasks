def Scan(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip().split(',')
def Print(parent):
    for row in parent:
        print(row)

Print(Scan('talks.csv'))