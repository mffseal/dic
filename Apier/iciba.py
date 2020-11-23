from libs.httper import HTTP
from setting import API_KEY


class Ici:
    key = API_KEY
    type = 'json'
    url = 'http://dict-co.iciba.com/api/dictionary.php'

    def __init__(self):
        self.info = []
        self.payload = {
            'key': self.key,
            'type': self.type,
        }

    def get_result(self, word):
        self.payload['w'] = word
        r = HTTP.get(url=self.url, params=self.payload)
        return r


class IciCH(Ici):
    def search(self, word):
        result_raw = self.get_result(word)
        self.__fill(result_raw)

    def __fill(self, data):
        symbols_raw = data['symbols']

        for s in symbols_raw:
            symbol = {
                'word_symbol': s.get('word_symbol'),
                'parts': []
            }
            for p in s['parts']:
                # 处理空字典
                if p.__contains__('means') is False:
                    continue
                part = {
                    'part_name': p.get('part_name'),
                    'means': []
                }
                for m in p['means']:
                    part['means'].append(m.get('word_mean'))
                symbol['parts'].append(part)
            self.info.append(symbol)


class IciEN(Ici):
    def search(self, word):
        result_raw = self.get_result(word)
        self.__fill(result_raw)

    def __fill(self, data):
        symbol_raw = data['symbols'][0]
        # 获取发音信息
        ph = {
            'ph_en': symbol_raw.get('ph_en'),
            'ph_am': symbol_raw.get('ph_am')
        }
        self.info.append(ph)

        pms = []
        # 获取词性和词义
        for pm in symbol_raw.get('parts'):
            pm_new = {
                'part': pm.get('part'),
                'means': pm.get('means')
            }
            pms.append(pm_new)
        self.info.append(pms)


def test():
    ie = IciEN()
    ie.search('hello')
    print(ie.info)
    ic = IciCH()
    ic.search('行')
    print(ic.info)


if __name__ == '__main__':
    test()
