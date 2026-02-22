from app.main import get_human_age


def test_should_return_zeros_when_ages_are_below_fifteen() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_year_at_fifteen() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_years_at_twenty_four() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_cat_and_dog_years_diverge_after_twenty_four() -> None:
    # Kot: 28 lat -> 24 (2 lata) + 4 (1 rok) = 3 lata
    # Pies: 28 lat -> 24 (2 lata) + 4 (wciąż w progu do 29) = 2 lata
    assert get_human_age(28, 28) == [3, 2]


def test_should_calculate_high_ages_correctly() -> None:
    assert get_human_age(100, 100) == [21, 17]
