# Custom_component for `hassbian-config`
![Version](https://img.shields.io/badge/version-1.0.0-green.svg?style=for-the-badge)

A custom component which allows you to controll some hassbian-config functions from Home Assistant.

**Some of the features require aleast version 0.9.0 of [hassbian-config](https://github.com/home-assistant/hassbian-scripts/releases/tag/v0.9.0)**

Example configuration.yaml:
```yaml
hassbian_config:
```

There will be registrered 2 services:
- hassbian_config.install_suite
- hassbian_config.upgrade_suite

##### hassbian_config.install_suite example:
```json
{
"suite":"hue"
}
```

##### hassbian_config.upgrade_suite example:
```json
{
"suite":"hassbian-script",
"beta": true
}
```

When the install/upgrade is done you will get a [Persistent notification](https://www.home-assistant.io/components/persistent_notification/) stating that it is finished.  

If it fails you will see that in the log, example:
```text
[custom_components.hassbian_config] The suite hassbiand-script does not exist, or can not be upgraded automatically.
```

***
_Disclamer: This is the frist thing I have done i Python, there can be issues._