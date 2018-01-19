import logging as log
import sys
import signal


log_file = "rous/rous.log"
whitelist = "rous/whitelist.txt"


def setup_logger():
    log.basicConfig(filename=log_file,
        format='%(asctime)s::%(levelname)s:: %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        stream=sys.stdout,
        level=log.INFO)


def parse_whitelist():
	try:
		file = open(whitelist, "r")
		lst = [line.split(',') for line in file.readlines()]
		return lst
	except:
		log.error("Failed to read whitelist")


def handle_crtl_z(signal, frame):
    log.info("Crtl Z -- Server shutting down")
    sys.exit(0)
