from IPython.core.getipython import get_ipython

from .magic import load_ipython_extension


load_ipython_extension(get_ipython())
