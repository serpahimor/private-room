2# -*- coding:utf-8 -*-
import os.path
import json
import requests


class PinYin(object):
    def __init__(self, dict_file='word.data'):
        self.word_dict = {}
        self.dict_file = dict_file

    def load_word(self):
        if not os.path.exists(self.dict_file):
            raise IOError("NotFoundFile")

        with open(self.dict_file) as f_obj:
            for f_line in f_obj.readlines():
                try:
                    line = f_line.split()
                    self.word_dict[line[0]] = line[1]
                except:
                    line = f_line.split()
                    self.word_dict[line[0]] = line[1]

    def hanzi2pinyin(self, string=""):
        result = []



        if not isinstance(string, str):
            string = string.decode("utf-8")

        for char in string:
            key = '%X' % ord(char)
            if not self.word_dict.get(key):
                result.append(char)
            else:
                result.append(self.word_dict.get(key, char).split()[0][:-1].lower())

        return result

    def hanzi2pinyin_split(self, string="", split=""):
        result = self.hanzi2pinyin(string=string)
        # if split == "":
        #    return result
        # else:
        return split.join(result)

    def getJW(self, name):
        url = "http://api.map.baidu.com/geocoder/v2/?ak=uiwx7N7FhYKGNqCxVGjCGcMPPrivr6fE&output=json&address='+encodeURIComponent("+name+")"
        response = requests.get(url)
        return json.loads(response.text)




if __name__ == "__main__":
    test = PinYin()
    test.load_word()
    # response = test.getJW("北京市")
    # print(response['result']['location'])
    # C = {"cities": []}
    ar = []
    with open('ha.json', 'r', encoding="utf-8") as json_file:

        data = json.load(json_file)
        arr = data['cities']

        for i in arr:
            name = i['name']
            code = i['code']
            pingyin = i['pingyin']
            response = test.getJW(name)
            lng = None
            lat = None
            if response['status'] == 1:
                lng = "无结果"
                lat = "无结果"
            else:
                lng = response['result']['location']['lng']
                lat = response['result']['location']['lat']

            content = {
                "name": name,
                "code": code,
                "pingyin": pingyin,
                "lng": lng,
                "lat": lat
            }
            ar.append(content)
    #
    #
    #
    ss = json.dumps({
            'cities': ar
        }, indent=4, ensure_ascii=False)
    print(ss)









    # with open("ha.json", "w") as f:
    # 	f.write(ss)
    #
    # print(C)
        # print(json_file)
    # string = "钓鱼岛是中国的"
    # print("in: %s" % string)
    # print("out: %s" % str(test.hanzi2pinyin(string=string)))
    # print("out: %s" % test.hanzi2pinyin_split(string=string, split=""))
