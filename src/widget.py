from src.masks import hides_card_number, hides_account_number


def hide_the_account_or_card(account_or_card: str) -> str:
    """
    принимает на вход строку с информацией тип карты/счета и номер карты/счета
    возвращает эту строку с замаскированным номером карты/счета.
    """
    name_of_account = account_or_card.split()
    if name_of_account[0] == 'счет' or name_of_account[0] == 'Счет':
        number = hides_account_number(name_of_account[1])
        return f'{name_of_account[0]} {number}'
    else:
        number = hides_card_number(name_of_account[len(name_of_account)-1])
        name_of_card = ' '.join(name_of_account[:len(name_of_account)-1])
        return f'{name_of_card} {number}'


def converts_date(date: str) -> str:
    """
    Функция переформатирует дату
    :param date: Дата для изменения
    :return: Отформатированная дата
    """
    return f'{date[8:10]}.{date[5:7]}.{date[0:4]}'
