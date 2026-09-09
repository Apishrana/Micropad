import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())
macros = Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (board.GP6, board.GP7, board.GP0)
keyboard.row_pins = (board.GP26, board.GP27, board.GP28, board.GP29)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Macros

gpt = KC.MACRO(Press(KC.LALT), Tap(KC.SPACE), Release(KC.LALT))
terminal = KC.MACRO(
    Press(KC.LALT),
    Press(KC.LGUI),
    Press(KC.LCTRL),
    Tap(KC.T),
    Release(KC.LALT),
    Release(KC.LGUI),
    Release(KC.LCTRL),
)
radial = KC.MACRO(
    Press(KC.LALT),
    Press(KC.LGUI),
    Press(KC.LCTRL),
    Tap(KC.SPACE),
    Release(KC.LALT),
    Release(KC.LGUI),
    Release(KC.LCTRL),
)

undo = KC.MACRO(Press(KC.LGUI), Tap(KC.Z), Release(KC.LGUI))
redo = KC.MACRO(
    Press(KC.LGUI), Press(KC.LSHIFT), Tap(KC.Z), Release(KC.LGUI), Release(KC.LSHIFT)
)
save = KC.MACRO(Press(KC.LGUI), Tap(KC.S), Release(KC.LGUI))

cut = KC.MACRO(Press(KC.LGUI), Tap(KC.X), Release(KC.LGUI))
copy = KC.MACRO(Press(KC.LGUI), Tap(KC.C), Release(KC.LGUI))
paste = KC.MACRO(Press(KC.LGUI), Tap(KC.V), Release(KC.LGUI))


keyboard.keymap = [
    [
        gpt,
        terminal,
        radial,
        undo,
        redo,
        save,
        cut,
        copy,
        paste,
        KC.MPRV,
        KC.MPLY,
        KC.MNXT,
    ]
]

if __name__ == "__main__":
    keyboard.go()
