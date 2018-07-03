# Custom_component for `hassbian-config`.
  
[![Version](https://img.shields.io/badge/version-version-green.svg?style=for-the-badge)](#) [![mantained](https://img.shields.io/maintenance/yes/2018.svg?style=for-the-badge)](#)   
A custom component which allows you to controll some hassbian-config functions from Home Assistant.
  
To get started put `/custom_components/hassbian_config.py`  
here: `<config directory>/custom_components/hassbian_config.py`  
  
**Example configuration.yaml:**
```yaml
hassbian_config:
```
  
For more example see the [services.yaml](https://gitlab.com/custom_components/hassbian_config/blob/master/custom_components/hassbian_config/services.yaml) file.  
  
***
Due to how `custom_componentes` are loaded, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home-Assistant.