VERSION = "1.0.0"
SEPARATOR_TIMES = 63
SEPARATOR_LINE = "-" * SEPARATOR_TIMES


FIRST_ICON_CROP = {
    "left": 52,
    "top": 29,
    "right": 90,
    "bottom": 67
}
SECOND_ICON_CROP = {
    "left": 196,
    "top": 29,
    "right": 234,
    "bottom": 67
    
}
THIRD_ICON_CROP = {
    "left": 270,
    "top": 29,
    "right": 309,
    "bottom": 67
}
DIALOGUE_CROP = {
    "left": 947,
    "top": 1031,
    "right": 973,
    "bottom": 1057
}

FIRST_ICON_REGION = (FIRST_ICON_CROP["left"], FIRST_ICON_CROP["top"], FIRST_ICON_CROP["right"], FIRST_ICON_CROP["bottom"])
SECOND_ICON_REGION = (SECOND_ICON_CROP["left"], SECOND_ICON_CROP["top"], SECOND_ICON_CROP["right"], SECOND_ICON_CROP["bottom"])
THIRD_ICON_REGION = (THIRD_ICON_CROP["left"], THIRD_ICON_CROP["top"], THIRD_ICON_CROP["right"], THIRD_ICON_CROP["bottom"])
DIALOGUE_REGION = (DIALOGUE_CROP["left"], DIALOGUE_CROP["top"], DIALOGUE_CROP["right"], DIALOGUE_CROP["bottom"])

FIRST_ICON_PIXELS_SCREEN = {
    "first": (55, 47),
    "second": (87, 47),
}
SECOND_ICON_PIXELS_SCREEN = {
    "first": (199, 47),
    "second": (231, 47),
}
THIRD_ICON_PIXELS_SCREEN = {
    "first": (273, 47),
    "second": (305, 47),
}
DIALOGUE_ICON_PIXELS_SCREEN = {
    "first": (960, 1029),
    "second": (960, 1048),
}

FLOUR_COLOR = (236, 229, 216)
AMBER_COLOR = (255, 186, 3)

FLOUR_COLOR_BGR = FLOUR_COLOR[::-1]
AMBER_COLOR_BGR = AMBER_COLOR[::-1]

LEFT, TOP = FIRST_ICON_CROP["left"], FIRST_ICON_CROP["top"]
RIGHT, BOTTOM = DIALOGUE_CROP["right"], DIALOGUE_CROP["bottom"]
REGION = (LEFT, TOP, RIGHT, BOTTOM)

MSS_REGION = {
    "top": TOP,
    "left": LEFT,
    "width": RIGHT - LEFT,
    "height": BOTTOM - TOP
}

FIRST_ICON_PIXELS_CROP = {
    "first": (FIRST_ICON_PIXELS_SCREEN["first"][0] - LEFT, FIRST_ICON_PIXELS_SCREEN["first"][1] - TOP),
    "second": (FIRST_ICON_PIXELS_SCREEN["second"][0] - LEFT, FIRST_ICON_PIXELS_SCREEN["second"][1] - TOP),
}
SECOND_ICON_PIXELS_CROP = {
    "first": (SECOND_ICON_PIXELS_SCREEN["first"][0] - LEFT, SECOND_ICON_PIXELS_SCREEN["first"][1] - TOP),
    "second": (SECOND_ICON_PIXELS_SCREEN["second"][0] - LEFT, SECOND_ICON_PIXELS_SCREEN["second"][1] - TOP),
}
THIRD_ICON_PIXELS_CROP = {
    "first": (THIRD_ICON_PIXELS_SCREEN["first"][0] - LEFT, THIRD_ICON_PIXELS_SCREEN["first"][1] - TOP),
    "second": (THIRD_ICON_PIXELS_SCREEN["second"][0] - LEFT, THIRD_ICON_PIXELS_SCREEN["second"][1] - TOP),
}
DIALOGUE_ICON_PIXELS_CROP = {
    "first": (DIALOGUE_ICON_PIXELS_SCREEN["first"][0] - LEFT, DIALOGUE_ICON_PIXELS_SCREEN["first"][1] - TOP),
    "second": (DIALOGUE_ICON_PIXELS_SCREEN["second"][0] - LEFT, DIALOGUE_ICON_PIXELS_SCREEN["second"][1] - TOP),
}