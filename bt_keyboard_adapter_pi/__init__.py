SCAN_CODES_NAME_MAPPING = {
    1: "esc",
    2: "1",
    3: "2",
    4: "3",
    5: "4",
    6: "5",
    7: "6",
    8: "7",
    9: "8",
    10: "9",
    11: "0",
    12: "−",
    13: "=",
    14: "backspace",
    15: "tab",
    16: "q",
    17: "w",
    18: "e",
    19: "r",
    20: "t",
    21: "y",
    22: "u",
    23: "i",
    24: "o",
    25: "p",
    26: "[",
    27: "]",
    28: "enter",
    29: "left ctrl",
    30: "a",
    31: "s",
    32: "d",
    33: "f",
    34: "g",
    35: "h",
    36: "j",
    37: "k",
    38: "l",
    39: ";",
    40: "'",
    41: "`",
    42: "left shift",
    43: "\\",
    44: "z",
    45: "x",
    46: "c",
    47: "v",
    48: "b",
    49: "n",
    50: "m",
    51: ",",
    52: ".",
    53: "/",
    54: "right shift",
    55: "×",  # keypad *
    56: "left alt",
    57: "space",
    58: "caps lock",
    59: "f1",
    60: "f2",
    61: "f3",
    62: "f4",
    63: "f5",
    64: "f6",
    65: "f7",
    66: "f8",
    67: "f9",
    68: "f10",
    69: "num lock",
    70: "scroll lock",
    71: "7",  # keypad 7
    72: "8",  # keypad 8
    73: "9",  # keypad 9
    74: "-",  # keypad -
    75: "4",  # keypad 4
    76: "5",  # keypad 5
    77: "6",  # keypad 6
    78: "+",  # keypad +
    79: "1",  # keypad 1
    80: "2",  # keypad 2
    81: "3",  # keypad 3
    82: "0",  # keypad 0
    83: ".",  # keypad .
    87: "f11",
    88: "f12",
    96: "enter",  # keypad enter
    97: "right ctrl",
    98: "÷",  # keypad /
    99: "\\",  # print screen
    100: "right alt",
    102: "home",
    103: "up",
    104: "page up",
    105: "left",
    106: "right",
    107: "end",
    108: "down",
    109: "page down",
    110: "insert",
    111: "delete",
    119: "pause",
    125: "left windows",
    126: "right windows",
}

MODIFIER = {
    29: 0x01, # left ctrl
    42: 0x02, # left shift
    56: 0x04, # left alt
    125: 0x08, # left windows
    97: 0x10, # right ctrl
    54: 0x20, # right shift
    100: 0x40, # right alt
    126: 0x80, # right windows
}

SCAN_CODES_HID_USAGEID_MAPPING = {
    1: 0x29,  # esc
    2: 0x1E,  # 1!
    3: 0x1F,  # 2@
    4: 0x20,  # 3#
    5: 0x21,  # 4$
    6: 0x22,  # 5%
    7: 0x23,  # 6^
    8: 0x24,  # 7&
    9: 0x25,  # 8*
    10: 0x26,  # 9(
    11: 0x27,  # 0)
    12: 0x2D,  # -_
    13: 0x2E,  # =+
    14: 0x2A,  # backspace
    15: 0x2B,  # tab
    16: 0x14,  # q
    17: 0x1A,  # w
    18: 0x08,  # e
    19: 0x15,  # r
    20: 0x17,  # t
    21: 0x1C,  # y
    22: 0x18,  # u
    23: 0x0C,  # i
    24: 0x12,  # o
    25: 0x13,  # p
    26: 0x2F,  # [
    27: 0x30,  # ]
    28: 0x28,  # enter
    29: 0xE0,  # left ctrl
    30: 0x04,  # a
    31: 0x16,  # s
    32: 0x07,  # d
    33: 0x09,  # f
    34: 0x0A,  # g
    35: 0x0B,  # h
    36: 0x0D,  # j
    37: 0x0E,  # k
    38: 0x0F,  # l
    39: 0x33,  # ;:
    40: 0x34,  #'"
    41: 0x35,  # `~
    42: 0xE1,  # left shift
    43: 0x31,  # \|
    44: 0x1D,  # z
    45: 0x1B,  # x
    46: 0x06,  # c
    47: 0x19,  # v
    48: 0x05,  # b
    49: 0x11,  # n
    50: 0x10,  # m
    51: 0x36,  # ,<
    52: 0x37,  # .>
    53: 0x38,  # /?
    54: 0xE5,  # right shift
    55: 0x55,  # *(keypad)
    56: 0xE2,  # left alt
    57: 0x2C,  # space
    58: 0x39,  # caps lock
    59: 0x3A,  # f1
    60: 0x3B,  # f2
    61: 0x3C,  # f3
    62: 0x3D,  # f4
    63: 0x3E,  # f5
    64: 0x3F,  # f6
    65: 0x40,  # f7
    66: 0x41,  # f8
    67: 0x42,  # f9
    68: 0x43,  # f10
    69: 0x53,  # num lock
    70: 0x47,  # scroll lock
    71: 0x5F,  # 7(key pad)
    72: 0x60,  # 8(key pad)
    73: 0x61,  # 9(key pad)
    74: 0x56,  # -(key pad)
    75: 0x5C,  # 4(key pad)
    76: 0x5D,  # 5(key pad)
    77: 0x5E,  # 6(key pad)
    78: 0x57,  # +(key pad)
    79: 0x59,  # 1(key pad)
    80: 0x5A,  # 2(key pad)
    81: 0x5B,  # 3(key pad)
    82: 0x62,  # 0(key pad)
    83: 0x63,  # .(key pad)
    87: 0x44,  # f11
    88: 0x45,  # f12
    96: 0x58,  # enter(key pad)
    97: 0xE4,  # right ctrl
    98: 0x54,  # /(key pad)
    99: 0x46,  # print screen
    100: 0xE6,  # right alt
    102: 0x4A,  # home
    103: 0x52,  # up
    104: 0x4B,  # page up
    105: 0x50,  # left
    106: 0x4F,  # right
    107: 0x4D,  # end
    108: 0x51,  # down
    109: 0x4E,  # page down
    110: 0x49,  # insert
    111: 0x4C,  # delete
    119: 0x48,  # pause
    125: 0xE3,  # left windows
    126: 0xE7,  # right windows
}

NAME_MAPPING_TO_SCAN_CODES = {
    "esc":1,
    "1":2,
    "2":3,
    "3":4,
    "4":5,
    "5":6,
    "6":7,
    "7":8,
    "8":9,
    "9":10,
    "0":11,
    "−":12,
    "=":13,
    "backspace":14,
    "tab":15,
    "q":16,
    "w":17,
    "e":18,
    "r":19,
    "t":20,
    "y":21,
    "u":22,
    "i":23,
    "o":24,
    "p":25,
    "[":26,
    "]":27,
    "enter":28,
    "left ctrl":29,
    "a":30,
    "s":31,
    "d":32,
    "f":33,
    "g":34,
    "h":35,
    "j":36,
    "k":37,
    "l":38,
    ";":39,
    "'":40,
    "`":41,
    "left shift":42,
    "\\":43,
    "z":44,
    "x":45,
    "c":46,
    "v":47,
    "b":48,
    "n":49,
    "m":50,
    ",":51,
    ".":52,
    "/":53,
    "right shift":54,
    "×":55,  # keypad *
    "left alt":56,
    "space":57,
    "caps lock":58,
    "f1":59,
    "f2":60,
    "f3":61,
    "f4":62,
    "f5":63,
    "f6":64,
    "f7":65,
    "f8":66,
    "f9":67,
    "f10":68,
    "num lock":69,
    "scroll lock":70,
    "7":71,  # keypad 7
    "8":72,  # keypad 8
    "9":73,  # keypad 9
    "-":74,  # keypad -
    "4":75,  # keypad 4
    "5":76,  # keypad 5
    "6":77,  # keypad 6
    "+":78,  # keypad +
    "1":79,  # keypad 1
    "2":80,  # keypad 2
    "3":81,  # keypad 3
    "0":82,  # keypad 0
    ".":83,  # keypad .
    "f11":87,
    "f12":88,
    "enter":96,  # keypad enter
    "right ctrl":97,
    "÷":98,  # keypad /
    "\\":99,  # print screen
    "right alt":100,
    "home":102,
    "up":103,
    "page up":104,
    "left":105,
    "right":106,
    "end":107,
    "down":108,
    "page down":109,
    "insert":110,
    "delete":111,
    "pause":119,
    "left windows":125,
    "right windows":126,
}