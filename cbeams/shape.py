from math import sqrt, trunc

def rect(y1, x1, y2, x2):
    '''
    A rectangle from top left (y1, x1), to bottom right (y2, x2), inclusive.
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

class Shape():
    '''
    Stores the geometry of a shape as a sequence of horizontal strips:
        [(x, y, length)... ]
    '''
    def __init__(self, strips):
        self.strips = strips

    @staticmethod
    def CircleFill(y, x, radius):
        '''
        A filled circle from an x,y center and radius.
        Radius may be a float, & fractional parts do make a visible difference.
        See tests for precise shape of some small-radius circles.
        '''
        if radius < 0:
            raise ValueError('radius ({}) must be >0'.format(radius))
        elif radius == 0:
            slices = []
        else:
            slices = []
            for yoffset in range(-trunc(radius), trunc(radius) + 1):
                height = radius + yoffset
                xoffset = sqrt((radius - height / 2) * 2 * height)
                slices.append((
                    y + yoffset,
                    x - trunc(xoffset),
                    trunc(xoffset) * 2 + 1
                ))
        return Shape(slices)

