from src.widget import hide_the_account_or_card, converts_date


def test_hide_the_account_or_card():
    assert hide_the_account_or_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_converts_date():
    assert converts_date("2018-07-11T02:26:18.671407") == "11.07.2018"
