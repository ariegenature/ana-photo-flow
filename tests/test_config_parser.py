"""Suite of tests for ana_photo_flow configuration parser."""

from importlib import reload
from unittest.mock import patch
import os.path
import unittest

from ana_photo_flow import _DEFAULT_CONFIG, init_config
import ana_photo_flow  # For importlib.reload function

_DATA_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
_MOCK_CONFIG_DIRS = [os.path.join(_DATA_FOLDER, 'etc', 'xdg')]
_MOCK_CONFIG_HOME = os.path.join(_DATA_FOLDER, 'home', '.config')
_MOCK_ANA_PHOTO_FLOW_CONF = os.path.join(_DATA_FOLDER, 'custom_config_folder',
                                         'ana_photo_flow.conf')


class TestChainConfig(unittest.TestCase):
    """Tests about the configuration override chain."""

    def test_default_config(self):
        """Check that if no config file exists, then default config is used."""
        reload(ana_photo_flow)
        with init_config() as config:
            for section, subconfig in _DEFAULT_CONFIG.items():
                for key, value in subconfig.items():
                    self.assertEqual(config[section][key], value)

    @patch('xdg.XDG_CONFIG_DIRS', new=_MOCK_CONFIG_DIRS)
    def test_only_global_config(self):
        """Check that if only global config file exists, then it is used."""
        reload(ana_photo_flow)
        with init_config() as config:
            self.assertEqual(config['celery']['broker_url'],
                             'amqp://global_user:global_password@global_host/global_vhost')
            self.assertEqual(config['celery']['result_backend'],
                             'redis://:global_password@global_host')
            self.assertEqual(config['celery']['worker_log_format'],
                             _DEFAULT_CONFIG['celery']['worker_log_format'])

    @patch('xdg.XDG_CONFIG_HOME', new=_MOCK_CONFIG_HOME)
    def test_only_local_config(self):
        """Check that if only local config file exists, then it is used."""
        reload(ana_photo_flow)
        with init_config() as config:
            self.assertEqual(config['celery']['broker_url'],
                             'amqp://local_user:local_password@local_host/local_vhost')
            self.assertEqual(config['celery']['result_backend'],
                             'redis://:local_password@local_host')
            self.assertEqual(config['celery']['worker_log_format'],
                             _DEFAULT_CONFIG['celery']['worker_log_format'])

    @patch.dict('ana_photo_flow.os.environ', {'ANA_PHOTO_FLOW_CONF': _MOCK_ANA_PHOTO_FLOW_CONF})
    def test_only_env_config(self):
        """Check that if only config file given by environment varialbe exists, then it is used."""
        reload(ana_photo_flow)
        with init_config() as config:
            self.assertEqual(config['celery']['broker_url'],
                             'amqp://env_user:env_password@env_host/env_vhost')
            self.assertEqual(config['celery']['result_backend'],
                             'redis://:env_password@env_host')
            self.assertEqual(config['celery']['worker_log_format'],
                             _DEFAULT_CONFIG['celery']['worker_log_format'])


if __name__ == '__main__':
    unittest.main()
