import logging

class Colors:
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[94m"
    RED = "\033[91m"
    VIOLET = "\033[35m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    BG = "\33[100m"

class Formatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: f"{Colors.BG}%(asctime)3s{Colors.ENDC} {Colors.VIOLET}%(name)3s {Colors.GREEN}{Colors.BOLD}%(levelname)3s{Colors.ENDC} %(message)12s",
        logging.INFO: f"{Colors.BG}%(asctime)3s{Colors.ENDC} {Colors.VIOLET}%(name)3s {Colors.BLUE}{Colors.BOLD}%(levelname)3s{Colors.ENDC} %(message)12s",
        logging.WARNING: f"{Colors.BG}%(asctime)3s{Colors.ENDC} {Colors.VIOLET}%(name)3s {Colors.YELLOW}{Colors.BOLD}%(levelname)3s{Colors.ENDC} %(message)12s",
        logging.ERROR: f"{Colors.BG}%(asctime)3s{Colors.ENDC} {Colors.VIOLET}%(name)3s {Colors.RED}{Colors.BOLD}%(levelname)3s{Colors.ENDC} %(message)12s",
        logging.CRITICAL: f"{Colors.BG}%(asctime)3s{Colors.ENDC} {Colors.VIOLET}%(name)3s {Colors.RED}{Colors.BOLD}%(levelname)3s{Colors.ENDC} %(message)12s"
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%H:%M:%S")
        return formatter.format(record)

class Logger:
    def setup() -> logging.Logger:
        logger = logging.getLogger("MCPackConverter")
        logger.setLevel(logging.INFO)
        sh = logging.StreamHandler()
        sh.setFormatter(Formatter())
        logger.addHandler(sh)
        return logger