from docopt import docopt

from . import __doc__ as root_doc, __version__ as version

def parse(args):
    return docopt(
        root_doc.format(version=version),
        argv=args,
        version=version
    )

