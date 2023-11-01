def hide_the_account_or_card(view: str, number: str) -> str:
    """
    принимает на вход строку информацией тип карты/счета и номер карты/счета
    возвращает эту строку с замаскированным номером карты/счета.
    """
    if view == 'счет' or view == 'Счет':
        return f"{view.title()} **{number[16:20]}"
    else:
        correct_number = number.replace(' ', '')
        return f"{view} {correct_number[:4]} {correct_number[4:6]}** **** {correct_number[12:16]}"


def converts_date(date: str) -> str:
    """
    принимает на вход строку, вида "2018-07-11T02:26:18.671407"
    и возвращает строку с датой в виде "11.07.2018"
    :param date:
    :return:
    """
    return f'{date[8:10]}.{date[5:7]}.{date[0:4]}'


print(hide_the_account_or_card('счет', '73654108430135874305'))
print(hide_the_account_or_card('Visa Platinum', '7000 7922 8960 6361'))
print(converts_date("2018-07-11T02:26:18.671407"))
