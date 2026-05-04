"""Protocol-agnostic tests for the somfy cover component."""

from somfy.cover import (
    CODEOWNERS,
    CONF_ALLOWED_REMOTES,
    CONF_DETECTED_REMOTE,
    CONF_ENCRYPTION_KEY,
    CONF_IOHC_MODE,
    CONF_PROG_BUTTON,
    CONF_REMOTE_CODE,
    CONF_REMOTE_RECEIVER,
    CONF_SOMFY_ID,
    CONF_SOMFY_STORAGE_KEY,
    CONF_SOMFY_STORAGE_NAMESPACE,
    CONF_REPEAT_COMMAND_COUNT,
    CONF_TARGET_NODE,
    COMMON_COVER_FIELDS,
    DEPENDENCIES,
    IOHC_MODE_1W,
    IOHC_MODE_2W,
    TYPE_IOHC,
    TYPE_RTS,
)

from somfy import (
    CODEOWNERS as HUB_CODEOWNERS,
    CONF_CC1101_ID,
    CONF_REMOTE_RECEIVER as HUB_CONF_REMOTE_RECEIVER,
    CONF_REMOTE_TRANSMITTER,
    DEPENDENCIES as HUB_DEPENDENCIES,
    MULTI_CONF,
    TYPE_IOHC as HUB_TYPE_IOHC,
    TYPE_RTS as HUB_TYPE_RTS,
)


# ---------------------------------------------------------------------------
# Shared constants
# ---------------------------------------------------------------------------

class TestSharedConstants:
    """Constants used across all protocols."""

    def test_type_rts(self):
        assert TYPE_RTS == "rts"

    def test_type_iohc(self):
        assert TYPE_IOHC == "iohc"

    def test_types_match_hub_and_cover(self):
        assert TYPE_RTS == HUB_TYPE_RTS
        assert TYPE_IOHC == HUB_TYPE_IOHC

    def test_conf_somfy_id(self):
        assert CONF_SOMFY_ID == "somfy_id"

    def test_conf_remote_code(self):
        assert CONF_REMOTE_CODE == "remote_code"

    def test_conf_storage_key(self):
        assert CONF_SOMFY_STORAGE_KEY == "storage_key"

    def test_conf_storage_namespace(self):
        assert CONF_SOMFY_STORAGE_NAMESPACE == "storage_namespace"

    def test_conf_repeat_command_count(self):
        assert CONF_REPEAT_COMMAND_COUNT == "repeat_command_count"

    def test_conf_prog_button(self):
        assert CONF_PROG_BUTTON == "prog_button"

    def test_conf_encryption_key(self):
        assert CONF_ENCRYPTION_KEY == "encryption_key"


# ---------------------------------------------------------------------------
# Module-level attributes
# ---------------------------------------------------------------------------

class TestModuleAttributes:
    """Verify module-level metadata."""

    def test_codeowners(self):
        assert "@LeonardPitzu" in CODEOWNERS

    def test_dependencies_include_esp32(self):
        assert "esp32" in DEPENDENCIES

    def test_common_cover_fields_is_dict(self):
        assert isinstance(COMMON_COVER_FIELDS, dict)


# ---------------------------------------------------------------------------
# Hub constants
# ---------------------------------------------------------------------------

class TestHubConstants:
    """Verify hub-level constants in __init__.py."""

    def test_conf_remote_transmitter(self):
        assert CONF_REMOTE_TRANSMITTER == "remote_transmitter"

    def test_conf_remote_receiver(self):
        assert HUB_CONF_REMOTE_RECEIVER == "remote_receiver"

    def test_conf_cc1101_id(self):
        assert CONF_CC1101_ID == "cc1101_id"

    def test_codeowners(self):
        assert "@LeonardPitzu" in HUB_CODEOWNERS

    def test_dependencies_include_esp32(self):
        assert "esp32" in HUB_DEPENDENCIES

    def test_multi_conf_enabled(self):
        assert MULTI_CONF is True


# ---------------------------------------------------------------------------
# Module importability
# ---------------------------------------------------------------------------

class TestImports:
    """Verify all expected symbols are importable."""

    def test_import_somfy_init(self):
        import somfy
        assert hasattr(somfy, "CONF_REMOTE_TRANSMITTER")
        assert hasattr(somfy, "CONF_REMOTE_RECEIVER")
        assert hasattr(somfy, "CONF_CC1101_ID")

    def test_import_somfy_cover(self):
        from somfy import cover
        assert hasattr(cover, "TYPE_RTS")
        assert hasattr(cover, "TYPE_IOHC")
        assert hasattr(cover, "CONF_SOMFY_ID")
        assert hasattr(cover, "COMMON_COVER_FIELDS")
