"""ana_photo_flow main package."""

from collections import ChainMap
import configparser
import contextlib
import logging
import os
import os.path
import traceback

from celery import Celery
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


@contextlib.contextmanager
def init_config():
    """Context manager initializing a configuration dictionary on enter and cleaning it up on exit.

    The context manager returns the configuration dictionary.
    """
    config = ChainMap(_DEFAULT_CONFIG)
    cfgparser = configparser.ConfigParser()
    for cfgfname in _CONFIG_LOCATIONS:
        if not cfgfname or not os.path.isfile(cfgfname):
            continue
        cfgparser.read(cfgfname)
        newconfig = {section: _DEFAULT_CONFIG[section].copy() for section in cfgparser.sections()}
        for section in cfgparser.sections():
            newconfig[section].update(dict(cfgparser.items(section)))
        config = config.new_child(newconfig)
    yield config
    config = {}


@contextlib.contextmanager
def init_app():
    """Context manager initializing application on enter and shutting it down properly on exit.

    The context manager returns the application object.
    """
    with init_config() as config:
        logger = logging.getLogger()
        logger.info('Starting ana_photo_flow...')
        celery_config = config['celery']
        app = Celery('ana_photo_flow')
        app.conf.update(celery_config)
        logger.debug('Celery started with following configuration:\n%s', app.conf.humanize())
        try:
            yield app
        except Exception as err:
            traceback.print_tb(err.__traceback__)
            logging.error(str(err))
        except KeyboardInterrupt:
            logger.debug('Terminating as requested...')
        finally:
            logger.info('ana_photo_flow finished.')
            logging.shutdown()
