#!/usr/bin/env python3
import argparse
import importlib
import imp
import sys
from . import VERSION

def parse_arguments():
    """parsing arguments.

    """
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--platform', '-p', type=str, required=True)
    parser.add_argument('--version', action='version',
                        version=format(VERSION),
                        help='show the version number and exit')
    return parser.parse_args()

def main():
    """Entrypoint if called as an executable."""
    args = parse_arguments()
    try:
        platform = importlib.import_module(".lib.platform.%s.k8s" % args.platform,
                                           package="k8satt")
    except ImportError:
        print("ERROR: provider %s is not implemented" % args.platform)
        sys.exit(2)

    platform.create_cluster()

if __name__ == "__main__":
    main()
