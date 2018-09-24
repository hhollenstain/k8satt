#!/usr/bin/env python3
import argparse
import coloredlogs
import importlib
import imp
import logging
import sys
from . import VERSION

LOG = logging.getLogger(__name__)

def parse_arguments():
    """parsing arguments.

    """
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--platform', '-p', type=str, required=True)
    parser.add_argument('--debug', help='enable debug', action='store_true')
    parser.add_argument('--version', action='version',
                        version=format(VERSION),
                        help='show the version number and exit')
    return parser.parse_args()

def main():
    """Entrypoint if called as an executable."""
    print(__name__)
    args = parse_arguments()
    #k8tils.k8satt_logger(args.debug)
    logging.basicConfig(level=logging.INFO)
    coloredlogs.install(level=0, fmt="[%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d] %(message)s", isatty=True)
    if args.debug:
        l_level = logging.DEBUG
    else:
        l_level = logging.INFO
    logging.getLogger(__package__).setLevel(l_level)

    try:
        platform = importlib.import_module(".lib.platform.%s.k8s" % args.platform,
                                           package="k8satt")
    except ImportError:
        logging.error('provider %s is not implemented' % args.platform)
        sys.exit(2)


    platform.create_cluster()

if __name__ == "__main__":
    print(__name__)
    main()
