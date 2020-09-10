# Seedboxes.cc Integration for Home Assistant

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
[![maintainer][maintenance-shield]][maintainer]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

![logo][logoimg]

This is a custom component to integrate with [Seedboxes.cc](https://seedboxes.cc/) and provide information and statics about your account.

Some examples of the type of information provided:

* Disk Quota
* Upload Traffic
* IP Address
* Torrent Client

**This component will set up the following platforms.**

Platform | Description
-- | --
`sensor` | A set of sensors to provide seedbox-related statistics

{% if not installed %}
## Installation

1. Click install
2. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for **"Seedboxes.cc"**

{% endif %}

## Configuration

All configuration is carried out in the UI. You will need to enter your Seedboxes.cc API key, [which can be obtained here](https://seedboxes.cc/client/settings).

<!---->

[logoimg]: https://raw.githubusercontent.com/swartjean/ha-seedboxes-cc/main/seedbox_logo.png
[buymecoffee]: https://www.buymeacoffee.com/swartjean
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/swartjean/ha-seedboxes-cc.svg?style=for-the-badge
[commits]: https://github.com/swartjean/ha-seedboxes-cc/commits/main
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/swartjean/ha-seedboxes-cc.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Jean%20Swart%20%40swartjean-blue.svg?style=for-the-badge
[maintainer]: https://github.com/swartjean
[releases-shield]: https://img.shields.io/github/v/release/swartjean/ha-seedboxes-cc?style=for-the-badge
[releases]: https://github.com/swartjean/ha-seedboxes-cc/releases
