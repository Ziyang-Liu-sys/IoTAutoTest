import allure
from commons.yaml_utils import load_yaml
from commons.runner_utils import set_property_runner
import pytest

@allure.epic('iot自动化测试')
@allure.feature('set_property测试')
@allure.story('iot-device::iot-power测试')
@pytest.mark.iot_device_iot_power
def test_set_property_iot_device_iot_power(simulator):
    
    my_val = {}
    data = load_yaml("tests/set_property_yaml/test_set_property_iot_device_iot_power.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            set_property_runner(k,v,my_val)


@allure.epic('iot自动化测试')
@allure.feature('set_property测试')
@allure.story('device-info::lon测试')
@pytest.mark.device_info_lon
def test_set_property_device_info_lon(simulator):
    
    my_val = {}
    data = load_yaml("tests/set_property_yaml/test_set_property_device_info_lon.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            set_property_runner(k,v,my_val)