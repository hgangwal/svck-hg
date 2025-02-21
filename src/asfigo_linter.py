# ----------------------------------------------------
# SPDX-FileCopyrightText: AsFigo Technologies, UK
# SPDX-FileCopyrightText: VerifWorks, India
# SPDX-License-Identifier: MIT
# ----------------------------------------------------

import argparse
import tomli
import os.path
import copy
import functools
from operator import countOf
import operator as op
import logging
import json
import string_utils.validation  as str_val


class BaseLintLogger:
    def __init__(self, prefix, configFile="config.toml", logLevel=logging.INFO):
        self.prefix = prefix
        self.logger = logging.getLogger(f"{prefix}Logger")
        self.logger.setLevel(logLevel)
        handler = logging.StreamHandler()
        handler.setLevel(logLevel)
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        if self.logger.hasHandlers():
            self.logger.handlers.clear()
        self.logger.addHandler(handler)
        self.rulesConfig = self.loadConfig(configFile)
        self.infoCount = 0
        self.warningCount = 0
        self.errorCount = 0

    def loadConfig(self, configFile):
        try:
            with open(configFile, "rb") as file:
                config = tomli.load(file)
            return config.get("rules", {})
        except FileNotFoundError:
            self.logger.warning(f"{self.prefix}: Config file '{configFile}' not found. Using default settings.")
            return {}

    def ruleEnabled(self, ruleId):
        return self.rulesConfig.get(ruleId, True)

    def logInfo(self, msg):
        self.infoCount += 1
        logMsg = f"{self.prefix}: INFO: {msg}"
        self.logger.info(logMsg)

    def logViolation(self, ruleId, msg, severity="ERROR"):
        if self.ruleEnabled(ruleId):
            logMsg = f"{self.prefix}: Violation: [{ruleId}]: {msg}"
            if severity == "ERROR":
                self.errorCount += 1
                self.logger.error(logMsg)
            elif severity == "WARNING":
                self.warningCount += 1
                self.logger.warning(logMsg)
            else:
                raise ValueError(f"Unsupported severity level: {severity}")
        else:
            self.logger.info(f"{self.prefix}: Rule [{ruleId}] is disabled and will not be logged.")

    def logSummary(self):
        self.logger.info(f"{self.prefix}: Summary: INFO: {self.infoCount}, WARNING: {self.warningCount}, ERROR: {self.errorCount}")


class AsFigoLinter(BaseLintLogger):
    def __init__(self, configFile="config.toml", logLevel=logging.INFO):
        super().__init__(prefix="AsFigo", configFile=configFile, logLevel=logLevel)
        self.args = self.parseArguments()
        self.testName = self.args.test

    def parseArguments(self):
        parser = argparse.ArgumentParser(description="AsFigoLinter Argument Parser")
        parser.add_argument("-t", "--test", required=True, help="Input test name (file path)")
        return parser.parse_args()

