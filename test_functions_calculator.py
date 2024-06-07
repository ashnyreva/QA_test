import functions_calculator
import pytest


def test_plus_positive_int():
    # assign
    a = 2
    b = 3

    # act
    s = functions_calculator.plus(a, b)

    # assert
    assert s == 5
    assert functions_calculator.plus(9, 2) == 11


def test_plus_positive_float():
    assert functions_calculator.plus(5.5, 13.5) == 19
    assert functions_calculator.plus(500.3, 13.1) == 513.4


def test_plus_negative_int():
    assert functions_calculator.plus(-10, -2) == -12
    assert functions_calculator.plus(-2, -1) == -3


def test_plus_negative_float():
    assert functions_calculator.plus(-10.5, -2.5) == -13
    assert functions_calculator.plus(-200.2, -123.7) == -323.9


def test_plus_mixed_int():
    assert functions_calculator.plus(-10, 2) == -8
    assert functions_calculator.plus(67, -1) == 66


def test_plus_mixed_float():
    assert functions_calculator.plus(-10.5, 2.5) == -8
    assert functions_calculator.plus(67.1, -1.6) == 65.5


def test_plus_zero_int():
    assert functions_calculator.plus(-10, 0) == -10
    assert functions_calculator.plus(0, -1) == -1
    assert functions_calculator.plus(0, 0) == 0
    assert functions_calculator.plus(0, 10) == 10
    assert functions_calculator.plus(794, 0) == 794


def test_plus_zero_float():
    assert functions_calculator.plus(-10.3, 0) == -10.3
    assert functions_calculator.plus(0, -1.1) == -1.1
    assert functions_calculator.plus(0, 10.9) == 10.9
    assert functions_calculator.plus(794.5, 0) == 794.5


def test_plus_init_and_float():
    assert functions_calculator.plus(2.5, 1) == 3.5
    assert functions_calculator.plus(1000, 100.1) == 1100.1
    assert functions_calculator.plus(-2.5, 1) == -1.5
    assert functions_calculator.plus(10, -100.1) == -90.1


def test_plus_large():
    assert functions_calculator.plus(2000000, 2000000) == 4000000


def test_minus_positive_int():
    assert functions_calculator.minus(3, 2) == 1
    assert functions_calculator.minus(2, 9) == -7


def test_minus_positive_float():
    assert functions_calculator.minus(5.5, 13.5) == -8
    assert functions_calculator.minus(500.3, 13.1) == 487.2


def test_minus_negative_int():
    assert functions_calculator.minus(-2, -10) == 8
    assert functions_calculator.minus(-2, -1) == -1


def test_minus_negative_float():
    assert functions_calculator.minus(-2.5, -10.6) == 8.1
    assert functions_calculator.minus(-200.6, -123.3) == -77.3


def test_minus_mixed_int():
    assert functions_calculator.minus(-10, 2) == -12
    assert functions_calculator.minus(67, -1) == 68


def test_minus_mixed_float():
    assert functions_calculator.minus(-10.5, 2.5) == -13
    assert functions_calculator.minus(67.1, -1.4) == 68.5


def test_minus_zero_int():
    assert functions_calculator.minus(-10, 0) == -10
    assert functions_calculator.minus(0, -1) == 1
    assert functions_calculator.minus(0, 0) == 0
    assert functions_calculator.minus(0, 10) == -10
    assert functions_calculator.minus(794, 0) == 794


def test_minus_zero_float():
    assert functions_calculator.minus(-10.3, 0) == -10.3
    assert functions_calculator.minus(0, -1.1) == 1.1
    assert functions_calculator.minus(0, 10.9) == -10.9
    assert functions_calculator.minus(794.5, 0) == 794.5


def test_minus_init_and_float():
    assert functions_calculator.minus(2.5, 1) == 1.5
    assert functions_calculator.minus(1000, 100.1) == 899.9
    assert functions_calculator.minus(-2.5, 1) == -3.5
    assert functions_calculator.minus(10, -100.1) == 110.1


def test_minus_large():
    assert functions_calculator.minus(2000000, 2000000) == 0


def test_multiply_positive_int():
    assert functions_calculator.multiply(100, 40) == 4000
    assert functions_calculator.multiply(2, 9) == 18


def test_multiply_positive_float():
    assert functions_calculator.multiply(5.5, 13.5) == 74.25
    assert functions_calculator.multiply(500.3, 13.1) == 6553.93


def test_multiply_negative_int():
    assert functions_calculator.multiply(-2, -10) == 20
    assert functions_calculator.multiply(-2, -1) == 2


def test_multiply_negative_float():
    assert functions_calculator.multiply(-2.5, -10.6) == 26.5
    assert functions_calculator.multiply(-200.6, -123.3) == 24733.98


def test_multiply_mixed_int():
    assert functions_calculator.multiply(-10, 2) == -20
    assert functions_calculator.multiply(67, -1) == -67


def test_multiply_mixed_float():
    assert functions_calculator.multiply(-10.5, 2.5) == -26.25
    assert functions_calculator.multiply(67.2, -1.4) == -94.08


def test_multiply_zero_int():
    assert functions_calculator.multiply(-10, 0) == 0
    assert functions_calculator.multiply(0, -1) == 0
    assert functions_calculator.multiply(0, 0) == 0
    assert functions_calculator.multiply(0, 10) == 0
    assert functions_calculator.multiply(794, 0) == 0


def test_multiply_zero_float():
    assert functions_calculator.multiply(-10.3, 0) == 0
    assert functions_calculator.multiply(0, -1.1) == 0
    assert functions_calculator.multiply(0, 10.9) == 0
    assert functions_calculator.multiply(794.5, 0) == 0


def test_multiply_init_and_float():
    assert functions_calculator.multiply(2.5, 1) == 2.5
    assert functions_calculator.multiply(1000, 100.1) == 100100
    assert functions_calculator.multiply(-2.5, 1) == -2.5
    assert functions_calculator.multiply(10, -100.1) == -1001


def test_multiply_large():
    assert functions_calculator.multiply(2000000, 2000000) == 4000000000000