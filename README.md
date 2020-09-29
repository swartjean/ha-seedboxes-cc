# Seedboxes.cc Integration for Home Assistant

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
[![maintainer][maintenance-shield]][maintainer]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

![logo][logoimg]

This is a custom component to integrate with [Seedboxes.cc](https://seedboxes.cc/) and provide information and statistics about your account.

Some examples of the type of information provided:

* Disk Quota
* Upload Traffic
* IP Address
* Torrent Client

**This component will set up the following platforms.**

Platform | Description
-- | --
`sensor` | A set of sensors to provide seedbox-related statistics

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `seedboxes_cc`.
4. Download _all_ the files from the `custom_components/seedboxes_cc/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for **"Seedboxes.cc"**

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
