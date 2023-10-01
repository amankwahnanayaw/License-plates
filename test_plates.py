import pytest
from plates import is_valid


def main():
    test_is_vailid()


def test_is_vailid():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid("PI3 14") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False



if __name__ == "__main__":
    main()
