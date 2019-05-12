"""ana_photo_flow main package."""

import logging
import os
import os.path

import xdg


__version__ = '0.1.0-dev2'
__author__ = 'Yann Voté <ygversil@lilo.org>'
__all__ = []


# Where to search for config files
# Order is important: each file overrides settings from previous files in this list
_CONFIG_LOCATIONS = [
    *(os.path.join(folder, 'ana_photo_flow.conf') for folder in xdg.XDG_CONFIG_DIRS),
    os.path.join(xdg.XDG_CONFIG_HOME, 'ana_photo_flow.conf'),
    os.environ.get('ANA_PHOTO_FLOW_CONF')
]

_DEFAULT_CONFIG = {
    'celery': {
        'broker_url': 'pyamqp://guest@localhost//',
        'result_backend': 'redis://localhost',
        'worker_log_format': ('%(asctime)s %(processName)s[%(process)s]: '
                              '%(levelname)s - %(message)s'),
        'worker_task_log_format': ('%(asctime)s %(processName)s[%(process)s]: '
                                   '%(levelname)s - %(task_name)s %(task_id)s - %(message)s'),
    },
}
