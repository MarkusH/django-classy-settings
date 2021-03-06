import os
import unittest
import cbs


class TestEnv(unittest.TestCase):

    def setUp(self):
        os.environ.clear()
        cbs.DEFAULT_ENV_PREFIX = ''

    def test_retrieve_from_method(self):
        class Settings:
            @cbs.env
            def SETTING(self):
                return 'bar'

        self.assertEqual(Settings().SETTING, 'bar')

    def test_retrieve_from_env(self):
        class Settings:
            @cbs.env
            def SETTING(self):
                return 'bar'

        os.environ['SETTING'] = 'foo'
        self.assertEqual(Settings().SETTING, 'foo')

    def test_retrieve_from_env_specifying_key(self):
        class Settings:
            @cbs.env(key='DJANGO_SETTING')
            def SETTING(self):
                return 'bar'

        os.environ['DJANGO_SETTING'] = 'foo'
        self.assertEqual(Settings().SETTING, 'foo')

    def test_retrieve_from_env_specifying_prefix(self):
        class Settings:
            @cbs.env(prefix='DJANGO_')
            def SETTING(self):
                return 'bar'

        os.environ['DJANGO_SETTING'] = 'foo'
        self.assertEqual(Settings().SETTING, 'foo')

    def test_default_env_prefix(self):
        cbs.DEFAULT_ENV_PREFIX = 'DJANGO_'

        class Settings:
            @cbs.env
            def SETTING(self):
                return 'bar'

        os.environ['DJANGO_SETTING'] = 'foo'
        self.assertEqual(Settings().SETTING, 'foo')

    def test_refer_to_other_setting(self):

        class Settings:
            OTHER = True

            @cbs.env
            def SETTING(self):
                return self.OTHER

        self.assertEqual(Settings().SETTING, True)
