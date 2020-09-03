"""Constants for Seedboxes.cc integration"""
# Base component constants
NAME = "Seedboxes.cc"
DOMAIN = "seedboxes_cc"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"

ISSUE_URL = "https://github.com/swartjean/ha-seedboxes-cc/issues"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]

# Configuration and options
CONF_ENABLED = "enabled"
CONF_SCAN_PERIOD = "scan_period"
CONF_API_KEY = "api_key"

# Defaults
DEFAULT_SCAN_PERIOD = 900
MIN_SCAN_PERIOD = 300

# Defaults
DEFAULT_NAME = "Seedbox"

# Type names
NAME_STATUS = "Status"
NAME_DISK_QUOTA_FREE = "Disk Quota Free"
NAME_DISK_QUOTA_USED = "Disk Quota Used"
NAME_DISK_QUOTA_USED_PCT = "Disk Quota Used Percent"
NAME_MONTHLY_TRAFFIC = "Monthly Traffic"
NAME_DISK_SIZE = "Disk Size"
NAME_IP_ADDRESS = "IP Address"
NAME_TORRENT_CLIENT = "Torrent Client"

# Sensor units
SENSOR_UNITS = {
    NAME_DISK_QUOTA_FREE: "GB",
    NAME_DISK_QUOTA_USED: "GB",
    NAME_DISK_QUOTA_USED_PCT: "%",
    NAME_MONTHLY_TRAFFIC: "GB",
    NAME_DISK_SIZE: "GB",
}

# Icons
SENSOR_ICONS = {
    NAME_STATUS: "mdi:cloud",
    NAME_DISK_QUOTA_FREE: "mdi:harddisk",
    NAME_DISK_QUOTA_USED: "mdi:harddisk",
    NAME_DISK_QUOTA_USED_PCT: "mdi:harddisk",
    NAME_MONTHLY_TRAFFIC: "mdi:upload-network",
    NAME_DISK_SIZE: "mdi:harddisk",
}

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
Welcome to the Seedboxes.cc integration!
If you have any issues with this you can open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
