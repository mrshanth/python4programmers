from __future__ import print_function
from IPython.display import Image, HTML

__all__ = ['guido_van_rossum', 'what_is_python']


def guido_van_rossum():
    print("https://www.python.org/~guido/")
    print("Benevolent dictator for life (BDFL)")
    print("Google -> Dropbox")
    return Image(
        'http://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Guido_van_Rossum_OSCON_2006.jpg/250px-Guido_van_Rossum_OSCON_2006.jpg')


def what_is_python():
    python_properties = ('high-level', 'interpreted', 'dynamic typed', 'strongly typed', 'multi-paradigm', 'everything is an object',
                         'whitespace to delimit program blocks')
    return HTML("<ul>" + "\n".join(["<li>{0}</li>".format(p) for p in python_properties]) + "</ul>")


def foo():
    print('bar')
