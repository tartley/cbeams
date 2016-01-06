import collections
import itertools
import math

Strip = collections.namedtuple('Strip', 'y x length')

def _subtract_strip(strip, gap):
    return [
        Strip(strip.y, strip.x, gap.x - strip.x),
        Strip(
            strip.y,
            gap.x + gap.length,
            strip.x + strip.length - gap.x - gap.length
        ),
    ]

def _subtract_row(strips, gaps):
    assert len(strips) == 1, \
        'subtracting from complicated shapes not implemented'
    strip = strips[0]
    if len(gaps) == 0:
        return [strip]
    elif len(gaps) == 1:
        return _subtract_strip(strip, gaps[0])
    else:
        raise AssertionError('subtract of complicated holes not implemented.')

def subtract(shape, hole):
    '''
    Given two shapes, e.g. return values from 'disc' or 'annulus' below,
    return the new shape that results from subtracting one from t'other.
    '''
    return list(itertools.chain.from_iterable(
        _subtract_row(
            [strip for strip in shape if strip.y == yord],
            [strip for strip in hole  if strip.y == yord]
        )
        for yord in set(strip.y for strip in shape)
    ))


def disc(y, x, radius):
    '''
    Given a filled disc of int center (y, x) and float radius,
    returns that disc as a series of horizontal strips.
    Fractional parts of radius do make a visible difference.
    '''
    if radius < 0:
        raise ValueError('radius ({}) must be >0'.format(radius))
    if radius == 0:
        return []
    else:
        strips = []
        for yoffset in range(-math.trunc(radius), math.trunc(radius) + 1):
            height = radius + yoffset
            xoffset = math.sqrt((radius - height / 2) * 2 * height)
            strips.append(Strip(
                y + yoffset,
                x - math.trunc(xoffset),
                math.trunc(xoffset) * 2 + 1
            ))
        return strips

def annulus(y, x, outer, inner):
    '''
    Given an annulus of int center (y, x), with outer and inner float radii,
    return that shape as a series of horizontal strips.
    '''
    if outer < 0 or inner < 0:
        raise ValueError(
            'outer ({}) and inner ({}) must be >= 0'.format(outer, inner)
        )
    if outer < inner:
        raise ValueError(
            'outer ({}) should be >= inner ({})'.format(outer, inner)
        )
    return subtract(disc(y, x, outer), disc(y, x, inner))

