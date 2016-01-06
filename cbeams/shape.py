from math import sqrt, trunc

def disc(y, x, radius):
    '''
    Given a filled disc of int center (y, x) and float radius,
    returns that disc as a series of horizontal strips.
    Fractional parts of radius do make a visible difference.
    '''
    if radius < 0:
        raise ValueError('radius ({}) must be >0'.format(radius))
    elif radius == 0:
        return []
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
        return strips

