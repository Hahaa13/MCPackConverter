import os
import dotenv
import shutil
from urllib.request import urlopen
from zipfile import ZipFile
from converter.gen import Gen
from utils.packloader import PackLoader
from utils.logger import Logger

class MCPackConverter:
    def __init__(self, javapack: str, javapackadd: str = None, bedrockadd: str = None):
        self.javapack = javapack
        self.javapackadd = javapackadd
        self.bedrockadd = bedrockadd
        self.logger = Logger.setup()

    def convert(self):
        if not (self.javapack.startswith("http") or self.javapack.endswith(".zip")):
            self.logger.error("Java pack url not found or input not url/file")
            return

        for folder in ("convert/", "bedrock/", "caches/"):
            if os.path.exists(folder):
                shutil.rmtree(folder)
            os.makedirs(folder, exist_ok=True)
        else:
            self.logger.warning("Clear old convert file")

        PackLoader.load(self.logger, self.javapack, "convert/")
        gen = Gen("bedrock", "convert", self.logger)
        gen.packinfo()

if __name__ == "__main__":
    dotenv.load_dotenv()
    MCPackConverter(os.getenv("PACK"), os.getenv("PACKADD"), os.getenv("BEDROCKPACKMERGE")).convert()