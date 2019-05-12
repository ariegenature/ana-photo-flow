"""Tests for ana_photo_flow."""

import os.path


_DATA_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
MOCK_CONFIG_DIRS = [os.path.join(_DATA_FOLDER, 'etc', 'xdg')]
MOCK_CONFIG_HOME = os.path.join(_DATA_FOLDER, 'home', '.config')
MOCK_ANA_PHOTO_FLOW_CONF = os.path.join(_DATA_FOLDER, 'custom_config_folder',
                                        'ana_photo_flow.conf')
