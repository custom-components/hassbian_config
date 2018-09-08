"""
A component which allows you to controll some hassbian-config functions.

For more details about this component, please refer to the documentation at
https://github.com/ludeeus/hassbian_config
"""
import logging

__version__ = '2.0.1'

REQUIREMENTS = ['pyhassbian==0.0.3']

DOMAIN = 'hassbian_config'

_LOGGER = logging.getLogger(__name__)


def setup(hass, config):
    """Component the setup."""
    import pyhassbian

    def install_suite_service(call):
        """Define install service."""
        suite = call.data.get('suite')
        dev = call.data.get('dev')
        beta = call.data.get('beta')
        version = call.data.get('version')
        all_suites = pyhassbian.get_suites()
        if suite in all_suites:
            _LOGGER.info('The suite %s is now beeing installed.', suite)
            pyhassbian.manage_suite('install', suite, dev, beta, version)
            _LOGGER.info('The suite %s has been installed.', suite)
        else:
            _LOGGER.error('The suite %s does not exist.', suite)

    def upgrade_suite_service(call):
        """Define update service."""
        suite = call.data.get('suite')
        dev = call.data.get('dev')
        beta = call.data.get('beta')
        version = call.data.get('version')
        if suite in pyhassbian.get_suites():
            _LOGGER.info('The suite %s is now beeing upgraded.', suite)
            pyhassbian.manage_suite('upgrade', suite, dev, beta, version)
            _LOGGER.info('The suite %s has been upgraded.', suite)
        else:
            _LOGGER.error('The suite %s does not exist.', suite)

    def upgrade_os_service(call):
        """Define update base OS service."""
        _LOGGER.info('Upgrade of the base OS are starting.')
        pyhassbian.os_upgrade()
        _LOGGER.info('Upgrade of the base OS are done.')

    if pyhassbian.is_installed():
        _LOGGER.info('hassbian-config found, registering services.')
        hass.services.register(DOMAIN, 'install_suite', install_suite_service)
        hass.services.register(DOMAIN, 'upgrade_suite', upgrade_suite_service)
        hass.services.register(DOMAIN, 'upgrade_os', upgrade_os_service)
    else:
        _LOGGER.error('hassbian-config not found...')
    return True
