def main(table):
    non_empty_columns = [list(filter(lambda x: x is not None, row)
                              ) for row in table]
    unique_rows = []
    for row in non_empty_columns:
        if row not in unique_rows:
            unique_rows.append(row)
    for row in unique_rows:
        row[0] = row[0].split(';')
    for row in unique_rows:
        row[2] = 'Да' if row[1] == 'true' and row[2] == 'true' else 'Нет'
        row[1] = format(float(row[0][0]), '.4f')
        row[0] = '/'.join(row[0][1].split('.')[::-1])
    return unique_rows


# Пример использования
# input_table = [
#     ['0.7;99.12.11', None, 'true', 'true'],
#     ['1.0;00.01.07', None, 'false', 'false'],
#     ['0.4;04.12.28', None, 'false', 'false'],
# ]

input_table = [
    ['0.7;01.07.14', None, 'false', 'false'],
    ['0.8;01.07.17', None, 'true', 'true'],
    ['0.3;01.12.26', None, 'true', 'true'],
]

print(main(input_table))
