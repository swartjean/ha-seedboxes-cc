"""Sensor platform for Seedboxes.cc integration"""
from .const import (
    DOMAIN,
    NAME_DISK_QUOTA_FREE,
    NAME_DISK_QUOTA_USED,
    NAME_DISK_QUOTA_USED_PCT,
    NAME_DISK_SIZE,
    NAME_IP_ADDRESS,
    NAME_MONTHLY_TRAFFIC,
    NAME_STATUS,
    NAME_TORRENT_CLIENT,
    SENSOR_ICONS,
    SENSOR_UNITS,
)
from .entity import SeedboxBaseEntity


async def async_setup_entry(hass, entry, async_add_entities):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    entities = []

    # Construct list of entities
    entities.append(SeedboxStatusSensor(coordinator, entry))
    entities.append(SeedboxGenericSensor(coordinator, entry, NAME_DISK_QUOTA_FREE))
    entities.append(SeedboxGenericSensor(coordinator, entry, NAME_DISK_QUOTA_USED))
    entities.append(SeedboxGenericSensor(coordinator, entry, NAME_DISK_QUOTA_USED_PCT))
    entities.append(SeedboxGenericSensor(coordinator, entry, NAME_MONTHLY_TRAFFIC))

    async_add_entities(entities, True)


class SeedboxStatusSensor(SeedboxBaseEntity):
    """Seedbox Status Sensor class."""

    def __init__(self, coordinator, config_entry):
        self.coordinator = coordinator
        self.config_entry = config_entry
        self._type_name = NAME_STATUS
        self._icon = SENSOR_ICONS.get(self._type_name)

        super().__init__(coordinator, config_entry, self._type_name)

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get(self._type_name)

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return self._icon

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            NAME_TORRENT_CLIENT: self.coordinator.data.get(NAME_TORRENT_CLIENT),
            NAME_IP_ADDRESS: self.coordinator.data.get(NAME_IP_ADDRESS),
            NAME_DISK_SIZE: self.coordinator.data.get(NAME_DISK_SIZE),
        }


class SeedboxGenericSensor(SeedboxBaseEntity):
    """Seedbox Generic Sensor class."""

    def __init__(self, coordinator, config_entry, type_name):
        self.coordinator = coordinator
        self.config_entry = config_entry
        self._type_name = type_name
        self._unit = SENSOR_UNITS.get(type_name)
        self._icon = SENSOR_ICONS.get(type_name)

        super().__init__(coordinator, config_entry, type_name)

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get(self._type_name)

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return self._icon

    @property
    def unit_of_measurement(self) -> str:
        """Return sensor measurement unit."""
        return self._unit
