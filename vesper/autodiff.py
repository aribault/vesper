from __future__ import annotations
from enum import Enum

class ScalarOperation(Enum):
    LEAF = "leaf"
    ADDITION = "addition"
    MULTIPLICATION = "multiplication"

class ScalarGraph:
    value: float
    operation: ScalarOperation
    inputs: tuple[ScalarGraph, ...]

    def __init__(self, value: float):
        self.value = value
        self.operation = ScalarOperation.LEAF
        self.inputs = ()

    def __add__(self, other: ScalarGraph):
        value = self.value + other.value
        res = ScalarGraph(value)
        res.operation = ScalarOperation.ADDITION
        res.inputs = (self, other)
        return res

    def __mul__(self, other: ScalarGraph):
        value = self.value * other.value
        res = ScalarGraph(value)
        res.operation = ScalarOperation.MULTIPLICATION
        res.inputs = (self, other)
        return res
