"""
Mussel Power is a layout formed of 3 banks
- left joystick for initial consonants
- bumpers and triggers for vowels
- right joystick for final consonants



    initials      vowels          finals
    8- 1- 2-      A- O- -E -U     -8 -1 -2
    7-    3-                      -7    -3
    6- 5- 4-                      -6 -5 -4

Joysticks can have an r or l appended to their direction by going clockwise or anticlockwise respectively, a larger movement for R or L

Selecting this system in Plover (Configure -> System) rebinds the controller to these keys via ``KEYMAPS["Controller"]`` below, so no separate machine is needed -- the same "Controller" machine emits both WSI and Mussel keys, and the active system decides which ones are meaningful.
"""

# fmt: off
KEYS = (
    "1-", "2-", "3-", "4-",
    "5-", "6-", "7-", "8-",
    "l-", "r-", "L-", "R-",
    "S-", # for stick clicks

    "A-", "O-", "-E", "-U",

    "-1", "-2", "-3", "-4",
    "-5", "-6", "-7", "-8",
    "-l", "-r", "-L", "-R",
    "-S" # for stick clicks
)
# fmt: on

# These vowels sit between the banks, so the hyphen is implicit there.
IMPLICIT_HYPHEN_KEYS = ("A-", "O-", "-E", "-U")

SUFFIX_KEYS = ()

# Mussel's 1-8 are consonant keys, not a number bar, so there is no number key.
NUMBER_KEY = None
NUMBERS = {}

UNDO_STROKE_STENO = "E"

ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_RULES_ALIASES = {}
ORTHOGRAPHY_WORDLIST = None

# Identity keymap: the controller profile emits Mussel key names directly, so
# each system action binds to the machine key of the same name.
KEYMAPS = {
    "Controller": {key: key for key in KEYS},
    "Touchpad": {key: key for key in KEYS},
}

DICTIONARIES_ROOT = "asset:plover:assets"
DEFAULT_DICTIONARIES = ()
