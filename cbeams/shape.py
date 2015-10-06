import math

class Shape():

    terminal = None

    def __init__(self, strips):
        self.strips = strips

    def __str__(self):
        return ''.join(
            self.terminal.move(y, x) + ' ' * length
            for y, x, length in self.strips
        )

    @classmethod
    def RectFill(cls, y1, x1, y2, x2):
        '''
        A rectangle from top left (y1, x1), to bottom right (y2, x2), inclusive.
        Negative co-ords are interpretted from the right/bottom terminal edge.
        e.g. RectFill(0, 1, -1, -2) gives:
             x
             01234
          y 0 ###
            1 ###
            2 ###
        '''
        y1 %= cls.terminal.height
        y2 %= cls.terminal.height
        if y1 > y2:
            raise ValueError('{}(y1) > {}(y2)'.format(y1, y2))
        x1 %= cls.terminal.width
        x2 %= cls.terminal.width
        if x1 > x2:
            raise ValueError('{}(x1) > {}(x2)'.format(x1, x2))
        return Shape([
            (y, x1, x2 - x1 + 1)
            for y in range(y1, y2 + 1)
        ])

    def CircleFill(y, x, radius):
        '''
        A filled circle from an x,y center and radius.
        Radius may be given as a float, which will make a visible difference.
        '''
        result = []
        for yoffset in range(-radius + 1, radius):
            height = radius - yoffset
            xoffset = math.sqrt((radius - height / 2) * 2 * height)
            result.append((
                y + yoffset,
                x - round(xoffset - 0.5),
                round(xoffset - 0.5) * 2 + 1
            ))
        return Shape(result)

