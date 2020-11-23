import sys


class Input:
    def __init__(self):
        try:
            self.arg = sys.argv[1]
        except IndexError:
            self.arg = 'hello'
            pass
