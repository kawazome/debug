# coding:utf-8

from datetime import datetime

def value_string(val):
    if isinstance(val, bool): return bool_string(val)
    if val == None: return "None"
    if isinstance(val, str): return val
    if isinstance(val, (int, float, complex)): return str(val)
    if isinstance(val, list): return list_string(val)
    if isinstance(val, tuple): return tuple_string(val)
    if isinstance(val, dict): return dict_string(val)
    if isinstance(val, datetime): return date_string(val)
    return "#cannot represent by letters"


def bool_string(val):
    if val == True:
        return "True"
    else:
        return "False"


def list_string(vals):
    if not isinstance(vals, list): return ""
    array = []
    for val in vals: array.append(value_string(val))
    return "[" + ','.join(array) + "]"


def tuple_string(vals):
    if not isinstance(vals, tuple): return ""
    array = []
    for val in vals: array.append(value_string(val))
    return "(" + ','.join(array) + ")"


def dict_string(vals):
    if not isinstance(vals, dict): return ""
    array = []
    for key, value in vals.items():
        array.append(" " + value_string(key) + ": " + value_string(value))
    return "{" + ','.join(array) + " }"


def date_string(val):
    if not isinstance(val, datetime): return ""
    return val.strftime('%Y/%m/%d %H:%M:%S')

