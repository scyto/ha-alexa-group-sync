# Actions (services)

For scripts and automations. With more than one Alexa account set up, pass `config_entry_id`.

| Action | Writes? | Notes |
|---|---|---|
| `alexa_group_sync.preview` | No | Plan and match details. Optional `area_id`. |
| `alexa_group_sync.sync` | With `apply: true` and the confirmation | Full sync. |
| `alexa_group_sync.sync_area` | With `apply: true` and the confirmation | One area. |
| `alexa_group_sync.list_groups` | No | Lists the groups in your Alexa account and the devices in each. |
| `alexa_group_sync.remove_managed_rooms` | With `confirm: true`, whatever the dry-run setting | Removes the groups it created or adopted (keeps devices you added yourself). |
| `alexa_group_sync.dump_appliances`, `probe_endpoints` | No | Diagnostics. `dump_appliances` redacts Amazon ids and Echo serials but keeps device names. |
