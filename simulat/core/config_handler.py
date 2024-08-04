# -*- coding: utf-8 -*-
"""Config handler module."""

from __future__ import annotations

import logging as lg
import os
from typing import Any, Final

import yaml
from cerberus import Validator

from simulat.core.version import VERSION


class ConfigHandler:
    """Config handler class.

    The config handler is responsible for loading, saving,
    and validating the configuration file.
    """

    CONFIG_FILE_PATH: Final[str] = "data/user/config.yaml"

    CONFIG_FILE_SCHEMA: Final = {
        "version": {"type": "string", "required": True},
        "fps_limit": {"type": "integer", "required": True},
        "resolution": {
            "type": "dict",
            "required": True,
            "schema": {
                "width": {"type": "integer", "required": True},
                "height": {"type": "integer", "required": True},
            },
        },
    }

    DEFAULT_CONFIG: Final[dict[str, Any]] = {
        "version": VERSION,
        "fps_limit": 60,
        "resolution": {"width": 1280, "height": 720},
    }

    def __init__(self) -> None:
        """Initialize the config handler."""
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.config: dict[str, Any] = {}

        if not self.user_config_exists:
            self.logger.warning("User configuration file not found. Creating...")
            self.config = ConfigHandler.DEFAULT_CONFIG.copy()
            self.save_config()

        self.config = self.load_config()

        self.validate_config()
        self.save_config()

        # check if version is up to date
        if not self.versions_match:
            self.logger.warning(
                "Version mismatch between default and user configuration files. This could lead to unexpected behavior."
                f"Current version: {ConfigHandler.DEFAULT_CONFIG.get('version')}, Config version: {self.config.get('version')}"
            )

    @property
    def versions_match(self) -> bool:
        """Check if the versions of the default and user configuration files match.
        Returns:
            bool: True if the versions match, False otherwise.
        """
        return ConfigHandler.DEFAULT_CONFIG.get("version") == self.config.get("version")

    @property
    def user_config_exists(self) -> bool:
        """Check if the user configuration file exists.
        Returns:
            bool: True if the versions match, False otherwise.
        """
        return os.path.isfile(self.CONFIG_FILE_PATH)

    def validate_config(self) -> None:
        """Validate the configuration file."""
        self.logger.info("Validating configuration...")

        v = Validator()

        valid = v.validate(self.config, self.CONFIG_FILE_SCHEMA)

        if valid:
            self.logger.debug("Configuration file is valid.")
            return

        # repair keys
        self.logger.error("Invalid configuration file. Repairing...")
        self._repair_keys(self.config, ConfigHandler.DEFAULT_CONFIG, v.errors)

    def _repair_keys(self, config_data: Any, default_data: Any, errors: Any) -> None:
        """Repair keys in the configuration file.

        Args:
            config_data (Any): The configuration data.
            default_data (Any): The default configuration data.
            errors (Any): The errors in the configuration data provided by the validator.
        """
        self.logger.info("Repairing configuration...")

        for key, value in errors.items():
            if isinstance(value, dict):
                # repair nested keys
                self._repair_keys(config_data[key], default_data[key], value)
            else:
                if key in default_data:
                    # repair key
                    self.logger.warning(f"Fixing key {key}...")
                    config_data[key] = default_data[key]
                else:
                    # skip unknown keys
                    self.logger.warning(f"Unknown key: {key}. Skipping...")

    def load_default_config(self) -> Any:
        """Load the default configuration."""
        self.logger.debug("Loading default configuration...")

        return ConfigHandler.DEFAULT_CONFIG

    def load_config(self) -> Any:
        """Load the configuration file."""
        self.logger.debug("Loading configuration...")

        if self.user_config_exists:
            with open(self.CONFIG_FILE_PATH, "r") as file:
                return yaml.safe_load(file)
        else:
            self.logger.error("Configuration file not found.")

    def save_config(self) -> None:
        """Save the configuration file."""
        self.logger.debug("Saving configuration...")

        with open(self.CONFIG_FILE_PATH, "w") as file:
            yaml.dump(self.config, file, default_flow_style=False)

    def get(self, key: str) -> Any:
        """Get a value from the configuration.

        Args:
            key (str): The key of the value to get.

        Returns:
            Any: The value.
        """
        return self.config[key]

    def get_default(self, key: str) -> Any:
        """Get a value from the default configuration.

        Args:
            key (str): The key of the value to get.

        Returns:
            Any: The value.
        """
        return ConfigHandler.DEFAULT_CONFIG[key]

    def set(self, key: str, value: Any) -> None:
        """Set a value in the configuration.

        Args:
            key (str): The key of the value to set.
            value (any): The value.
        """
        self.config[key] = value
        self.save_config()


if __name__ == "__main__":
    ch = ConfigHandler()
    print(ch.config)
