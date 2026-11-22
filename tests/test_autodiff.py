import pytest

from vesper.autodiff import ScalarGraph, ScalarOperation


@pytest.fixture
def two_operands():
    return ScalarGraph(2.0), ScalarGraph(3.0)


def test_addition(two_operands):
    x, y = two_operands
    assert (x + y).value == pytest.approx(5.0)
    assert x.value == pytest.approx(2.0)
    assert y.value == pytest.approx(3.0)
    second_x, second_y = (x + y).inputs
    assert x is second_x
    assert y is second_y
    assert (x + y).operation == ScalarOperation.ADDITION


def test_multiplication(two_operands):
    x, y = two_operands
    assert (x * y).value == pytest.approx(6.0)
    assert x.value == pytest.approx(2.0)
    assert y.value == pytest.approx(3.0)
    second_x, second_y = (x * y).inputs
    assert x is second_x
    assert y is second_y
    assert (x * y).operation == ScalarOperation.MULTIPLICATION


def test_empty(two_operands):
    x, _ = two_operands
    assert x.value == pytest.approx(2.0)
    assert x.operation == ScalarOperation.LEAF
    assert x.inputs == ()


def test_composed(two_operands):
    x, y = two_operands
    u = x * y
    v = x + y
    z = u * v
    assert u.value == pytest.approx(6.0)
    assert v.value == pytest.approx(5.0)
    assert z.value == pytest.approx(30.0)
    assert z.inputs[0] is u
    assert z.inputs[1] is v
    assert u.inputs[0] is x
    assert v.inputs[1] is y


def test_self_ref(two_operands):
    x, _ = two_operands
    u = x * x
    assert u.inputs[0] is x
    assert u.inputs[1] is x
    v = x + x
    assert v.inputs[0] is x
    assert v.inputs[1] is x


def test_equal_different():
    x = ScalarGraph(2.0)
    y = ScalarGraph(2.0)
    assert x is not y
