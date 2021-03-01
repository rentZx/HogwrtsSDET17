#!/usr/bin/env python
# encoding: utf-8
"""
@author: zixue.ren
@contact: renzixue@58.com
@file: test_a.py
@time: 2021/2/28 13:16
@desc:pytestDemo
"""
import pytest


def func(x):
    return x + 1


@pytest.mark.parametrize('a,b', [
    (1, 2),
    (3, 3),
    (5, 6)
])
def test_answer(a, b):
    assert func(a) == b


@pytest.fixture()
def login():
    print("login")
    return "jerry"


class TestDemo():
    def test_a(self, login):
        print("a")

    def test_b(self):
        print("b")

    def test_c(self):
        print("c")
