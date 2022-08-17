# coding:utf-8

import debug.value_string as vs

debug_mode = False
nest_level = 0
max_level = 9

enter_nest = ['+', '| +', '| | +', '| | | +', '| | | | +', '| | | | | +', '| | | | | | +', '| | | | | | | +',
              '| | | | | | | | +', '| | | | | | | | | +']
print_nest = ['', '| ', '| | ', '| | | ', '| | | | ', '| | | | | ', '| | | | | | ', '| | | | | | | ',
              '| | | | | | | | ', '| | | | | | | | | ']

debug_file = None


def start(file="debug.txt"):
    global debug_mode
    global debug_file
    debug_mode = True
    print("debug start.")
    if file: debug_file = open(file, 'w')


def end():
    global debug_mode
    global debug_file
    if debug_file: debug_file.close()
    if debug_mode: print("debug end.")
    debug_mode = False


class logger(object):

    def __init__(self, name=""):
        self.name = name

    def enter(self, func=""):
        global debug_mode
        global nest_level
        global max_level
        global enter_nest
        global debug_file
        if debug_file:
            debug_file.write("{0}enter[{1}.{2}]\n".format(enter_nest[nest_level], self.name, vs.value_string(func)))
        if nest_level < max_level: nest_level = nest_level + 1

    def leave(self):
        global debug_mode
        global nest_level
        global max_level
        global enter_nest
        global debug_file
        if nest_level < max_level: nest_level = nest_level - 1
        if debug_file:
            debug_file.write("{0}leave[]\n".format(enter_nest[nest_level]))

    def put(self, value, name=None):
        global debug_mode
        global print_nest
        global debug_file
        if not debug_file: return
        if isinstance(name, str):
            debug_file.write("{0} {1}={2}\n".format(print_nest[nest_level], name, vs.value_string(value)))
        else:
            debug_file.write("{0} {1}\n".format(print_nest[nest_level], vs.value_string(value)))


def test():
    start("test.debug")
    log = logger("test")
    val1 = "this is a string"
    val2 = 10
    val3 = -0.123
    array1 = [val1, val2, val3, None, "", 0, True]
    array2 = ["Hoge", -5.0, 9.9, None, "", 3, False]
    dic = {}
    dic["karen"] = array2
    dic["reito"] = array1
    log.put(dic)
    end()


if __name__ == '__main__':
    test()
