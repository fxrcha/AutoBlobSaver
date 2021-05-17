from optparse import OptionParser


def option_parser():
    parser = OptionParser(usage="usage: $prog [options]")

    parser.add_option(
        "--debug",
        "--verbose",
        help="print verbose things",
        action="store_true",
        dest="debug",
    )

    parser.add_option(
        "--path",
        help="override path to save SHSH2 blob files",
        dest="save_path",
        default=None,
        type=str,
    )

    parser.add_option(
        "--time",
        help="override refresh time to check new IPSW (in seconds, default: 6 hours - 21600)",
        dest="time",
        default=None,
        type=int,
    )

    return parser
