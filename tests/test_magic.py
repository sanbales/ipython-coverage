from unittest import TestCase

from IPython.testing.globalipapp import get_ipython

from ipycoverage.magic import load_ipython_extension


class TestMagic(TestCase):
    """ A Test for the IPython Coverage cell and line magic. """

    def setUp(self):
        self.ip = get_ipython()
        # self.ip.magic("load_ext ipycoverage")
        load_ipython_extension(self.ip)

    def test_basics(self):
        self.ip.run_line_magic("coverage", "import unittest")
