# way one to do things
#############################################################
# from subprocess import Popen, PIPE

# control_f4_sequence = '''keydown Control_L
# keydown Alt_L
# key l
# keyup Alt_L
# keyup Control_L
# '''

# shift_a_sequence = '''keydown Shift_L
# key A
# keyup Shift_L
# '''

# key_a_down = '''keydown q
# '''

# key_a_up = '''keyup q
# keydown \x1B[C
# keyup \x1B[C
# '''


#way two
#################################################################
# def keypress(sequence):
#     p = Popen(['xte'], stdin=PIPE)
#     p.communicate(input=sequence)

# #keypress(shift_a_sequence)
# #keypress(control_f4_sequence)

# keypress(key_a_down)
# i = 1
# while(i<10000000):
#     i = i + 1

# keypress(key_a_up)

#way 3
###################################################################
# from evdev import uinput, ecodes as e

# with uinput.UInput() as ui:
#      ui.write(e.EV_KEY, e.KEY_ENTER, 1)
#      ui.write(e.EV_KEY, e.KEY_ENTER, 0)
#      ui.syn()

# import uinput
# `
# device = uinput.Device([
#         uinput.KEY_LEFTALT,
#         uinput.KEY_TAB,
#         ])

# device.emit_combo([
#         uinput.KEY_LEFTALT,
#         uinput.KEY_TAB,
#         ])


#workign way
######################################################################



from pykeyboard import PyKeyboard
import sys

# for checking if a string is a number or not
def isInt(s):
    if s.isdigit():
        return True
    elif s[0] == '-' and s[1:].isdigit():
        return True
    else:
        return False

k = PyKeyboard()
'''
backspace = k.backspace_key
tab = k.tab_key
enter = k.enter_key
shift = k.shift_l_key
ctrl = k.control_l_key
alt = k.alt_key
pause_break = k.pause_key
caps_lock = k.caps_lock_key
escape = k.escape_key
page_up = k.page_up_key
page_down = k.page_down_key
end = k.end_key
home = k.home_key
left_arrow = k.left_key
up_arrow = k.up_key
right_arrow = k.right_key
down_arrow = k.down_key
insert = k.insert_key
delete = k.delete_key
left_window_key = k.windows_l_key
right_window_key = k.windows_r_key
select_key = k.select_key
numpad_0 = k.numpad_keys[0]
numpad_1 = k.numpad_keys[1]
numpad_2 = k.numpad_keys[2]
numpad_3 = k.numpad_keys[3]
numpad_4 = k.numpad_keys[4]
numpad_5 = k.numpad_keys[5]
numpad_6 = k.numpad_keys[6]
numpad_7 = k.numpad_keys[7]
numpad_8 = k.numpad_keys[8]
numpad_9 = k.numpad_keys[9]
multiply = k.numpad_keys['Multiply']
add = k.numpad_keys['Add']
subtract = k.numpad_keys['Subtract']
decimal_point = k.numpad_keys['Decimal']
divide = k.numpad_keys['Divide']
f1 = k.function_keys[1]
f2 = k.function_keys[2]
f3 = k.function_keys[3]
f4 = k.function_keys[4]
f5 = k.function_keys[5]
f6 = k.function_keys[6]
f7 = k.function_keys[7]
f8 = k.function_keys[8]
f9 = k.function_keys[9]
f10 = k.function_keys[10]
f11 = k.function_keys[11]
f12 = k.function_keys[12]
num_lock = k.num_lock_key
scroll_lock = k.scroll_lock_key
semi_colon = ';'
equal_sign = '='
comma = ','
dash = '-'
period = '.'
forward_slash = '/'
grave_accent = None
open_bracket = '['
back_slash = '\\'
close_braket = ']'
single_quote = '\''


# mapping from numbers to keys
key_map = {8 : backspace  ,
           9 : tab  ,
           13 : enter  ,
           16 : shift  ,
           17 : ctrl  ,
           18 : alt  ,
           19 : pause_break  ,
           20 : caps_lock  ,
           27 : escape  ,
           32 : " " ,
           33 : page_up  ,
           34 : page_down  ,
           35 : end  ,
           36 : home  ,
           37 : left_arrow  ,
           38 : up_arrow  ,
           39 : right_arrow  ,
           40 : down_arrow  ,
           45 : insert  ,
           46 : delete  ,
           48 : '0'  ,
           49 : '1'  ,
           50 : '2'  ,
           51 : '3'  ,
           52 : '4'  ,
           53 : '5'  ,
           54 : '6'  ,
           55 : '7'  ,
           56 : '8'  ,
           57 : '9'  ,
           65 : 'a'  ,
           66 : 'b'  ,
           67 : 'c'  ,
           68 : 'd'  ,
           69 : 'e'  ,
           70 : 'f'  ,
           71 : 'g'  ,
           72 : 'h'  ,
           73 : 'i'  ,
           74 : 'j'  ,
           75 : 'k'  ,
           76 : 'l'  ,
           77 : 'm'  ,
           78 : 'n'  ,
           79 : 'o'  ,
           80 : 'p'  ,
           81 : 'q'  ,
           82 : 'r'  ,
           83 : 's'  ,
           84 : 't'  ,
           85 : 'u'  ,
           86 : 'v'  ,
           87 : 'w'  ,
           88 : 'x'  ,
           89 : 'y'  ,
           90 : 'z'  ,
           91 : left_window_key  ,
           92 : right_window_key  ,
           #93 : select_key  ,
           96 : numpad_0  ,
           97 : numpad_1  ,
           98 : numpad_2  ,
           99 : numpad_3  ,
           100 : numpad_4  ,
           101 : numpad_5  ,
           102 : numpad_6  ,
           103 : numpad_7  ,
           104 : numpad_8  ,
           105 : numpad_9  ,
           106 : multiply  ,
           107 : add  ,
           109 : subtract  ,
           110 : decimal_point  ,
           111 : divide  ,
           112 : f1  ,
           113 : f2  ,
           114 : f3  ,
           115 : f4  ,
           116 : f5  ,
           117 : f6  ,
           118 : f7  ,
           119 : f8  ,
           120 : f9  ,
           121 : f10  ,
           122 : f11  ,
           123 : f12  ,
           144 : num_lock  ,
           145 : scroll_lock  ,
           186 : semi_colon  ,
           187 : equal_sign  ,
           188 : comma  ,
           189 : dash  ,
           190 : period  ,
           191 : forward_slash  ,
           #192 : grave_accent  ,
           219 : open_bracket  ,
           220 : back_slash  ,
           221 : close_braket  ,
           222 : single_quote  
           }  
'''
key_map = [0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            22,
            23,
            0,
            0,
            0,
            36,
            0,
            0,
            50,
            37,
            64,
            127,
            66,
            0,
            0,
            0,
            0,
            0,
            0,
            9,
            0,
            0,
            0,
            0,
            ' ',
            112,
            117,
            115,
            110,
            113,
            111,
            114,
            116,
            0,
            0,
            0,
            0,
            118,
            119,
            0,
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            'a',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
            'm',
            'n',
            'o',
            'p',
            'q',
            'r',
            's',
            't',
            'u',
            'v',
            'w',
            'x',
            'y',
            'z',
            133,
            134,
            0,
            0,
            0,
            90,
            87,
            88,
            89,
            83,
            84,
            85,
            79,
            80,
            81,
            63,
            86,
            0,
            82,
            129,
            106,
            67,
            68,
            69,
            70,
            71,
            72,
            73,
            74,
            75,
            76,
            95,
            96,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            77,
            78,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            ';',
            '=',
            ',',
            '-',
            '.',
            '/',
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            '[',
            '\\',
            ']',
            '\'']
'''
i = 0
while i <= 222:
  if i in key_map:
    if isInt(str(key_map[i])):
      print str(key_map[i]) + ","
    else:
      print "'" + key_map[i] + "',"
  else:
    print "0,"
  i+=1
'''
'''
# length of arguments
len = len(sys.argv)

# argument lengths should be equal to 2

if len < 2:
    print "usage -> python keyPressTest.py arg1"
else:
    # when only one argument present
  '''
key_value_str = sys.argv[1]
#if isInt(key_value_str):
key_value = int(key_value_str)
if key_value >= 0:
    k.press_key(key_map[key_value])
else:
    k.release_key(key_map[-key_value])
#else:
#    print "Please provide a number int as argument"
