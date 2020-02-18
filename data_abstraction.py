"""
数据抽象
"""
from operator import getitem

empty_list = None

"""
构建有理数
基于python的元组实现(tuple)
"""
def make_rat(n, d):
    return (n, d)


"""
获取有理数的分子
"""
def numer(x):
    return getitem(x, 0)


"""
获取有理数的分母
"""
def denom(x):
    return getitem(x, 1)


def add_rat(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return make_rat(nx * dy + ny * dx, dx * dy)


def mul_rat(x, y):
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))


def eq_rat(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


def make_pair(x, y):
    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y
    return dispatch


def get_pair(p, i):
    return p(i)


def str_rat(x):
    """
    :param x:
    :return:
    return a string 'n/d' for numerator n and denominator d.
    """
    return '{0}/{1}'.format(numer(x), denom(x))


def make_rlist(first, rest):
    return (first, rest)


def first(s):
    """
    递归元组的第一个元素
    :param s: 递归元组
    :return: 递归元组的第一个元素
    """
    return s[0]


def rest(s):
    """
    递归元组除第一个其余的部分
    :param s: 递归元组
    :return: 递归元组除第一个其余的部分
    """
    return s[1]


def len_list(s):
    """
    获取递归元组的长度
    :param s: 待求解递归元组
    :return: 递归元组的长度
    """
    length = 0
    while s != empty_list:
        s, length = rest(s), length + 1
    return length


def getitem_rlist(s, i):
    """
    获取第i个元素
    :param s: 递归元组
    :param i: 第i个元素
    :return: 第i个元素
    """
    while i > 0:
        s, i = rest(i), i - 1
    return first(s)


# while循环版本的遍历
# def count(s, value):
#     total, index = 0, 0
#     while index < len(s):
#         if s[index] == value:
#             total = total + 1
#         index = index + 1
#     return total


def count(s, value):
    """
    for循环版本的遍历
    :param s: 待遍历链表
    :param value: 待查找值
    :return: value的出现次数
    """
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    return total


if __name__ == '__main__':
    print(1/3)
    print(1/3 == 0.33333333333333333333333300000)
    half = make_rat(1, 2)
    print(str_rat(half))
    counts = make_rlist(2, make_rlist(2, make_rlist(3, make_rlist(4, empty_list))))
    print(first(counts))
    print(rest(counts))

