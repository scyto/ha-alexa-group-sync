# Alexa Group Sync

Keep your **Alexa groups** in step with your **Home Assistant areas**, so "Alexa, turn off the
kitchen" controls what HA calls the kitchen. HA Cloud exposes your devices to Alexa but can't create
groups. This creates one for each area and keeps it up to date, with optional groups per floor.

> ⚠️ **This uses Amazon's undocumented Alexa API**, which can change without notice. It previews by
> default and writes nothing until you turn writes on.

## What you need

- **Home Assistant** 2025.12 or later.
- **A signed-in Alexa account** in either integration. This borrows that session and never asks for
  your password:
  - **Alexa Devices**, built into HA (recommended). Before HA 2026.11 its sign-in is broken by an
    Amazon change, so use Alexa Media Player there.
  - **Alexa Media Player**, from HACS.
- **Your devices exposed to Alexa through HA Cloud** (Settings > Voice assistants > Expose) and
  discovered in the Alexa app.

## Install

1. [![Open this repository in Home Assistant](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=scyto&repository=ha-alexa-group-sync&category=integration)
   Download it, then restart HA.
2. [![Add Alexa Group Sync to Home Assistant](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=alexa_group_sync)
   Pick your Alexa account. Setup tells you if anything above is missing.

## Your first sync

On the integration's device page:

1. Press **Whole house – Preview**. **Activity** lists, by name, what each Alexa group would gain or
   lose.
2. To allow writes, go to **Configure > Settings**, turn **Dry-run** off and tick **I understand
   'apply' will write to my Alexa account**.
3. Pick an area in **One area** and press **One area – Sync** to try it.
4. Press **Whole house – Sync** for the rest. Groups can take a minute or two to appear in the Alexa
   app.

For "turn on the lights" to work without naming the area, each Echo must be in its area's group. Turn
on **Put Echos in their area's Alexa group**, or add them by hand in the Alexa app.

## Options

| Option (Configure > Settings) | Default | What it does |
|---|---|---|
| Dry-run | On | Syncs only preview. |
| I understand 'apply' will write… | Off | Must be ticked for a sync to write. |
| Sync automatically | Off | Syncs after changes to areas, floors, devices or exposure, and hourly. |
| Put Echos in their area's Alexa group | Off | Adds each Echo to its area's group. |
| Also make one Alexa group per floor | Off | "Alexa, turn off the ground floor". |
| Floor groups: lights and light switches only | On | Floor commands leave thermostats and the like alone. |
| Include climate entities | On | Thermostats join their area's group. |
| Include child-lock switches | Off | Adds them to groups. |
| Ask HA Cloud to resend devices Alexa has lost | On | Re-sends exposed devices missing from Alexa. |
| Alexa group name prefix | None | For example `HA `, to tell synced groups apart. |
| Areas to skip | None | These areas get no group. |

More detail: [all options](https://github.com/scyto/ha-alexa-group-sync/blob/main/docs/options.md).

## What it won't do

- **Your own groups are left alone**, except that a group named exactly like an unmanaged area is
  adopted. Devices you added to a group by hand stay.
- **Deletions wait.** A group goes only if it was already due for removal at least 15 minutes earlier,
  and a run that would remove many groups holds them all. Deleting matters because Alexa routines
  that use a group break.
- **Removing the integration doesn't change Alexa.** Your groups keep working. To delete them too, use
  **Configure > Remove the Alexa groups it manages** first.

## If something's wrong

- **Alexa Devices fails with "Bad Request":** turn on Calling & Messaging in the Alexa app (the
  Communicate tab), then reload Alexa Devices
  ([aioamazondevices#1247](https://github.com/chemelli74/aioamazondevices/issues/1247)).
- **Alexa Media Player says "failed to login":** restart HA and finish its login on the first attempt
  ([alexa_media_player#3559](https://github.com/alandtse/alexa_media_player/issues/3559)).
- **"Which one?" from Alexa:** two areas sound alike. Rename one, or use a prefix. Since HA 2026.8 Alexa
  gets an entity's first alias as its name, so put the name you say first.
- **"Turn off the lights" skips a device:** Alexa treats switches as switches. Use HA's *Show as light*.
- **A device isn't in any group:** it needs an HA area.
- **Blank labels after updating:** reload the browser.

## More

- [How it works](https://github.com/scyto/ha-alexa-group-sync/blob/main/docs/how-it-works.md): the device page, what a sync changes, removing it
- [Actions](https://github.com/scyto/ha-alexa-group-sync/blob/main/docs/actions.md) for scripts and automations
- [Upgrading from Alexa Room Sync or Alexa Area Sync](https://github.com/scyto/ha-alexa-group-sync/blob/main/docs/upgrading.md)
- [Changelog](https://github.com/scyto/ha-alexa-group-sync/blob/main/CHANGELOG.md)

## Contributing

Branch from `dev` and open pull requests against `dev`. To release, bump `version` in `manifest.json`
and add a line to `CHANGELOG.md`; merging that to `main` tags and publishes the release.

## Credits and licence

MIT. Inspired by and originally forked from
[neilellis/ha-alexa-room-sync](https://github.com/neilellis/ha-alexa-room-sync); the early history is
in [scyto/ha-alexa-room-sync-history](https://github.com/scyto/ha-alexa-room-sync-history). Sign-in
relies on [aioamazondevices](https://github.com/chemelli74/aioamazondevices) or
[alexa_media_player](https://github.com/alandtse/alexa_media_player) /
[alexapy](https://gitlab.com/keatontaylor/alexapy) (Apache-2.0). Endpoint shapes come from
[alexa-remote](https://github.com/Apollon77/alexa-remote) (MIT) and community reverse-engineering.
Not affiliated with or endorsed by Amazon.
