from termcolor import colored
from colorama import init


class Cmd:
    # 输出颜色设置
    style = {
        'div_line': {
            'color': 'green',
            'change': []
        },
        'ph_e': {
            'color': 'magenta',
            'change': []
        },
        'ph_a': {
            'color': 'magenta',
            'change': []
        },
        'ph_e_v': {
            'color': 'cyan',
            'change': []
        },
        'ph_a_v': {
            'color': 'cyan',
            'change': []
        },
        'part_e_v': {
            'color': 'blue',
            'change': ['bold', 'underline']
        },
        'mean_e_v': {
            'color': 'yellow',
            'change': []
        },
        'symbol_c_v': {
            'color': 'white',
            'change': ['bold']
        },
        'part_c_v': {
            'color': 'blue',
            'change': ['bold', 'underline']
        },
        'mean_c_v': {
            'color': 'yellow',
            'change': []
        },
        'warning': {
            'color': 'red',
            'change': ['bold', 'reverse']
        }
    }

    # 初始化需要输出的数据
    def __init__(self, data):
        self.data = data
        # 兼容windows控制台
        init()

    # 输出英文的样式
    def show_en(self):
        phs = self.data[0]
        part_means = self.data[1]
        # 输出发音
        wrap_ph_e = self.wrap('ph_e', '英音: ')
        print(wrap_ph_e, end='')
        wrap_ph_e_v = self.wrap('ph_e_v', phs.get('ph_en'))
        print('[%s]' % wrap_ph_e_v, end='\t\t')
        wrap_ph_a = self.wrap('ph_a', '美音: ')
        print(wrap_ph_a, end='')
        wrap_ph_a_v = self.wrap('ph_a_v', phs.get('ph_am'))
        print('[%s]' % wrap_ph_a_v, end='')
        self._diver()
        # 输出词性和词义
        for pms in part_means:
            wrap_part = self.wrap('part_e_v', pms.get('part'))
            print(wrap_part)
            for m in pms['means']:
                wrap_mean = self.wrap('mean_e_v', m)
                print('\t' + wrap_mean)
        self._diver()

    def show_ch(self):
        for single_word in self.data:
            wrap_symbol = self.wrap('symbol_c_v', single_word['word_symbol'])
            print(wrap_symbol)
            for pm in single_word['parts']:
                part_time = pm.get('part_name')
                if part_time == '':
                    part_time = '--'
                wrap_p = self.wrap('part_c_v', part_time)
                print(wrap_p + ': ')
                for m in pm['means']:
                    wrap_m = self.wrap('mean_c_v', m)
                    print('\t' + wrap_m)
            self._diver()

    # 为文字包装样式
    @classmethod
    def wrap(cls, kind, text_raw, outside=False):
        # 外部调用时执行初始化
        if outside:
            init()

        this_style = cls.style[kind]
        text = colored(text_raw, this_style['color'], attrs=this_style['change'])
        return text

    @classmethod
    def _diver(cls):
        div_line = '\n-----------------------------------\n'
        wrap_div_line = cls.wrap('div_line', div_line)
        print(wrap_div_line, end='')
