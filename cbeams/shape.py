from math import sqrt, trunc

def rect(y1, x1, y2, x2):
    '''
    Given rectangle corners top left (y1, x1) to botto right (y2, x2) (incl),
    returns that rectangle as a series of horizontal strips.
    e.g. rect(0, 1, 2, 3) gives:
    [
        (0, 1, 3),
        (1, 1, 3),
        (2, 1, 3),
    ]
    i.e:
         x
         01234
      y 0 ###
        1 ###
        2 ###
    '''
    if y1 > y2:
        raise ValueError('{}(y1) > {}(y2)'.format(y1, y2))
    if x1 > x2:
        raise ValueError('{}(x1) > {}(x2)'.format(x1, x2))
    return Shape([
        (y, x1, x2 - x1 + 1)
        for y in range(y1, y2 + 1)
    ])

def disc(y, x, radius):
    '''
    Given a filled disc of int center (y, x) and float radius,
    returns that disc as a series of horizontal strips.
    Fractional parts of radius do make a visible difference.
    '''
    if radius < 0:
        raise ValueError('radius ({}) must be >0'.format(radius))
    elif radius == 0:
        strips = []
    else:
        strips = []
        for yoffset in range(-trunc(radius), trunc(radius) + 1):
            height = radius + yoffset
            xoffset = sqrt((radius - height / 2) * 2 * height)
            strips.append((
                y + yoffset,
                x - trunc(xoffset),
                trunc(xoffset) * 2 + 1
            ))
    return Shape(strips)

class Shape():
    '''
    Stores the geometry of a shape as a sequence of horizontal strips:
        [(x, y, length)... ]
    '''
    def __init__(self, strips):
        self.strips = strips

