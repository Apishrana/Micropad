import displayio
import terminalio
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle

image_imgbitmap_png_bits = displayio.OnDiskBitmap("/image_imgbitmap_png_bits.bmp")
image_Volup_bits = displayio.OnDiskBitmap("/image_Volup_bits.bmp")
image_music_play_bits = displayio.OnDiskBitmap("/image_music_play_bits.bmp")
image_music_pause_bits = displayio.OnDiskBitmap("/image_music_pause_bits.bmp")


Default = displayio.Group()


def drawDefault():
    rect_1 = Rect(4, 10, 7, 51, outline=0xFFFFFF)
    Default.append(rect_1)
    rect_1 = Rect(117, 10, 7, 51, outline=0xFFFFFF)
    Default.append(rect_1)
    image_Volup_tile = displayio.TileGrid(
        image_Volup_bits, pixel_shader=image_Volup_bits.pixel_shader, position=(3, 2)
    )
    Default.append(image_Volup_tile)
    image_imgbitmap_png_tile = displayio.TileGrid(
        image_imgbitmap_png_bits,
        pixel_shader=image_imgbitmap_png_bits.pixel_shader,
        position=(117, 2),
    )
    Default.append(image_imgbitmap_png_tile)
    string_5 = label.Label(terminalio.FONT, text="88:88", color=0xFFFFFF)
    string_5.x = 21
    string_5.y = 32
    string_5.scale = 2
    Default.append(string_5)
    string_6 = label.Label(terminalio.FONT, text="AM", color=0xFFFFFF)
    string_6.x = 83
    string_6.y = 32
    string_6.scale = 2
    Default.append(string_6)
    rect_7 = Rect(4, 48, 7, 12, fill=0xFFFFFF, outline=0xFFFFFF)
    Default.append(rect_7)
    rect_7 = Rect(117, 48, 7, 12, fill=0xFFFFFF, outline=0xFFFFFF)
    Default.append(rect_7)



media__play_icon_ = displayio.Group()


def drawmedia__play_icon_():
    rect_1 = Rect(4, 10, 7, 51, outline=0xFFFFFF)
    media__play_icon_.append(rect_1)
    rect_1 = Rect(117, 10, 7, 51, outline=0xFFFFFF)
    media__play_icon_.append(rect_1)
    image_Volup_tile = displayio.TileGrid(
        image_Volup_bits, pixel_shader=image_Volup_bits.pixel_shader, position=(3, 2)
    )
    media__play_icon_.append(image_Volup_tile)
    image_imgbitmap_png_tile = displayio.TileGrid(
        image_imgbitmap_png_bits,
        pixel_shader=image_imgbitmap_png_bits.pixel_shader,
        position=(117, 2),
    )
    media__play_icon_.append(image_imgbitmap_png_tile)
    string_5 = label.Label(terminalio.FONT, text="88:88", color=0xFFFFFF)
    string_5.x = 42
    string_5.y = 11
    media__play_icon_.append(string_5)
    string_6 = label.Label(terminalio.FONT, text="AM", color=0xFFFFFF)
    string_6.x = 74
    string_6.y = 11
    media__play_icon_.append(string_6)
    rect_7 = Rect(4, 48, 7, 12, fill=0xFFFFFF, outline=0xFFFFFF)
    media__play_icon_.append(rect_7)
    rect_7 = Rect(117, 48, 7, 12, fill=0xFFFFFF, outline=0xFFFFFF)
    media__play_icon_.append(rect_7)
    string_17 = label.Label(terminalio.FONT, text="Current", color=0xFFFFFF)
    string_17.x = 42
    string_17.y = 31
    media__play_icon_.append(string_17)
    rect_18 = Rect(21, 54, 86, 5, outline=0xFFFFFF)
    media__play_icon_.append(rect_18)
    rect_19 = Rect(21, 55, 21, 4, fill=0xFFFFFF, outline=0xFFFFFF)
    media__play_icon_.append(rect_19)
    circle_20 = Circle(41, 56, 4, fill=0xFFFFFF, outline=0xFFFFFF)
    media__play_icon_.append(circle_20)
    image_music_play_tile = displayio.TileGrid(
        image_music_play_bits,
        pixel_shader=image_music_play_bits.pixel_shader,
        position=(61, 42),
    )
    media__play_icon_.append(image_music_play_tile)


media__pause_icon_ = displayio.Group()


def drawmedia__pause_icon_():
    rect_1 = Rect(4, 10, 7, 51, outline=0xFFFFFF)
    media__pause_icon_.append(rect_1)
    rect_1 = Rect(117, 10, 7, 51, outline=0xFFFFFF)
    media__pause_icon_.append(rect_1)
    image_Volup_tile = displayio.TileGrid(
        image_Volup_bits, pixel_shader=image_Volup_bits.pixel_shader, position=(3, 2)
    )
    media__pause_icon_.append(image_Volup_tile)
    image_imgbitmap_png_tile = displayio.TileGrid(
        image_imgbitmap_png_bits,
        pixel_shader=image_imgbitmap_png_bits.pixel_shader,
        position=(117, 2),
    )
    media__pause_icon_.append(image_imgbitmap_png_tile)
    string_5 = label.Label(terminalio.FONT, text="88:88", color=0xFFFFFF)
    string_5.x = 42
    string_5.y = 11
    media__pause_icon_.append(string_5)
    string_6 = label.Label(terminalio.FONT, text="AM", color=0xFFFFFF)
    string_6.x = 74
    string_6.y = 11
    media__pause_icon_.append(string_6)
    rect_7 = Rect(4, 48, 7, 12, fill=0xFFFFFF, outline=0xFFFFFF)
    media__pause_icon_.append(rect_7)
    rect_7 = Rect(117, 48, 7, 12, fill=0xFFFFFF, outline=0xFFFFFF)
    media__pause_icon_.append(rect_7)
    string_17 = label.Label(terminalio.FONT, text="Current", color=0xFFFFFF)
    string_17.x = 42
    string_17.y = 31
    media__pause_icon_.append(string_17)
    rect_18 = Rect(21, 54, 86, 5, outline=0xFFFFFF)
    media__pause_icon_.append(rect_18)
    rect_19 = Rect(21, 55, 21, 4, fill=0xFFFFFF, outline=0xFFFFFF)
    media__pause_icon_.append(rect_19)
    circle_20 = Circle(41, 56, 4, fill=0xFFFFFF, outline=0xFFFFFF)
    media__pause_icon_.append(circle_20)
    image_music_play_tile = displayio.TileGrid(
        image_music_pause_bits,
        pixel_shader=image_music_pause_bits.pixel_shader,
        position=(61, 42),
    )
    media__pause_icon_.append(image_music_play_tile)
