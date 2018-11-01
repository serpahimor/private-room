# -*- coding: utf-8 -*-
from time import time
import json
import csv


def isProvince(s):
    return s.endswith('0000')


def isCity(s):
    return s.endswith('00')


def get_data(filename):
    f = open(filename, "r", encoding="utf-8")
    _lines = f.readlines()
    f.close()
    return _lines


provinces = {}

if __name__ == "__main__":
    lines = get_data('city.txt')
    cities = []
    for line in lines:
        # parse the city data, output code and name
        cities.append(tuple(line.split()))

    results = []
    _cities = []
    p = None
    c = None
    for v in cities:
        code = v[0]
        name = v[1]
        if isProvince(code):
            p = {
                'name': v[1],
                'code': v[0],
                'cities': []
            }
            results.append(p)
        elif isCity(code):
            c = {
                'name': v[1],
                'code': v[0],
                'counties': []
            }
            p['cities'].append(c)
            _cities.append({
                'name': v[1],
                'code': v[0],
            })
        else:
            c['counties'].append({
                'name': v[1],
                'code': v[0]
            })

    # ss = json.dumps({
    #     'provinces': results},indent=4, ensure_ascii=False )
    ss = json.dumps({
        'province': results
    }, indent=4, ensure_ascii=False)

    print(ss)