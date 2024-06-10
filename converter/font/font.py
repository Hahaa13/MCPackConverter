from logging import Logger
from PIL import Image

class Fonts:
    def __init__(self, file: str, logger: Logger) -> None:
        self.file = file
        self.logger = logger
