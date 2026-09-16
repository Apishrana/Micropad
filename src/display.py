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
brightnessBarOutline = Rect(117, 10, 7, 51, outline=0xFFFFFF)
Default.append(brightnessBarOutline)
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
volumeBarFill = Rect(4, 49, 7, 12, fill=0xFFFFFF, outline=0xFFFFFF)
Default.append(volumeBarFill)
brightnessBarFill = Rect(117, 49, 7, 12, fill=0xFFFFFF, outline=0xFFFFFF)
Default.append(brightnessBarFill)


mediaPlay = displayio.Group()


volumeBarOutline = Rect(4, 10, 7, 51, outline=0xFFFFFF)
mediaPlay.append(volumeBarOutline)
brightnessBarOutline = Rect(117, 10, 7, 51, outline=0xFFFFFF)
mediaPlay.append(brightnessBarOutline)
image_Volup_tile = displayio.TileGrid(
    volumeImg, pixel_shader=volumeImg.pixel_shader, position=(3, 2)
)
mediaPlay.append(image_Volup_tile)
image_imgbitmap_png_tile = displayio.TileGrid(
    brightnessImg,
    pixel_shader=brightnessImg.pixel_shader,
    position=(117, 2),
)
mediaPlay.append(image_imgbitmap_png_tile)
timeString = label.Label(terminalio.FONT, text="88:88", color=0xFFFFFF)
timeString.x = 42
timeString.y = 11
mediaPlay.append(timeString)
timeSuffixString = label.Label(terminalio.FONT, text="AM", color=0xFFFFFF)
timeSuffixString.x = 74
timeSuffixString.y = 11
mediaPlay.append(timeSuffixString)
volumeBarFill = Rect(4, 49, 7, 12, fill=0xFFFFFF, outline=0xFFFFFF)
mediaPlay.append(volumeBarFill)
brightnessBarFill = Rect(117, 49, 7, 12, fill=0xFFFFFF, outline=0xFFFFFF)
mediaPlay.append(brightnessBarFill)
string_17 = label.Label(terminalio.FONT, text="Current", color=0xFFFFFF)
string_17.x = 42
string_17.y = 31
mediaPlay.append(string_17)
mediaBarOutline = Rect(21, 54, 86, 5, outline=0xFFFFFF)
mediaPlay.append(mediaBarOutline)
mediaBarFill = Rect(21, 55, 21, 4, fill=0xFFFFFF, outline=0xFFFFFF)
mediaPlay.append(mediaBarFill)
mediaCircle = Circle(41, 56, 4, fill=0xFFFFFF, outline=0xFFFFFF)
mediaPlay.append(mediaCircle)
image_music_play_tile = displayio.TileGrid(
    playIconImg,
    pixel_shader=playIconImg.pixel_shader,
    position=(61, 42),
)
mediaPlay.append(image_music_play_tile)


mediaPause = displayio.Group()


volumeBarOutline = Rect(4, 10, 7, 51, outline=0xFFFFFF)
mediaPause.append(volumeBarOutline)
brightnessBarOutline = Rect(117, 10, 7, 51, outline=0xFFFFFF)
mediaPause.append(brightnessBarOutline)
image_Volup_tile = displayio.TileGrid(
    volumeImg, pixel_shader=volumeImg.pixel_shader, position=(3, 2)
)
mediaPause.append(image_Volup_tile)
image_imgbitmap_png_tile = displayio.TileGrid(
    brightnessImg,
    pixel_shader=brightnessImg.pixel_shader,
    position=(117, 2),
)
mediaPause.append(image_imgbitmap_png_tile)
timeString = label.Label(terminalio.FONT, text="88:88", color=0xFFFFFF)
timeString.x = 42
timeString.y = 11
mediaPause.append(timeString)
timeSuffixString = label.Label(terminalio.FONT, text="AM", color=0xFFFFFF)
timeSuffixString.x = 74
timeSuffixString.y = 11
mediaPause.append(timeSuffixString)
volumeBarFill = Rect(4, 49, 7, 12, fill=0xFFFFFF, outline=0xFFFFFF)
mediaPause.append(volumeBarFill)
brightnessBarFill = Rect(117, 49, 7, 12, fill=0xFFFFFF, outline=0xFFFFFF)
mediaPause.append(brightnessBarFill)
string_17 = label.Label(terminalio.FONT, text="Current", color=0xFFFFFF)
string_17.x = 42
string_17.y = 31
mediaPause.append(string_17)
mediaBarOutline = Rect(21, 54, 86, 5, outline=0xFFFFFF)
mediaPause.append(mediaBarOutline)
mediaBarFill = Rect(21, 55, 21, 4, fill=0xFFFFFF, outline=0xFFFFFF)
mediaPause.append(mediaBarFill)
mediaCircle = Circle(41, 56, 4, fill=0xFFFFFF, outline=0xFFFFFF)
mediaPause.append(mediaCircle)
image_music_play_tile = displayio.TileGrid(
    pauseIconImg,
    pixel_shader=pauseIconImg.pixel_shader,
    position=(61, 42),
)
mediaPause.append(image_music_play_tile)
