import logging

try:
    import coverage
except ImportError:
    coverage = None

from IPython import display
from IPython.core import (
    magic_arguments,
)
from IPython.core.magic import (
    Magics,
    magics_class,
    needs_local_scope,
    line_cell_magic,
)


@magics_class
class CoverageMagic(Magics):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if coverage is None:
            self.coverage = self.coverage_missing_notice
        # Default execution function used to actually run user code.
        self.default_runner = None

    @staticmethod
    def coverage_missing_notice(*args, **kwargs):
        logging.error("""\
The coverage module could not be found, install it by running
`pip install coverage`.""")

    @magic_arguments.magic_arguments()
    @magic_arguments.argument(
        '--branch', action='store_false',
        help="Measure branch coverage in addition to statement coverage.",
    )
    @magic_arguments.argument(
        '-i', '--ignore-errors', action='store_true',
        help="Ignore errors while reading source files.",
    )
    @magic_arguments.argument(
        'statement', nargs='*',
        help="""Code call statement to include in the code coverage analysis. 
        You can omit this in cell magic mode.""",
    )
    @line_cell_magic
    @needs_local_scope
    def coverage(self, line="", cell=None, local_ns=None):
        """ Run coverage on a line or cell. """

        args = magic_arguments.parse_argstring(self.coverage, line)
        branch = args.branch
        ignore_errors = args.ignore_errors

        code = "\n".join(args.statement)
        if cell:
            code += "\n" + cell

        if not code:
            return

        ns = {}
        glob = self.shell.user_ns
        # handles global vars with same name as local vars. We store them in conflict_globs.
        if local_ns is not None:
            conflict_globs = {}
            for var_name, var_val in glob.items():
                if var_name in local_ns:
                    conflict_globs[var_name] = var_val
            glob.update(local_ns)

        cov = coverage.Coverage(branch=branch)
        cov.start()

        exec(code, glob, ns)

        cov.stop()
        cov.save()
        try:
            cov.html_report()
            # TODO: make a tempfolder to store and read the HTML results from
            return display.IFrame("htmlcov/index.html", width="100%", height=600)
        except Exception as exc:
            logging.error(exc)
            return code


def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magics(CoverageMagic)
