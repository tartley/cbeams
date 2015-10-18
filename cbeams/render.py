
def render(terminal, shape):
    return ''.join(
        terminal.move(y, x) + ' ' * length
        for y, x, length in shape.clipped(terminal.height, terminal.width)
        if length > 0
    )

