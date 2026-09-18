import displayio
import terminalio
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle

brightnessImg = displayio.OnDiskBitmap("images/brightnessImg.bmp")
volumeImg = displayio.OnDiskBitmap("images/volumeImg.bmp")
playIconImg = displayio.OnDiskBitmap("images/playIconImg.bmp")
pauseIconImg = displayio.OnDiskBitmap("images/pauseIconImg.bmp")


Default = displayio.Group()


volumeBarOutline = Rect(4, 10, 7, 51, outline=0xFFFFFF)
Default.append(volumeBarOutline)
volumeBarFill = Rect(5, 11, 5, 49, fill=0xFFFFFF, outline=0xFFFFFF)
Default.append(volumeBarFill)
brightnessBarOutline = Rect(117, 10, 7, 51, outline=0xFFFFFF)
Default.append(brightnessBarOutline)
brightnessBarFill = Rect(118, 49, 5, 12, fill=0xFFFFFF, outline=0xFFFFFF)
Default.append(brightnessBarFill)
image_Volup_tile = displayio.TileGrid(
    volumeImg, pixel_shader=volumeImg.pixel_shader, position=(3, 2)
)
Default.append(image_Volup_tile)
image_imgbitmap_png_tile = displayio.TileGrid(
    brightnessImg,
    pixel_shader=brightnessImg.pixel_shader,
    position=(117, 2),
)
Default.append(image_imgbitmap_png_tile)
timeString = label.Label(terminalio.FONT, text="88:88", color=0xFFFFFF)
timeString.x = 21
timeString.y = 32
timeString.scale = 2
Default.append(timeString)
timeSuffixString = label.Label(terminalio.FONT, text="AM", color=0xFFFFFF)
timeSuffixString.x = 83
timeSuffixString.y = 32
timeSuffixString.scale = 2
Default.append(timeSuffixString)


def updateTimeDefault(time, suffix):
    timeString.text = time
    timeSuffixString.text = suffix


def updateVolumeDefault(percent):
    h = int(49 / 100 * percent)
    volumeBarFill.height = h
    volumeBarFill.y = 60 - h
    if h == 0:
        volumeBarFill.fill = 0x000000
        volumeBarFill.outline = 0x000000
    else:
        volumeBarFill.fill = 0xFFFFFF
        volumeBarFill.outline = 0xFFFFFF


def updateBrightnessDefault(percent):
    h = int(49 / 100 * percent)
    brightnessBarFill.height = h
    brightnessBarFill.y = 60 - h
    if h == 0:
        brightnessBarFill.fill = 0x000000
        brightnessBarFill.outline = 0x000000
    else:
        brightnessBarFill.fill = 0xFFFFFF
        brightnessBarFill.outline = 0xFFFFFF


media = displayio.Group()


volumeBarOutline = Rect(4, 10, 7, 51, outline=0xFFFFFF)
media.append(volumeBarOutline)
volumeBarFillMedia = Rect(4, 49, 7, 12, fill=0xFFFFFF, outline=0xFFFFFF)
media.append(volumeBarFillMedia)
brightnessBarOutline = Rect(117, 10, 7, 51, outline=0xFFFFFF)
media.append(brightnessBarOutline)
brightnessBarFillMedia = Rect(117, 49, 7, 12, fill=0xFFFFFF, outline=0xFFFFFF)
media.append(brightnessBarFillMedia)
image_Volup_tile = displayio.TileGrid(
    volumeImg, pixel_shader=volumeImg.pixel_shader, position=(3, 2)
)
media.append(image_Volup_tile)
image_imgbitmap_png_tile = displayio.TileGrid(
    brightnessImg,
    pixel_shader=brightnessImg.pixel_shader,
    position=(117, 2),
)
media.append(image_imgbitmap_png_tile)
timeStringMedia = label.Label(terminalio.FONT, text="88:88", color=0xFFFFFF)
timeStringMedia.x = 42
timeStringMedia.y = 11
media.append(timeStringMedia)
timeSuffixStringMedia = label.Label(terminalio.FONT, text="AM", color=0xFFFFFF)
timeSuffixStringMedia.x = 74
timeSuffixStringMedia.y = 11
media.append(timeSuffixStringMedia)
string_17 = label.Label(terminalio.FONT, text="Current", color=0xFFFFFF)
string_17.x = 42
string_17.y = 31
media.append(string_17)
mediaBarOutline = Rect(21, 54, 86, 5, outline=0xFFFFFF)
media.append(mediaBarOutline)
mediaBarFill = Rect(21, 55, 21, 4, fill=0xFFFFFF, outline=0xFFFFFF)
media.append(mediaBarFill)
mediaCircle = Circle(41, 56, 4, fill=0xFFFFFF, outline=0xFFFFFF)
media.append(mediaCircle)
image_music_play_tile = displayio.TileGrid(
    pauseIconImg,
    pixel_shader=playIconImg.pixel_shader,
    position=(61, 42),
)
media.append(image_music_play_tile)


def setPlaying(playing):
    if playing:
        image_music_play_tile.bitmap = pauseIconImg
    else:
        image_music_play_tile.bitmap = playIconImg


def updateTimeMedia(time, suffix):
    timeStringMedia.text = time
    timeSuffixStringMedia.text = suffix


def updateVolumeMedia(percent):
    h = int(49 / 100 * percent)
    volumeBarFillMedia.height = h
    volumeBarFillMedia.y = 60 - h
    if h == 0:
        volumeBarFillMedia.fill = 0x000000
        volumeBarFillMedia.outline = 0x000000
    else:
        volumeBarFillMedia.fill = 0xFFFFFF
        volumeBarFillMedia.outline = 0xFFFFFF


def updateBrightnessMedia(percent):
    h = int(49 / 100 * percent)
    brightnessBarFillMedia.height = h
    brightnessBarFillMedia.y = 60 - h
    if h == 0:
        brightnessBarFillMedia.fill = 0x000000
        brightnessBarFillMedia.outline = 0x000000
    else:
        brightnessBarFillMedia.fill = 0xFFFFFF
        brightnessBarFillMedia.outline = 0xFFFFFF
