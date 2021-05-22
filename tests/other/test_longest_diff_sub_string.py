import pytest
from loguru import logger

from other.find_longest_diff_sub_string import find_longest_diff_sub_string


@pytest.mark.parametrize("not_str", [None, True, 6, 7.0])
def test_bad_class_input(not_str):
    logger.debug(f"{not_str=}")
    assert find_longest_diff_sub_string(not_str) == ""


def test_empty():
    assert find_longest_diff_sub_string("") == ""


def test_whole():
    assert find_longest_diff_sub_string("abc") == "abc"


def test_begin():
    assert find_longest_diff_sub_string("abcdb") == "abcd"


def test_mid():
    assert find_longest_diff_sub_string("abcdaa") == "bcda"


def test_end():
    assert find_longest_diff_sub_string("abcdab") == "cdab"


def test_mult():
    assert find_longest_diff_sub_string("abcabdabmab") == "dabm"
