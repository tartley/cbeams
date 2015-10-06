
class Shape():

    terminal = None

    def __init__(self, slivers):
        self.slivers = slivers

    def __str__(self):
        return ''.join(
            Shape.terminal.move(y, x) + ' ' * length
            for y, x, length in self.slivers
        )

    @staticmethod
    def rectfill(y1, x1, y2, x2):
        return Shape([
            (y, x1, x2 - x1)
            for y in range(y1, y2)
        ])

