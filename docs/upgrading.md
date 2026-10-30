# Upgrading from an earlier name

This integration was called Alexa Room Sync (domain `alexa_room_sync`, before 0.15.0) and then
Alexa Area Sync (`alexa_area_sync`, 0.15.0 to 0.18.x). Home Assistant sees each rename as a new
integration, so:

1. If the old one has *Sync automatically* on, turn it off (Configure > Settings).
2. Update in HACS and restart, then **Add integration > Alexa Group Sync** with the same Alexa
   account. It copies the old integration's settings and its record of the Alexa groups it manages,
   so your existing groups carry on; nothing is recreated.
3. Remove the old entry. That doesn't change Alexa. If HACS left the old folder
   (`custom_components/alexa_area_sync` or `alexa_room_sync`), delete it and restart.

Its actions are now `alexa_group_sync.*`, and its button, picker and sensor entity ids change, so
update anything of yours that used the old ones.
