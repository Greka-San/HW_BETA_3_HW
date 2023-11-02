from masks import hides_card_number, hides_account_number


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
    принимает на вход строку, вида "2018-07-11T02:26:18.671407"
    и возвращает строку с датой в виде "11.07.2018"
    :param date:
    :return:
    """
    return f'{date[8:10]}.{date[5:7]}.{date[0:4]}'


print(hide_the_account_or_card("Maestro Platinum Visa Classic Gold 1596837868705199"))
print(hide_the_account_or_card("Maestro 1596837868705199"))
print(hide_the_account_or_card("Счет 64686473678894779589"))
print(hide_the_account_or_card("Visa Classic 6831982476737658"))
print(converts_date("2018-07-11T02:26:18.671407"))
