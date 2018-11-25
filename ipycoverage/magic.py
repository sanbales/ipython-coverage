import logging
import os

try:
    import coverage
except ImportError:
    coverage = None

from IPython.display import IFrame
from IPython.core import magic, magic_arguments


if "sandbox" not in IFrame.iframe:
    IFrame.iframe = IFrame.iframe.replace(
        "allowfullscreen\n",
        "allowfullscreen\n"
        '            sandbox="allow-forms allow-same-origin allow-scripts"\n'
    )


@magic.magics_class
class CoverageMagic(magic.Magics):

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
        '--branch', '-b', action='store_false',
        help="Measure branch coverage in addition to statement coverage.",
    )
    @magic_arguments.argument(
        'statement', nargs='*',
        help="""Code call statement to include in the code coverage analysis. 
        You can omit this in cell magic mode.""",
    )
    @magic.line_cell_magic
    @magic.needs_local_scope
    def coverage(self, line="", cell=None, local_ns=None):
        """ Run coverage on a line or cell. """

        args = magic_arguments.parse_argstring(self.coverage, line)
        branch = args.branch

        code = "\n".join(args.statement)
        if cell:
            code += "\n" + cell

        if not code:
            return

        global_variables = self.shell.user_ns
        if local_ns is not None:
            conflict_globs = {}
            for var_name, var_val in global_variables.items():
                if var_name in local_ns:
                    conflict_globs[var_name] = var_val
            global_variables.update(local_ns)

        cov = coverage.Coverage(branch=branch)
        exception = None
        try:
            cov.start()
            exec(code, global_variables, {})
        except Exception as exc:
            logging.error(exc)
            exception = exc
        finally:
            cov.stop()

        if exception:
            return "Failed to run: \n%s\nBecause: %s" % (code, str(exception))

        cov.save()

        cov.html_report()
        # TODO: add options for IFrame display
        return IFrame(os.path.join("htmlcov/index.html"), width="100%", height=600)


def load_ipython_extension(ipython):
    """Load the extension in IPython."""
    ipython.register_magics(CoverageMagic)
