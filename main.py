from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.capsword import CapsWord
from kmk.modules.combos import Chord, Combos
from kmk.modules.holdtap import HoldTap, HoldTapRepeat
from kmk.modules.layers import Layers

from kb import KMKKeyboard

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.extensions.append(MediaKeys())
combos = Combos()
keyboard.modules.append(combos)
caps_word = CapsWord()
keyboard.modules.append(caps_word)


combos.combos = [
    Chord((KC.Q, KC.W), KC.ESC),
]


TAP_TIME = 250

VOLD = KC.VOLD
VOLU = KC.VOLU
VVVV = KC.TRNS
____ = KC.NO

HOLDTAP_OPT = dict(
    prefer_hold=True,
    tap_interrupted=True,
    tap_time=TAP_TIME,
    repeat=HoldTapRepeat.TAP,
)

TAB = KC.HT(KC.TAB, KC.LGUI, **HOLDTAP_OPT)
Z_L3 = KC.LT(3, KC.Z, **HOLDTAP_OPT)
BSPC = KC.LT(1, KC.BSPC, **HOLDTAP_OPT)
J_SFT = KC.HT(KC.J, KC.RSFT, **HOLDTAP_OPT)
F_SFT = KC.HT(KC.F, KC.LSFT, **HOLDTAP_OPT)
A_CTL = KC.HT(KC.A, KC.LCTL, **HOLDTAP_OPT)
S_NAV = KC.LT(2, KC.S, **HOLDTAP_OPT)
L_NUM = KC.LT(2, KC.L, **HOLDTAP_OPT)
K_GUI = KC.HT(KC.K, KC.RGUI, **HOLDTAP_OPT)
D_GUI = KC.HT(KC.D, KC.LGUI, **HOLDTAP_OPT)
G_OPT = KC.HT(KC.G, KC.LALT, **HOLDTAP_OPT)
H_OPT = KC.HT(KC.H, KC.RALT, **HOLDTAP_OPT)
SPACE = KC.LT(2, KC.SPACE, **HOLDTAP_OPT)
ENTER = KC.HT(KC.ENTER, KC.LGUI, **HOLDTAP_OPT)
SLSH_L3 = KC.LT(3, KC.SLSH, **HOLDTAP_OPT)
SCLN_CTL = KC.HT(KC.SCLN, KC.RCTL, **HOLDTAP_OPT)


# fmt: off
keyboard.keymap = [
 [
 #--------+--------+--------+--------+--------+******+--------+--------+--------+--------+-------#
  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,           KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
  A_CTL,   S_NAV,   D_GUI,   F_SFT,   G_OPT,          H_OPT,   J_SFT,   K_GUI,   L_NUM,   SCLN_CTL,
  Z_L3,    KC.X,    KC.C,    KC.V,    KC.B,           KC.N,    KC.M,    KC.COMM, KC.DOT,  SLSH_L3,
 #--------+--------+--------+--------+--------+******+--------+--------+--------+--------+-------#
  ____,    ____,    VOLD,    ENTER,   SPACE,          BSPC,    TAB,     VOLU,    ____,    ____,
 ],
 # symbols
 [
 #--------+--------+--------+--------+--------+______+--------+--------+--------+--------+-------#
  KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC,        KC.CIRC, KC.AMPR, KC.ASTR, ____,    ____,
  KC.MINS, KC.UNDS, KC.GRV,  KC.QUOT, KC.DQT,         KC.COLN, KC.LPRN, KC.RPRN, KC.LBRC, KC.RBRC,
  KC.BSLS, KC.PIPE, KC.TILD, KC.EQL,  KC.PLUS,        KC.LBRC, KC.RBRC, KC.LABK, KC.RABK, KC.QUES,
 #--------+--------+--------+--------+--------+______+--------+--------+--------+--------+-------#
  ____,    ____,    VVVV,    VVVV,    VVVV,           VVVV,    VVVV,    VVVV,    ____,    ____,
 ],
 # numbers
 [
 #--------+--------+--------+--------+--------+______+--------+--------+--------+--------+-------#
  KC.N1,   KC.N2,   KC.N3,   KC.MINS, KC.ASTR,        ____,    ____,    ____,    ____,    KC.CW,
  KC.N4,   KC.N5,   KC.N6,   KC.PLUS, KC.SLSH,        KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, ____,
  KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.DOT,         KC.HOME, KC.PGDG, KC.PGUP, KC.END,  ____,
 #--------+--------+--------+--------+--------+______+--------+--------+--------+--------+-------#
  ____,    ____,    VVVV,    VVVV,    VVVV,           VVVV,    VVVV,    VVVV,    ____,    ____,
 ],
 [
 #--------+--------+--------+--------+--------+______+--------+--------+--------+--------+-------#
  ____,    ____,    ____,    ____,    ____,           ____,    ____,    ____,    ____,    ____,
  KC.CW,   ____,    ____,    ____,    ____,           ____,    ____,    ____,    ____,    ____,
  ____,    ____,    ____,    ____,    ____,           ____,    ____,    ____,    ____,    ____,
 #--------+--------+--------+--------+--------+______+--------+--------+--------+--------+-------#
  ____,    ____,    VVVV,    VVVV,    VVVV,           VVVV,    VVVV,    VVVV,    ____,    ____,
 ],
]
# fmt: on

if __name__ == "__main__":
    keyboard.go()
