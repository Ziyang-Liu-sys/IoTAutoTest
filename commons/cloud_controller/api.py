import requests

from commons.cloud_controller.utils import generate_password

class CloudAPI:
    def __init__(self, user, password, api_key, base_url, auth_url, api_key_id):
        self.user = user
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.password = password
        self.auth_url = auth_url
        self.api_key_id = api_key_id

    def set_property(self, value, heasers):
        url = f"{self.base_url}/cloud/iot_v3/set_property"
        self.session.headers = heasers
        # 使用http给浏览器发送post请求
        response = self.session.post(url, json=value)
        response.raise_for_status()
        return response.json()

    def run_action(self, params, headers):
        url = f"{self.base_url}/cloud/iot_v3/send_action"
        self.session.headers = headers
        response = self.session.post(url, json=params)
        response.raise_for_status()
        return response.json()
    ####
    def get_property(self, value, heasers):
        url = f"{self.base_url}/cloud/iot_v3/get_property"
        self.session.headers = heasers
        # 使用http给浏览器发送post请求
        response = self.session.post(url, json=value)
        response.raise_for_status()
        return response.json()
    
    def get_event_history(self, value, heasers):
        url = f"{self.base_url}/cloud/iot_v3/event_history"
        self.session.headers = heasers
        # 使用http给浏览器发送post请求
        response = self.session.post(url, json=value)
        response.raise_for_status()
        return response.json()

    def get_access_token(self):
        headers = {"Keyid": self.api_key_id, "Apikey": self.api_key, "Content-Type": "application/json"}
        response = self.session.post(self.auth_url, headers=headers, json={"email": self.user, "password": generate_password(self.password)})
        response.raise_for_status()
        return response.json()

