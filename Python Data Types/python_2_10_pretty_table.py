NUMBERS_INDENT = 2


def main():
    tuple1 = (2, 13)
    tuple2 = (8, 10)
    r = pretty_mul_table(tuple1, tuple2)
    print(r)


def pretty_mul_table(value_x: tuple, value_y: tuple) -> str:
    extended_x = []
    extended_y = []
    for x in range(value_x[0], value_x[1] + 1):
        extended_x.append(x)
    for y in range(value_y[0], value_y[1] + 1):
        extended_y.append(y)
    d = mul_table_as_dict(extended_x, extended_y)
    return pretty_print(d, extended_x, extended_y)


def mul_table_as_dict(value_x: list, value_y: list) -> dict:
    table = {}
    for x in value_x:
        table[x] = list(map(lambda y, value=x: y * value, value_y))
    return table


def pretty_print(table: dict, value_x: list, value_y: list) -> str:
    max_len_x = len(str(max(list(value_x))))
    max_len_y = get_max_list_value_len(list(table.values()))

    head_list = list(map(lambda s: format_value(s, max_len_y), value_y))
    head_list.insert(0, ' ' * (max_len_x + NUMBERS_INDENT))
    head = ''.join(head_list)

    body_list = []
    body = ''
    for key_x in table.keys():
        body_list_item = list(map(lambda v: format_value(v, max_len_y), table.get(key_x)))
        body_list_item.insert(0, format_value(key_x, max_len_x))
        body_list.append(''.join(body_list_item))
    body += ('\n').join(body_list)
    return '{0}\n{1}'.format(head, body)


def format_value(value: int, max_value_len: int) -> str:
    svalue = str(value)
    return svalue + ' ' * ((max_value_len - len(svalue)) + NUMBERS_INDENT)


def get_max_list_value_len(list_of_int: list) -> int:
    max_y_list = []
    for row_list in list_of_int:
        row_list_len = list(map(lambda x: len(str(x)), row_list))
        max_y_list.append(max(row_list_len))
    return max(max_y_list)


if __name__ == '__main__':
    main()
