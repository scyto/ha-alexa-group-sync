# Changelog

- **v0.19.2:** the README is now a short getting-started guide; the detail moved to `docs/` and this changelog to `CHANGELOG.md`. No change to the integration itself.
- **v0.19.1:** with Alexa Devices, an Echo you haven't given an area there uses its Alexa Media Player area, so switching sessions doesn't pull Echos out of their groups.
- **v0.19.0:** renamed to **Alexa Group Sync**: domain `alexa_group_sync` (was `alexa_area_sync`), repo `ha-alexa-group-sync`. See [Upgrading from an earlier name](docs/upgrading.md).
- **v0.18.0:** setup says what's missing: no Alexa login integration, one that isn't signed in (with its state), a session that can't reach Alexa, or HA Cloud / exposure not set up.
- **v0.17.0:** safer removals (held until confirmed on a later sync, capped per run, never on adoption); a sync stops if HA's exposure settings can't be read; the managed-groups record is saved even after an error; the Alexa lists / to-do feature is removed; diagnostics redact Echo serials; actions register once at startup; the README is exact about what writes.
- **v0.16.0:** lists exposed devices Alexa doesn't have, and asks HA Cloud to resend them if they stay missing.
- **v0.15.1:** no "Unable to remove unknown job listener" error when the integration is reloaded or removed with auto-sync on.
- **v0.15.0:** renamed to **Alexa Area Sync** (domain `alexa_area_sync`, was `alexa_room_sync`) so it can't clash with other integrations of the old name. See [Upgrading from an earlier name](docs/upgrading.md).
- **v0.14.3:** floor groups hold only lights and light switches by default; the "Alexa lists unavailable" message is logged once at info level instead of a warning on every start.
- **v0.14.2:** an Echo that Alexa lists in a group by serial counts as already there, so it no longer shows as added on every sync; such entries show as "<Echo> (by serial)".
- **v0.14.1:** Alexa Media Player works again as a fallback; Alexa Devices is used when it's signed in to the account.
- **v0.14.0:** uses Home Assistant's built-in Alexa Devices integration instead of Alexa Media Player.
- **v0.13.0:** optional floor groups and auto-sync; Add to Home Assistant buttons in the README.
- **v0.12.0:** Activity and *Last result* name the devices each run added, removed or deleted, not just counts; `list_groups` lists each group's devices.
- **v0.11.1:** Echos: only the Echo speaker device is added to a group (a tablet's AlexaBridge endpoint made Amazon reject the update).
- **v0.11.0:** optional *Put Echos in their area's Alexa group*, using Alexa Media Player's areas.
- **v0.10.2:** each run's per-group changes are written to the Activity (logbook); the notification is gone.
- **v0.10.1:** *Last result* keeps each run's per-group outcome as attributes, viewable in History.
- **v0.10.0:** clearer names: *One area* / *Whole house* controls, "area" for HA and "Alexa group" for what's created.
- **v0.9.3:** removing the integration also removes the `probe_endpoints` action.
- **v0.9.2:** `dump_appliances` reports the GraphQL and `/api/phoenix` sources separately.
- **v0.9.1:** *Area to sync* lists only areas that get an Alexa group.
- **v0.9.0:** *Area to sync* picker and per-area buttons on the device page; *Last result* and the
  picked area survive restarts.
- **v0.8.0:** *Sync one area* in Configure (moved to the device page in 0.9.0).
- **v0.7.0:** removing the integration leaves Alexa alone; *Remove managed rooms* in Configure;
  per-call account selection; *Last result* sensor.
- **v0.6.0:** full lifecycle (create, update, delete, adopt, keep Echos), plus Preview and Sync
  buttons (results went to a notification until 0.10.2).
- **v0.5.0:** *Rooms to skip* area picker.
- **v0.4.1:** `sync` / `sync_area` actually run. They were registered as lambdas HA never awaited.
- **v0.4.0:** devices are listed via GraphQL, matched by HA's `domain#object_id` ids and by alias.
  The original's `/api/phoenix` lookup returns nothing on current accounts.
