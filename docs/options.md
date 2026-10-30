# Options

In **Configure > Settings** on the integration.

- **Dry-run** (on by default): syncs never write to Alexa. (*Remove the Alexa groups it
  manages* is separate and has its own confirmation.)
- **I understand 'apply' will write to my Alexa account**: must be ticked for any write.
- **Alexa group name prefix**: for example `HA `, to tell synced groups apart.
- **Include climate entities** (on by default): thermostats go in their area's group.
- **Include child-lock switches** (off by default).
- **Put Echos in their area's Alexa group** (off by default): each Echo that has an HA area joins
  that area's group, matched by serial number. The areas come from whichever integration the
  session comes from (Alexa Devices or Alexa Media Player). With Alexa Devices, an Echo you haven't
  given an area there uses its Alexa Media Player area. Phone apps and speaker groups are skipped. Echos placed this way are managed like HA devices: moved when you change their area, and
  removed by *Remove the Alexa groups it manages*.
- **Also make one Alexa group per Home Assistant floor** (off by default): each HA floor
  gets a group holding the HA devices of its synced areas, so "Alexa, turn off the ground
  floor" works. Floors with nothing synced get no group, Echos stay only in their area's
  group, and a floor named the same as an area's group is skipped. Turning this off
  removes the floor groups on the next whole-house sync.
- **Floor groups: lights and light switches only** (on by default): floor groups hold only
  lights and switches, so "Alexa, turn off the ground floor" doesn't also turn off thermostats,
  purifiers or other devices. Turn it off to give floor groups everything their areas have.
- **Ask HA Cloud to resend exposed devices that Alexa has lost** (on by default): every run lists
  devices that are exposed and have an area in HA but that Alexa doesn't know about ("Not in Alexa
  yet"). If one is still missing 10 minutes later, a sync asks HA Cloud to send it to Alexa again,
  at most once an hour. This is the report HA Cloud's own *Sync entities* button sends; it never
  turns exposure off, which would make Alexa delete the device.
- **Sync automatically** (off by default): runs a whole-house sync a minute after you
  change areas, floors, devices or what's exposed to Alexa, and once an hour to catch
  devices Alexa discovers late. It only writes when dry-run is off and the confirmation is
  ticked, and it only adds to Activity when something changed.
- **Areas to skip**: areas that never get an Alexa group from a whole-house sync and don't appear
  in *One area*. If a skipped area already has an Alexa group from this integration, the next
  whole-house sync removes it. The `sync_area` action can still target a skipped area directly.
