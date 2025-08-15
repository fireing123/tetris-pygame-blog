INDEX = ['I', 'O', 'T', 'S', 'Z', 'J', 'L']

COLORS = {
    'I': (0, 186, 255),
    'O': (255, 207, 0),
    'T': (208, 80, 255),
    'S': (0, 214, 120),
    'Z': (255, 75, 85),
    'J': (70, 120, 255),
    'L': (255, 160, 40),
}

SIZE = 40

SHAPES = {
    'I': [
        [False, False, False, False],
        [True,  True,  True,  True ],
        [False, False, False, False],
        [False, False, False, False],
    ],
    'O': [
        [True,  True ],
        [True,  True ],
    ],
    'T': [
        [False, True,  False],
        [True,  True,  True ],
        [False, False, False],
    ],
    'S': [
        [False, True,  True ],
        [True,  True,  False],
        [False, False, False],
    ],
    'Z': [
        [True,  True,  False],
        [False, True,  True ],
        [False, False, False],
    ],
    'J': [
        [True,  False, False],
        [True,  True,  True ],
        [False, False, False],
    ],
    'L': [
        [False, False, True ],
        [True,  True,  True ],
        [False, False, False],
    ],
}
