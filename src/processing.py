dicts_for_tests = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 615061191, 'state': 'CANCELED', 'date': '2011-10-14T08:21:33.419441'}
]


def necessary_dictionaries(date: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Принимает список словарей и возвращает список словарей с ключом state
    :param date: список словарей
    :param state: ключ для сортировки
    :return: список словарей, у которых ключ state содержит значение
    """
    correct_dict = []
    for status in date:
        if status['state'] == state:
            correct_dict.append(status)
    return correct_dict


def sorts_the_list_by_date(date: list[dict], reverse: bool = False) -> list[dict]:
    """
    принимаетсписок словарей и возвращает новый список, в котором
    исходные словари отсортированы по убыванию даты/по возрастанию
    :param date: список словарей
    :param reverse: прямой/обратный порядок
    :return: список словарей
    """
    if reverse:
        return sorted(date, key=lambda x: x['date'], reverse=True)
    return sorted(date, key=lambda x: x['date'])


# print(necessary_dictionaries(dicts_for_tests))
# print(sorts_the_list_by_date(dicts_for_tests, True))
