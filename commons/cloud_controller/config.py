import configparser
import os
config_dir = os.path.dirname(os.path.abspath(__file__))


class Config:
    def __init__(self, config_file=f'{config_dir}/cloud_config.ini'):
        self.config = configparser.ConfigParser()

        # Default values
        self.config['Account'] = {
            'user': '',
            'password': '',
            'api-key': '',
            'api-key-id': '',
            'auth_url': '',

        }
        self.config['DEVICE'] = {
            'device_id': '',
            'device_model': ''
        }
        self.config['CLOUD'] = {
            'iot_v3_service_url': '',
          
        }

        if os.path.exists(config_file):
            self.config.read(config_file,encoding='utf-8')

    def get(self, section, key):
        return self.config.get(section, key)

    def get_int(self, section, key):
        return self.config.getint(section, key)
