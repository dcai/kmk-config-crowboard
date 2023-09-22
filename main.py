import board
from kb import KMKKeyboard
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.combos import Chord, Combos, Sequence
from kmk.modules.holdtap import HoldTap, HoldTapRepeat
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.extensions.append(MediaKeys())
combos = Combos()
keyboard.modules.append(combos)

combos.combos = [
    Chord((KC.Q, KC.W), KC.ESC),
    Chord((KC.M, KC.LABK), KC.VOLD),
    #  Chord((KC.RABK, KC.LABK), KC.VOLU),
]


XXXX = KC.NO
TAP_TIME = 250

HOLDTAP_OPT = dict(
    prefer_hold=True,
    tap_interrupted=True,
    tap_time=TAP_TIME,
    repeat=HoldTapRepeat.TAP,
)

J_SFT = KC.HT(KC.J, KC.RSFT, **HOLDTAP_OPT)
F_SFT = KC.HT(KC.F, KC.LSFT, **HOLDTAP_OPT)
A_CTL = KC.HT(KC.A, KC.LCTL, **HOLDTAP_OPT)
S_NAV = KC.LT(2, KC.S, **HOLDTAP_OPT)
L_NUM = KC.LT(2, KC.L, **HOLDTAP_OPT)
K_GUI = KC.HT(KC.K, KC.RGUI, **HOLDTAP_OPT)
D_GUI = KC.HT(KC.D, KC.LGUI, **HOLDTAP_OPT)
G_OPT = KC.HT(KC.G, KC.LALT, **HOLDTAP_OPT)
H_OPT = KC.HT(KC.H, KC.RALT, **HOLDTAP_OPT)
SLSH_SFT = KC.HT(KC.SLSH, KC.LSFT, **HOLDTAP_OPT)
SCLN_CTL = KC.HT(KC.SCLN, KC.RCTL, **HOLDTAP_OPT)

SPACE = KC.LT(2, KC.SPACE, **HOLDTAP_OPT)
ENTER = KC.HT(KC.ENTER, KC.LGUI, **HOLDTAP_OPT)
BSPC = KC.LT(1, KC.BSPC, **HOLDTAP_OPT)
TAB = KC.HT(KC.TAB, KC.LGUI, **HOLDTAP_OPT)

VOLD = KC.VOLD
VOLU = KC.VOLU
____ = KC.TRNS


# fmt: off
keyboard.keymap = [
 [
 #-----+------+------+------+------+------+------+------+--------+-------+--------#
 KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,         KC.Y,  KC.U,  KC.I,    KC.O,   KC.P,
 A_CTL, S_NAV, D_GUI, F_SFT, G_OPT,        H_OPT, J_SFT, K_GUI,   L_NUM,  SCLN_CTL,
 KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,         KC.N,  KC.M,  KC.COMM, KC.DOT, SLSH_SFT,
 #-----+------+------+------+------+______+------+------+--------+-------+--------#
 XXXX,  XXXX,  VOLD,  ENTER, SPACE,        BSPC,  TAB,   VOLU,    XXXX,   XXXX,
 ],
 # symbols
 [
 KC.EXLM, KC.AT,   KC.HASH, KC.DLR,   KC.PERC,      KC.CIRC, KC.AMPR, KC.ASTR, XXXX,    XXXX,
 KC.MINS, KC.UNDS, KC.GRV,  KC.QUOTE, KC.DQT,       KC.COLN, KC.LPRN, KC.RPRN, KC.LBRC, KC.RBRC,
 KC.BSLS, KC.PIPE, KC.TILD, KC.EQL,   KC.PLUS,      KC.LBRC, KC.RBRC, KC.LABK, KC.RABK, KC.QUES,
 #-------+--------+--------+---------+-------+_____+--------+--------+--------+--------+-------#
 XXXX,    XXXX,    ____,    ____,     ____,         ____,    ____,    ____,    XXXX,    XXXX,
 ],
 # numbers
 [
 KC.N1, KC.N2, KC.N3, KC.MINS, KC.ASTR,       XXXX,    XXXX,    XXXX,    XXXX,    XXXX,
 KC.N4, KC.N5, KC.N6, KC.PLUS, KC.SLSH,       KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, XXXX,
 KC.N7, KC.N8, KC.N9, KC.N0,   KC.DOT,        KC.HOME, KC.PGDG, KC.PGUP, KC.END,  XXXX,
 #-----+------+------+------+---------+______+--------+--------+--------+--------+----#
 XXXX,  XXXX,  ____,  ____,    ____,          ____,    ____,    ____,    XXXX,    XXXX,
 ],
]
# fmt: on

if __name__ == "__main__":
    keyboard.go()
