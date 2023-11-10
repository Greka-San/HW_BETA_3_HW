from src.masks import hides_card_number, hides_account_number


def test_hides_card_number():
    assert hides_card_number("7000792289606361") == "7000 79** **** 6361"


def test_hides_account_number():
    assert hides_account_number("73654108430135874305") == "**4305"
