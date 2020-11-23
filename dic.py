from textwrap import wrap

from termcolor import colored

from Apier.iciba import IciCH, IciEN
from libs.helper import is_chinese
from shell.cmd import Cmd
from shell.input import Input


def main():
    user_input = Input()
    word = user_input.arg
    if is_chinese(word):
        result = IciCH()
        try:
            result.search(word)
            cmd = Cmd(result.info)
            cmd.show_ch()
        except TypeError:
            print('查询失败！')
    else:
        result = IciEN()
        try:
            result.search(word)
            cmd = Cmd(result.info)
            cmd.show_en()
        except TypeError or KeyError:
            print(Cmd.wrap('warning', '查询失败！', outside=True))


if __name__ == '__main__':
    main()
