import logging
import sys

from cli import check_os, header, option_parser

if __name__ == "__main__":
    header()

    if not check_os():
        print("AutoBlobSaver only supports Macintosh & Linux systems.")
        exit(0)

    optparser = option_parser()
    (option, args) = optparser.parse_args(sys.argv)

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    else:
        logging.getLogger().setLevel(logging.INFO)

    if args.time is not None:
        time = int(args.time)

    else:
        time = 21600  # default to 6 hrs
