import pytest
from src.processing import dicts_for_tests, sorts_the_list_by_date, necessary_dictionaries


@pytest.fixture()
def import_from_processing():
    processing_for_test = dicts_for_tests
    return processing_for_test


@pytest.mark.parametrize('state, expected', [
    ('EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
                  ]),
    ('CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                  {'id': 615061191, 'state': 'CANCELED', 'date': '2011-10-14T08:21:33.419441'}])
])
def test_necessary_dictionaries(import_from_processing, state, expected):
    assert necessary_dictionaries(import_from_processing, state) == expected


@pytest.mark.parametrize('reverse, expected', [
    (False, [{'id': 615061191, 'state': 'CANCELED', 'date': '2011-10-14T08:21:33.419441'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
             ]),
    (True, [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 615061191, 'state': 'CANCELED', 'date': '2011-10-14T08:21:33.419441'}])
])
def test_sorts_the_list_by_date(import_from_processing, reverse, expected):
    assert sorts_the_list_by_date(import_from_processing, reverse) == expected
