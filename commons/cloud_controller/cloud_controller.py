import json
import time
from commons.cloud_controller.api import CloudAPI
from commons.cloud_controller.utils import generate_signature_vpc,beijing_to_timestamp

class IoTCloud:
    def __init__(self, config):
        self.config= config   
        self.device_id = config.get('DEVICE', 'device_id')
        self.device_model = config.get('DEVICE', 'device_model')

        self.api = CloudAPI(
            config.get('Account', 'user'),
            config.get('Account', 'password'),
            config.get('Account', 'api-key'),
            config.get('CLOUD', 'iot_v3_service_url'),
            config.get('Account', 'auth_url'),
            config.get('Account', 'api-key-id'),
        )
        self.access_token, self.refresh_token = self._get_access_token()
       
    # 向云端上报属性 然后云端向固件设置属性
    def set_property(self, property_name, value, tid):
        ts = int(round(time.time()*1000))
        # tid = ts % 65535 + 1   # 产生一段时间内不会重复的 1~65535 之间的随机数
        try:
            request_body = {
                             "targetInfo": {
                                             "id": self.device_id,
                                             "model": self.device_model
                             },
                             "payload": {
                                         "ver": 1,
                                         "tid": tid,
                                         "ts": ts,
                                         "cmd": "set_property",
                                         "props": {                
                                                    property_name: value
                                         }
                             }
            }
            signature = generate_signature_vpc(self.access_token, json.dumps(request_body).encode('utf-8'),
                                               self.config.get('Account', 'api-key'))
            headers = {"requestid": "webservice_script", "access_token": self.access_token,
                       "Signature2": signature}
            res = self.api.set_property(request_body, headers)
            return res
        except Exception as e:
            print(f"Failed to set property: {e}")

    # 向云端上报指令 然后云端向固件跑指令
    def run_action(self, action_name, params_dict,tid):
        ts = int(round(time.time()*1000))
        # tid = ts % 65535 + 1   # 产生一段时间内不会重复的 1~65535 之间的随机数
        try:
            request_body = {
                            "targetInfo": {
                                            "id": self.device_id,  
                                            "model": self.device_model  
                                          },
                            "payload": {
                                         "ver": 1,
                                
                                         "tid": tid,
                                         "ts": ts,
                                         "cmd": "run_action",
                                         "action": action_name,  
                                         "params": params_dict
                            }
            }
            signature = generate_signature_vpc(self.access_token, json.dumps(request_body).encode('utf-8'),
                                               self.config.get('Account', 'api-key'))
            headers = {"requestid": "webservice_script", "access_token": self.access_token,
                       "Signature2": signature}
            res = self.api.run_action(request_body, headers)
         
        except Exception as e:
            print(f"Failed to run action: {e}")

    #### 从云端获取属性
    def get_property(self,property):
        try:
            ts = int(round(time.time()*1000))
            request_body = {
                             "targetInfo": {
                                             "id": self.device_id,
                                             "model": self.device_model
                             },
                             "payload": {
                                         "ver": 1,
                                         "tid": 0,
                                         "ts": ts,
                                         "cmd": "get_property",  
                                         "props": [
                                            property
                                            # "iot-device::iot-state", 
                                            #  # "battery::working_status",
                                            #  "battery::battery-level",
                                            #  "iot-device::log-level",                          
                                         ]
                             }
            }
            signature = generate_signature_vpc(self.access_token, json.dumps(request_body).encode('utf-8'),
                                               self.config.get('Account', 'api-key'))
            headers = {"requestid": "webservice_script", "access_token": self.access_token,
                       "Signature2": signature}
            res = self.api.get_property(request_body, headers)  # res就是从云端读取到的json格式的Response
            return res
            # if res.get("code") == '1':
            #    pass
            # else:
            #   print(f"get_property failed!")
        except Exception as e:
            print(f"Failed to get property: {e}")

    #### 从云端获取事件历史
    def get_event_history(self,event_name):
        try:
            # start_timestamp = beijing_to_timestamp(str(start_time).strip())
            # end_timestamp = beijing_to_timestamp(str(end_time).strip())
          
            now = int(time.time() * 1000)
            start_timestamp = now - 30 * 1000  # 取最近30s的事件
            end_timestamp = now + 3000

            request_body = {
                           
                            "device_id": self.device_id,
                            "device_model": self.device_model,
                            # 要获取的事件名称列表
                            "event_names":[
                               event_name
                            ],
                            "start_time":start_timestamp,
                            "end_time":end_timestamp,
                            "page": 0,  # 页数
                            "size": 1  # 条数
                             
            }
            signature = generate_signature_vpc(self.access_token, json.dumps(request_body).encode('utf-8'),
                                               self.config.get('Account', 'api-key'))
            headers = {"requestid": "webservice_script", "access_token": self.access_token,
                       "Signature2": signature}
            res = self.api.get_event_history(request_body, headers)  # res就是从云端读取到的json格式的Response
            # print(res)
            return res
            # if res.get("code") == '1':
            #     pass
            # else:
            #     print(f"get_event_history failed!")
        except Exception as e:
            print(f"Failed to get_event_history: {e}")
 
    def _get_access_token(self):
        response = self.api.get_access_token()
        return response.get("access_token"), response.get("refresh_token")
    
 