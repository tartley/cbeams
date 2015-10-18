
def render(terminal, shape):
    return ''.join(
        terminal.move(y, x) + ' ' * length
        for y, x, length in shape.strips
    )

