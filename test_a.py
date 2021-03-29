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
import requests


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


class TestRequest():
    def setup(self):
        pass

    def test_get(self):
        herder = {
            "Cookie": "_ga=GA1.2.1671349380.1615960729; Hm_lvt_214f62eef822bde113f63fedcab70931=1616036531,1616036777,1616136837,1616670644; _gid=GA1.2.1596377054.1616670644; _t=8e994db882367347afaf7dc0fd162ac7; _forum_session=OXRudGltYkswZlRwNmdlbi9vclZyTnh1MGxpMjhlWWE1MmlQdFFOL1JpTnpUdUw5bVJxck9mclBzdS9BRkxNM0NpT3d2K2U2ek9zei9teHNyZURHaXZseUkwQW16Mm13VGFhM1c5TER1YWpYTngvbEtveE1GaE02QndleVNPUHN5QWQxYUw2UzhzcmtNaGs0N0xidmcwOG5vWkMyN25GQ3kxVC9ZQlZENFpDVktzZ1NIdTM3Y2I4WlBYYTlBdXNCLS0vRjRRUmJiRW9yaEltM2FlQlc5ZURnPT0%3D--9a1bbe18a4b1c55104bff18af864c2a920990817; Hm_lpvt_214f62eef822bde113f63fedcab70931=1616672196"
        }
        parameter = {
            "ascending": "false"
        }
        response = requests.get("https://ceshiren.com/c/sdet-python/7/l/latest.json", params=parameter, headers=herder)
        print("\n~~~~~\n")
        print(response.json()["users"][0]["id"])
        assert response.status_code == 200