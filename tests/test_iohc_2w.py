"""Tests for iohc 2W (bidirectional) config validation and constants."""

import pytest

from somfy.cover import (
    CONF_ENCRYPTION_KEY,
    CONF_IOHC_MODE,
    CONF_TARGET_NODE,
    IOHC_MODE_1W,
    IOHC_MODE_2W,
    validate_iohc_config,
)

import esphome.config_validation as cv


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

class TestConstants:
    """Verify 2W-specific constants are defined correctly."""

    def test_conf_iohc_mode_value(self):
        assert CONF_IOHC_MODE == "mode"

    def test_conf_target_node_value(self):
        assert CONF_TARGET_NODE == "target_node"

    def test_iohc_mode_1w_value(self):
        assert IOHC_MODE_1W == "1w"

    def test_iohc_mode_2w_value(self):
        assert IOHC_MODE_2W == "2w"


# ---------------------------------------------------------------------------
# validate_iohc_config()
# ---------------------------------------------------------------------------

class TestValidateIohcConfig:
    """Verify validate_iohc_config enforces 2W requirements."""

    def test_passes_1w_mode_no_extra_fields(self):
        config = {CONF_IOHC_MODE: IOHC_MODE_1W}
        assert validate_iohc_config(config) is config

    def test_passes_1w_mode_default(self):
        config = {}
        assert validate_iohc_config(config) is config

    def test_passes_2w_with_target_and_key(self):
        config = {
            CONF_IOHC_MODE: IOHC_MODE_2W,
            CONF_TARGET_NODE: 0x123456,
            CONF_ENCRYPTION_KEY: "34C3466ED88F4E8E16AA473949884373",
        }
        assert validate_iohc_config(config) is config

    def test_fails_2w_without_target_node(self):
        config = {
            CONF_IOHC_MODE: IOHC_MODE_2W,
            CONF_ENCRYPTION_KEY: "34C3466ED88F4E8E16AA473949884373",
        }
        with pytest.raises(cv.Invalid, match=CONF_TARGET_NODE):
            validate_iohc_config(config)

    def test_fails_2w_without_encryption_key(self):
        config = {
            CONF_IOHC_MODE: IOHC_MODE_2W,
            CONF_TARGET_NODE: 0x123456,
        }
        with pytest.raises(cv.Invalid, match=CONF_ENCRYPTION_KEY):
            validate_iohc_config(config)

    def test_fails_2w_without_both(self):
        config = {CONF_IOHC_MODE: IOHC_MODE_2W}
        with pytest.raises(cv.Invalid):
            validate_iohc_config(config)
