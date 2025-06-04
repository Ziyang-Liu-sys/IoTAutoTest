import allure
from commons.yaml_utils import load_yaml
from commons.runner_utils import run_action_connect_state_runner
import pytest

@allure.epic('iot自动化测试')
@allure.feature('connect_state测试')
@allure.story('iot-device::server-migration测试')
@pytest.mark.iot_device_server_migration
def test_run_action_iot_device_server_migration(simulator):
    
    my_val = {}
    data = load_yaml("tests/connect_state_yaml/test_run_action_iot_device_server_migration.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_connect_state_runner(simulator,k,v,my_val)
