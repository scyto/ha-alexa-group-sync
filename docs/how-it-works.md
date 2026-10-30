# How it works

## The device page

| Control | What it does |
|---|---|
| **One area** | Picks an HA area. Lists only areas that get an Alexa group (something exposed to Alexa, not skipped). Follows renames. |
| **One area – Preview** | Shows what syncing that area would change. Never writes. |
| **One area – Sync** | Syncs only that area's Alexa group. |
| **Whole house – Preview** | Shows what syncing every area would change. Never writes. |
| **Whole house – Sync** | Syncs every area. |
| **Last result** | One-line summary of the last run. Each run also adds an entry to the device's **Activity** listing what changed in each Alexa group, and the latest run's detail is in the sensor's attributes (`scope`, `mode`, `ran_at`, `groups`). |

Both Sync buttons write only when dry-run is off and writes are confirmed; otherwise they preview.
HA lists the controls by name, which keeps the *One area* controls together, followed by
*Whole house*.

**Wording:** an **area** is Home Assistant's; an **Alexa group** is what this creates for it in Alexa.

## What a sync changes

The integration remembers which Alexa groups it created or adopted, and which devices it put in each, keyed by
HA area. A full sync then:

- **creates** a group for an area that doesn't have one;
- **updates** a managed group when the area's devices change or the area is renamed;
- **deletes** a managed group when its area is skipped, deleted, or has no exposed devices left.
  If the group also holds something you added yourself, such as an Echo, the HA devices are taken
  out, your additions stay, and the group is released instead of deleted.

A single-area sync never touches other groups. Groups the integration didn't create are left alone,
with one exception: an Alexa group with exactly the area's name, in an area nothing manages yet, is
adopted. Only Home Assistant devices are matched, plus Echos if you turn that option on. Nothing else is added.

Deleting a group is the one change you'd notice later (Alexa routines that use it break,
and a recreated group is a new one), so removals are deliberate:

- a group is only deleted, or released, if it was already due for removal on a sync at least
  15 minutes earlier; until then Activity says it's *held*;
- if more than three groups would go in one run, or half of those it manages (once it manages
  six or more), it holds all of them, because that looks like a glitch, not a decision;
- it never takes over one of your groups by name just to delete it.

As safety checks, a sync refuses to run if Alexa returns no devices, or no groups while groups are
managed. Without that, a glitch on Amazon's side could look like "everything is gone".

## Removing it

Removing the integration **doesn't change Alexa**. Your groups keep working, and a reinstall picks
them up again by name. Only the integration's saved record of its groups is deleted. Its settings
go too: after re-adding it, dry-run is back on, so turn it off again before syncing.

To take the groups down too, first use **Configure > Remove the Alexa groups it manages**, which asks
you to confirm. It removes the groups it manages, which are the ones it created **plus any it
adopted** (an existing Alexa group with exactly an area's name). It keeps any device it didn't put
there. So an adopted group you made by hand is deleted too if it only held HA devices. Rename such
a group in Alexa before a sync if you want it left alone.

## Under the hood

- **Login:** it reuses an already signed-in session, so no credentials live here: the HTTP
  wrapper of Alexa Devices' `aioamazondevices` API, or Alexa Media Player's `AlexaLogin` and
  alexapy's request helper. Both are private to those integrations, so an update to either can
  break this until it's adapted.
- **Devices:** it lists Alexa's smart-home devices with the Alexa app's GraphQL query
  (`POST /nexus/v1/graphql`), falling back to `GET /api/phoenix`. It matches each exposed HA entity
  by the entity_id that HA Cloud embeds in the Alexa device id (`…_light#kitchen_cans`). Otherwise
  it matches by name, where the first alias is what HA sends Alexa as the name.
- **Groups:** `GET /api/phoenix/group` to list, `POST` to create, `PUT /api/phoenix/group/{id}` to
  update (it sends Amazon's own group document back with the name and members changed), and
  `DELETE` to remove.
- **Memory:** the managed groups and their members are kept in HA storage
  (`.storage/alexa_group_sync.<entry>.rooms`).
