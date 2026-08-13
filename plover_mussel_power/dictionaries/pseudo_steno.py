"""
replaces the raw steno positions from Plover with the associated chord's sound
"""
import re

LONGEST_KEY = 1
TOKEN_RE = re.compile(r"\d(?:[lrLR])?|.")

LEFT = {
    "1": "R", "1l": "W", "1r": "V", "1L": "RY", "1R": "KM",
    "2": "K", "2l": "KR", "2r": "KN", "2L": "KW", "2R": "KL",
    "3": "B", "3l": "M", "3r": "H", "3L": "BR", "3R": "BL",
    "4": "P", "4l": "Y", "4r": "PL", "4L": "PR", "4R": "Z",
    "5": "L", "5l": "G", "5r": "J", "5L": "GR", "5R": "SH",
    "6": "D", "6l": "F", "6r": "DS", "6L": "FL", "6R": "FR",
    "7": "S", "7l": "N", "7r": "ST", "7L": "SP", "7R": "STR",
    "8": "T", "8l": "AH", "8r": "TR", "8L": "AN", "8R": "CH",
}

RIGHT = {
    "1": "S", "1l": "Z", "1r": "SE", "1L": "ST", "1R": "RSE",
    "2": "NG", "2l": "SH", "2r": "NK", "2L": "CH", "2R": "B",
    "3": "Y", "3l": "G", "3r": "K", "3L": "J", "3R": "BL",
    "4": "L", "4l": "LY", "4r": "LD", "4L": "LS", "4R": "LT",
    "5": "D", "5l": "P", "5r": "M", "5L": "RM", "5R": "MP",
    "6": "N", "6l": "ND", "6r": "NT", "6L": "NSE", "6R": "NS",
    "7": "T", "7l": "F", "7r": "V", "7L": "TH", "7R": "RK",
    "8": "R", "8l": "RT", "8r": "RS", "8L": "RD", "8R": "RY",
}

VOWELS = set("AOEU")


def convert_key(stroke):
    tokens = TOKEN_RE.findall(stroke)
    out = []

    prev = None
    for token in tokens:
        if token[0].isdigit():
            if prev == "-" or prev in VOWELS:
                out.append(RIGHT[token])
            else:
                out.append(LEFT[token])
        else:
            out.append(token)
        prev = token

    return "".join(out)


def lookup(strokes):

    stroke = strokes[0] #This is for one-strokes after all

    if stroke == 'E': # undo button
        raise KeyError

    return convert_key(stroke)
