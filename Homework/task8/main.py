import re


def main(data):
    data = data.replace(' ', '').replace('\n', '')
    answer = dict()  # Словарь
    pattern = r"<data>global`(\w+)\|>@'(\w*)';"
    find_result = re.findall(pattern, data)
    for elem in find_result:
        answer.update({elem[1]: elem[0]})
    return answer


print(main(
    "[[ <data> global `biveve|>@'onxe_176'; </data>; <data> global `teon |>@'rive_778'; </data>;<data>global `rabe |> @'erus_519'; </data>; ]]"))
