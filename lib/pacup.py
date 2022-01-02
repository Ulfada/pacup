#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

from .middleware import create_parser
from .util.output import PacupUserError

def main():
    parser, middleware = create_parser()

    # bash autocompletion
    try:
        import argcomplete
        argcomplete.autocomplete(parser)
    except ImportError:
        pass

    # get cli arguments
    args = parser.parse_args()

    # run handler for a given subcommand (see https://docs.python.org/3/library/argparse.html#the-add-argument-method)
    if hasattr(args, "handler"):
        try:
            for f in middleware:
                f(args)
            args.handler(args)
        except PacupUserError as e:
            print(e)
    else:
        parser.print_help()
