import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.combos import Chord, Combos, Sequence
from kmk.modules.holdtap import HoldTapRepeat
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.scanners import DiodeOrientation

TAP_TIME = 200
NONE = KC.NO

combos = Combos()
keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())
keyboard.modules.append(combos)

HOLDTAP_OPTIONS = {
    "prefer_hold": False,
    "tap_interrupted": False,
    "tap_time": TAP_TIME,
    "repeat": HoldTapRepeat.TAP,
}
SHIFT_OPTIONS = {
    "prefer_hold": True,
    "tap_interrupted": False,
    "tap_time": 3000,
    "repeat": HoldTapRepeat.TAP,
}

combos.combos = [
    Chord((KC.R, KC.T), KC.BSPC),
    Chord((KC.Q, KC.W), KC.ESC),
    Chord((KC.A, KC.B, KC.C), KC.LALT),
    Chord((0, 1), KC.ESC, match_coord=True),
    Chord((8, 9, 10), KC.MO(4), match_coord=True),
    Sequence((KC.LEADER, KC.A, KC.B), KC.C),
    Sequence(
        (KC.E, KC.F), KC.MYKEY, timeout=500, per_key_timeout=False, fast_reset=False
    ),
]

CTL_A = KC.MT(KC.A, KC.LCTRL, *HOLDTAP_OPTIONS)
CTL_SEMI = KC.MT(KC.SEMI, KC.RCTRL, *HOLDTAP_OPTIONS)

ALT_TAB = KC.MT(KC.TAB, KC.ALT, *HOLDTAP_OPTIONS)
ALT_G = KC.MT(KC.G, KC.ALT, *HOLDTAP_OPTIONS)
ALT_H = KC.MT(KC.H, KC.ALT, *HOLDTAP_OPTIONS)

SFT_F = KC.MT(KC.F, KC.LSFT, *SHIFT_OPTIONS)
SFT_J = KC.MT(KC.J, KC.RSFT, *SHIFT_OPTIONS)

NUM_SPC = KC.LT(2, KC.SPACE, *HOLDTAP_OPTIONS)
NUM_S = KC.LT(2, KC.SPACE, *HOLDTAP_OPTIONS)
NUM_L = KC.LT(2, KC.SPACE, *HOLDTAP_OPTIONS)

CMD_ENT = KC.MT(KC.ENTER, KC.LGUI, *HOLDTAP_OPTIONS)
CMD_S = KC.MT(KC.S, KC.LGUI, *HOLDTAP_OPTIONS)
CMD_K = KC.MT(KC.K, KC.RGUI, *HOLDTAP_OPTIONS)

SYM_BSPC = KC.LT(1, KC.BACKSPACE, *HOLDTAP_OPTIONS)

# fmt: off
BASE = [ # QWERTY
  KC.Q,  KC.W,  KC.E,     KC.R,    KC.T,     KC.Y,     KC.U,     KC.I,    KC.O,   KC.P,
  CTL_A, NUM_S, CMD_S,    SFT_F,   ALT_G,    ALT_H,    SFT_J,    CMD_K,   NUM_L,  CTL_SEMI,
  KC.Z,  KC.X,  KC.C,     KC.V,    KC.B,     KC.N,     KC.M,     KC.COMM, KC.DOT, KC.SLSH,
  NONE,  NONE,  KC.LALT,  CMD_ENT, NUM_SPC,  SYM_BSPC, ALT_TAB,  KC.RALT, NONE,   NONE,
]
SYMBOLS = [ # Symbols
  KC.EXLM,  KC.AT,    KC.HASH,  KC.DLR,   KC.PERC,  KC.CARET, KC.AMPS, KC.STAR, NONE,    NONE,
  KC.MINUS, KC.UNDER, KC.GRAVE, KC.SQT,   KC.DQT,   KC.COLN,  KC.LPAR, KC.RPAR, KC.LBKT, KC.RBKT,
  KC.BSLH,  KC.PIPE,  KC.TILDE, KC.EQUAL, KC.PLUS,  KC.LBRC,  KC.RBRC, KC.LT, 	KC.GT,   KC.QMARK,
  NONE,     NONE,     NONE,     KC.ENTER, KC.SPACE, KC.BSPC,  KC.TAB,  NONE,    NONE,    NONE,
]
NUMBERS = [ # Numbers
  KC.EXLM,  KC.AT,  KC.HASH,     KC.DLR,    KC.PERC,     KC.CIRC,    KC.AMPR,     KC.ASTR,    KC.LPRN,   KC.RPRN,
  KC.ESC,  KC.TRNS,  KC.TRNS,     KC.TRNS,    KC.TRNS,     KC.TRNS,    KC.UNDS,     KC.PLUS,    KC.LCBR,   KC.RCBR,
  KC.CAPS,  KC.TILDE,  KC.TRNS,     KC.TRNS,    KC.TRNS,     KC.TRNS,    KC.TRNS,     KC.TRNS, KC.PIPE, KC.COLN,
  KC.NO, KC.NO, KC.TRNS,     ADJUST,    KC.TRNS, KC.ENTER, KC.TRNS,     KC.DEL,    KC.NO,  KC.NO,
]
ADJUST = [ # ADJUST
  KC.F1,  KC.F2,  KC.F3,     KC.F4,    KC.F5,     KC.F6,    KC.F7,     KC.F8,    KC.F9,   KC.F10,
  KC.F11,  KC.F12,  KC.TRNS,     KC.TRNS,    KC.TRNS,     KC.TRNS,    KC.TRNS,     CAE,    CAD,   CAD,
  KC.TRNS,  KC.TRNS,  KC.TRNS,     KC.TRNS,    KC.TRNS,     KC.TRNS,    KC.TRNS,     KC.TRNS, KC.TRNS, KC.TRNS,
  KC.NO, KC.NO, KC.TRNS,     KC.TRNS,    KC.TRNS, KC.ENTER, KC.TRNS,     KC.TRNS,    KC.NO,  KC.NO,
]
# fmt: on
keyboard.keymap = [BASE, SYMBOLS, NUMBERS, ADJUST]

# Uncomment for Trackball
# from kmk.modules.pimoroni_trackball import Trackball, TrackballMode
# import busio as io

# i2c1 = io.I2C(scl=board.GP3, sda=board.GP2)
# trackball = Trackball(i2c1, mode=TrackballMode.MOUSE_MODE)
# keyboard.modules.append(trackball)
# trackball.set_rgbw(255, 255, 255, 30)
# trackball.set_red(20)
# trackball.set_green(100)
# trackball.set_blue(100)
# trackball.set_white(40)

# uncomment for Encoders
# from kmk.modules.encoder import EncoderHandler
# encoder_handler = EncoderHandler()
# keyboard.modules = [encoder_handler]
# encoder_handler.pins = ((board.GP12, board.GP13, None, False), (board.GP27, board.GP26, None, False),)

# encoder_handler.map = [(( KC.VOLD, KC.VOLU),(KC.VOLD, KC.VOLU),), # Layer 1
#                      ((KC.VOLD, KC.VOLU),(KC.VOLD, KC.VOLU),), # Layer 2
#                      ((KC.VOLD, KC.VOLU),(KC.VOLD, KC.VOLU),), # Layer 3
#                      ((KC.VOLD, KC.VOLU),(KC.VOLD, KC.VOLU),), # Layer 4
#                      ]

# keyboard.debug_enabled = True

if __name__ == "__main__":
    keyboard.go()
