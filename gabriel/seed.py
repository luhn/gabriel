"""
This file deals with constructing the website heirarchy.
"""

import os
import os.path
from page import Page


def generate_tree(directory):
    """Take a directory and generate a tree of ``Page`` objects."""

    # Find the index file and create the root
    fn = os.path.join(directory, 'index.html')
    name = os.path.split(directory)[-1]
    try:
        root = Page(name, fn)
    except IOError:
        raise IOError('Could not find `%s`.' % fn)

    # Iterate through the directory and create all the other pages.
    for item in os.listdir(directory):
        if os.path.basename(item)[0] == '.': # Ignore hidden files
            continue
        fn = os.path.join(directory, item)
        # If it's a directory, put on my recursion shoes.
        if os.path.isdir(fn):
            root[item] = generate_tree(fn)
        else:
            name = '.'.join(os.path.basename(fn).split('.')[:-1])
            if name == 'index': # Ignore index file, we've already done that.
                continue
            root[item] = Page(name, fn)

    return root

