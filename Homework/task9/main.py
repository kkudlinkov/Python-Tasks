def main(table):
    non_empty_columns = [i for i in range(len(table[0]))
                         if any(row[i] for row in table)]
    unique_rows = []
    for row in [[row[i] for i in non_empty_columns] for row in table]:
        row[0] = 'Выполнено' if row[0] == 'да' else 'Не выполнено'
        row[1] = '-'.join(row[1].split('/')[::-1])
        row[2] = row[2][:-2]
        row[3] = row[3].split('@')[1]
        if row not in unique_rows:
            unique_rows.append(row)

    unique_rows.sort(key=lambda x: x[2] if x[2] else '')
    return list(map(list, zip(*unique_rows)))