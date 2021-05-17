from optparse import OptionParser


def option_parser():
    parser = OptionParser(usage="usage: $prog [options]")

    parser.add_option(
        "--verbose",
        help="print verbose things",
        dest="debug",
        action="store_true",
    )

    parser.add_option(
        "--path",
        help="override path to save SHSH2 blob files",
        dest="save_path",
        default=None,
    )

    parser.add_option(
        "--time",
        help="override time to check new IPSW (in seconds, default: 6 hours - 21600)",
        dest="check_time",
        default=None,
        type=int,
    )

    return parser
