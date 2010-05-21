import os

Digits = [
    [' _ ','   ',' _ ',' _ ','   ',' _ ',' _ ',' _ ',' _ ',' _ ','   ',' _ ','   ',' _ ','   ',' _ '],
    ['| |','  |',' _|',' _|','|_|','|_ ','|_ ','  |','|_|','|_|',' _ ','|_|','|_ ','|  ',' _|','|_ '],
    ['|_|','  |','|_ ',' _|','  |',' _|','|_|','  |','|_|',' _|','   ','| |','|_|','|_ ','|_|','|_ '],
]

Segments = [
    "M 3 1 L 17 1 13 5 7 5 Z",                      # top
    "M 2 3 L 6 7 6 10 2 14 Z",                      # left upper
    "M 18 3 L 18 14 14 10 14 7 Z",                  # right upper
    "M 6.5 12.5 L 13.5 12.5 16 14.5 13.5 16.5 6.5 16.5 4 14.5 Z",   # middle
    "M 2 15 L 6 19 6 22 2 26 Z",                    # left lower
    "M 18 15 L 18 26 14 22 14 19 Z",                # right lower
    "M 3 28 L 17 28 13 24 7 24 Z",                  # bottom
]

for i in range(len(Digits[0])):
    name = "0123456789-ABCDE"[i]
    f = open(name + ".svg", "w")
    print >>f, """<?xml version="1.0"?>
        <svg width="20" height="30">
            <g fill="black">"""
    if Digits[0][i][1] == '_': print >>f, """<path d="%s" />""" % Segments[0]
    if Digits[1][i][0] == '|': print >>f, """<path d="%s" />""" % Segments[1]
    if Digits[1][i][2] == '|': print >>f, """<path d="%s" />""" % Segments[2]
    if Digits[1][i][1] == '_': print >>f, """<path d="%s" />""" % Segments[3]
    if Digits[2][i][0] == '|': print >>f, """<path d="%s" />""" % Segments[4]
    if Digits[2][i][2] == '|': print >>f, """<path d="%s" />""" % Segments[5]
    if Digits[2][i][1] == '_': print >>f, """<path d="%s" />""" % Segments[6]
    print >>f, """ </g>
        </svg>"""
    f.close()
    os.system("convert -background none %s.svg %s.png" % (name, name))

f = open("decimal.svg", "w")
print >>f, """<?xml version="1.0"?>
    <svg width="4" height="4">
        <rect width="100%" height="100%" fill="black" />
    </svg>"""
f.close()
os.system("convert -background none decimal.svg decimal.png")

f = open("neg.svg", "w")
print >>f, """<?xml version="1.0"?>
    <svg width="12" height="3">
        <rect width="100%" height="100%" fill="black" />
    </svg>"""
f.close()
os.system("convert -background none neg.svg neg.png")
