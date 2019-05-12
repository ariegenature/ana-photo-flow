"""ana_photo_flow main package."""

import logging


__version__ = '0.1.0-dev2'
__author__ = 'Yann Voté <ygversil@lilo.org>'
__all__ = []


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
