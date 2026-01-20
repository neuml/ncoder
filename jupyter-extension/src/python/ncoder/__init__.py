"""
NCoder imports
"""

from .ncoder import NCoder


def load_ipython_extension(ipython):
    """
    Loads the NCoder IPython extension.

    Args:
        ipython: ipython instance
    """

    ipython.register_magics(NCoder)
