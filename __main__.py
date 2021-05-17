import asyncio
import logging
import sys

from cli import check_os, header, option_parser
from tsschecker import TSSSaver
from utils import Logger, load_config

if __name__ == "__main__":
    header()

    optparser = option_parser()
    (options, args) = optparser.parse_args(sys.argv)

    if options.debug is not None:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    logger = Logger.generate("Main")

    logger.debug("Checking your opeating system")

    if not check_os():
        print("AutoBlobSaver only supports Macintosh & Linux systems.")
        exit(0)

    config = load_config()

    if options.time is not None:
        logger.debug(f"Overriding refresh time to {options.time}")
        config["time"] = options.time
    else:
        config["time"] = 21600  # default to 6 hrs

    if options.save_path is not None:
        logger.debug(f"Overriding save path to {options.save_path}")
        config["outdir"] = options.save_path

    tss = TSSSaver(config)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tss.start())
