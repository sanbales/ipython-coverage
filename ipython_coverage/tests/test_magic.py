from unittest import TestCase

from IPython.testing.globalipapp import get_ipython

from .. import load_ipython_extension, unload_ipython_extension


class TestMagic(TestCase):
    """ A Test for the IPython Coverage cell and line magic. """

    def setUp(self):
        self.ipython = get_ipython()
        # self.ip.magic("load_ext ipycoverage")
        load_ipython_extension(self.ipython)

    def test_basics(self):
        self.ipython.run_line_magic("coverage", "import unittest")

    def tearDown(self):
        unload_ipython_extension(self.ipython)
