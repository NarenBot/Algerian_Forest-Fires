import logging

logging.basicConfig(
    filename="logBase.log",
    level= logging.DEBUG,
    format="%(asctime)s | %(module)s | %(levelname)s => %(message)s",
    datefmt="%d-%b-%y %H:%M:%S"
)

log = logging.getLogger()
# log.setLevel(logging.DEBUG)