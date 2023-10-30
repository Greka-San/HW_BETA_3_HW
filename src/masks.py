def hides_card_number(card_number: str) -> str:
    """возвращает маску карты"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:16]}"


def hides_account_number(account_number: str) -> str:
    """возвращает маску счета"""
    return f"**{account_number[16:20]}"


print(hides_card_number("7000792289606361"))
print(hides_account_number("73654108430135874305"))
