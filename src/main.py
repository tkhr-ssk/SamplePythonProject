# -*- coding: utf-8 -*-
"""Sample Project Main

     * ソースコードの一番始めに記載すること
     * importより前に記載する

Todo:
   TODOリストを記載
    * xxx をしないと使用できない
"""

from liba import liba_print


def add_func(a: int, b: int):
    """add function
    2つの値の和を取得する

    Parameters:
    ----------
    a: int
        一つ目の値
    b: int
        二つ目の値

    Returns
    -------
    sum: int
        二つの値の和
    """
    return a+b


def main():
    """main
    """
    print("hello world")
    print(add_func(10, 20))
    liba_print("abc")


if __name__ == "__main__":
    main()
