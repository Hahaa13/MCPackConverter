import os
import shutil
import logging
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

class PackLoader:
    def load(logger: logging.Logger, packfile: str, path: str):
        zf = BytesIO(urlopen(packfile).read()) if packfile.startswith("http") else packfile
        with ZipFile(zf) as zfd:
            zfd.extractall(path)
        logger.info(f"Loaded packfile {packfile}")
