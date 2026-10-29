"""Echo areas: with Alexa Devices, an Echo without an area falls back to AMP's."""

from types import SimpleNamespace

from alexa_group_sync import sync as s
from alexa_group_sync.const import ALEXA_DEVICES_DOMAIN


def _device(dev_id, serial, area_id=None):
    return SimpleNamespace(id=dev_id, area_id=area_id, entry_type=None,
                           identifiers={(ALEXA_DEVICES_DOMAIN, serial)})


def _patch_registries(monkeypatch, devices):
    monkeypatch.setattr(s.dr, "async_entries_for_config_entry", lambda reg, eid: devices,
                        raising=False)
    monkeypatch.setattr(s.er, "async_entries_for_device", lambda reg, dev_id: [],
                        raising=False)


def test_alexa_devices_echo_without_area_uses_amp_area(monkeypatch):
    _patch_registries(monkeypatch, [_device("d1", "abc123"), _device("d2", "XYZ", "study")])
    monkeypatch.setattr(s, "_echo_serials_by_area", lambda hass, email: {
        "kitchen": [("media_player.kitchen_show", "ABC123")],
        "bedroom": [("media_player.dot", "XYZ")],
    })
    areas = s._echo_areas(None, "me@example.com", "entry")
    # No area in Alexa Devices: AMP's area. Placed in Alexa Devices: that area wins.
    assert areas == {"kitchen": [("device:d1", "ABC123")], "study": [("device:d2", "XYZ")]}


def test_echo_without_area_anywhere_is_left_out(monkeypatch):
    _patch_registries(monkeypatch, [_device("d1", "abc123")])
    monkeypatch.setattr(s, "_echo_serials_by_area", lambda hass, email: {})
    assert s._echo_areas(None, "me@example.com", "entry") == {}


def test_amp_session_uses_amp_areas_only(monkeypatch):
    amp = {"kitchen": [("media_player.kitchen_show", "ABC123")]}
    monkeypatch.setattr(s, "_echo_serials_by_area", lambda hass, email: amp)
    assert s._echo_areas(None, "me@example.com", None) == amp
