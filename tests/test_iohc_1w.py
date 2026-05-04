"""Tests for iohc 1W (one-way) specific behaviour."""

from somfy.cover import (
    CONF_ENCRYPTION_KEY,
    CONF_IOHC_MODE,
    IOHC_MODE_1W,
    validate_iohc_config,
)


class TestIohc1WConfig:
    """Verify 1W mode validation passes without extra requirements."""

    def test_passes_explicit_1w_mode(self):
        config = {CONF_IOHC_MODE: IOHC_MODE_1W}
        assert validate_iohc_config(config) is config

    def test_passes_default_mode(self):
        config = {}
        assert validate_iohc_config(config) is config

    def test_passes_1w_with_optional_encryption_key(self):
        config = {
            CONF_IOHC_MODE: IOHC_MODE_1W,
            CONF_ENCRYPTION_KEY: "34C3466ED88F4E8E16AA473949884373",
        }
        assert validate_iohc_config(config) is config
