def round_float(value, precision):
    """
    Округляет float значение до указанной точности без потери точности
    """
    decimal_part = str(value - int(value))[1:]  # находим десятичную часть числа
    precision = min(len(decimal_part),
                    precision)  # если нужно округлить до большего количества знаков, чем есть после запятой, то округляем до количества знаков после запятой
    rounded_decimal_part = str(round(float(decimal_part), precision))  # округляем десятичную часть числа
    if rounded_decimal_part == '1':  # если после округления получилось 1, то нужно увеличить целую часть на 1
        return str(int(value) + 1)
    return str(int(value)) + '.' + rounded_decimal_part  # иначе возвращаем число с округленной десятичной частью


def main(table):
    unique_rows = []
    for row in table:
        if row not in unique_rows:
            unique_rows.append(row)
    non_empty_rows = []
    for row in unique_rows:
        if any(cell is not None for cell in row):
            non_empty_rows.append(row)
    transformed_rows = []
    for row in non_empty_rows:
        date, value = row[1].split('!')
        rounded_value = round_float(value, 2)
        if rounded_value == 1.0:
            rounded_value = 1
        date_parts = date.split('.')
        transformed_date = f'{date_parts[2]}/{date_parts[1]}/{date_parts[0]}'
        if row[0] == 'true':
            status = 'Выполнено'
        else:
            status = 'Не выполнено'
        transformed_row = [status, transformed_date, str(rounded_value)]
        transformed_rows.append(transformed_row)
    return transformed_rows


# Пример использования
# input_table = [
#     ['true', '15.08.2001!0.856'],
#     ['false', '14.09.2000!0.194'],
#     ['false', '14.09.2000!0.194'],
#     ['false', '07.12.2001!0.218'],
#     [None, None],
#     ['false', '14.09.2000!0.194'],
#     ['true', '16.12.2004!0.614']
# ]

input_table = [['true', '03.05.2002!0.998'],
               [None, None],
               ['true', '04.04.2000!0.439'],
               [None, None],
               ['true', '03.05.2002!0.998'],
               ['true', '16.08.2002!0.605'],
               ['true', '03.05.2002!0.998'],
               ['true', '10.01.2003!0.782']]

# input_table = [['false', '24.09.2001!0.927'],
#                ['false', '18.11.2003!0.379'],
#                ['false', '18.11.2003!0.379'],
#                [None, None],
#                ['false', '08.09.2000!0.426'],
#                ['true', '27.01.2002!0.044'],
#                ['false', '18.11.2003!0.379']]
# i2 = [['true', '15.08.2001!0.856'], ['false', '14.09.2000!0.194'], ['false', '14.09.2000!0.194'], [None, None], ['false', '07.12.2001!0.218'], [None, None], ['false', '14.09.2000!0.194'], ['true', '16.12.2004!0.614']]

print(main(input_table))
