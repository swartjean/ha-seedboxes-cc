"""SeedboxBaseEntity class"""
from homeassistant.helpers import entity

from .const import DEFAULT_NAME, DOMAIN, NAME, VERSION


class SeedboxBaseEntity(entity.Entity):
    def __init__(self, coordinator, config_entry, type_name):
        self.coordinator = coordinator
        self.config_entry = config_entry
        self._name = f"{DEFAULT_NAME} {type_name}"
        self._unique_id = f"{self.config_entry.entry_id}-{type_name}"

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def should_poll(self):
        """No need to poll. Coordinator notifies entity of updates."""
        return False

    @property
    def available(self):
        """Return if entity is available."""
        return self.coordinator.last_update_success

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return self._unique_id

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.config_entry.entry_id)},
            "name": NAME,
            "model": VERSION,
            "manufacturer": "swartjean",
        }

    async def async_added_to_hass(self):
        """Connect to dispatcher listening for entity data notifications."""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    async def async_update(self):
        """Update entity."""
        await self.coordinator.async_request_refresh()
