import os
import json
import shutil
import logging
from uuid import uuid4

class Gen:
    def __init__(self, bedrock_folder: str, java_folder: str, logger: logging.Logger) -> None:
        self.bedrock_folder = bedrock_folder
        self.java_folder = java_folder
        self.logger = logger
    
    def packinfo(self):
        with open(f"{self.java_folder}/pack.mcmeta") as f:
            jpd = json.load(f)
        data = {
            "format_version": 2,
            "header": {
                "name": "Pack Convert By MCPackConverter",
                "description": jpd["pack"]["description"],
                "uuid": str(uuid4()),
                "version": [1,0,0],
                "min_engine_version": [1,16,0]
            },
            "modules": [
                {
                    "description": jpd["pack"]["description"],
                    "type": "resources",
                    "uuid": str(uuid4()),
                    "version": [1,0,0]
                }
            ]
        }
        with open(f"{self.bedrock_folder}/manifest.json", "w") as f:
            json.dump(data, f, indent=int(os.getenv("JSON_INDENT")))
        self.logger.info("Created manifest")
        if os.path.exists(f"{self.java_folder}/pack.png"):
            shutil.copy(f"{self.java_folder}/pack.png", f"{self.bedrock_folder}/pack_icon.png")
            self.logger.info("Copied pack icon")
