def Join(left, right):
    # находим индекс общего столбца
    left_header = next(left)
    right_header = next(right)
    # формируем новый заголовок таблицы
    new_header = left_header + right_header[1:]
    yield new_header
    # проходимся по строкам таблицы left и ищем соответствующие строки из таблицы right
    for left_row in left:
        for right_row in right:
            right_key = right_row[0]
            yield left_row + right_row[1:]
            break