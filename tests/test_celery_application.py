"""Suite of tests for ana_photo_flow Celery application."""

import unittest

from ana_photo_flow import _DEFAULT_CONFIG, init_app


class TestApplicationConfig(unittest.TestCase):
    """Tests about the application configuration."""

    def test_default_config(self):
        """Check that if no config file exists, then default config is used."""
        with init_app() as app:
            conf_pairs = list(app.conf.items()).copy()
        for pair in _DEFAULT_CONFIG['celery'].items():
            self.assertIn(pair, conf_pairs)
