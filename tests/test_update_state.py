import allure
from commons.yaml_utils import load_yaml
from commons.runner_utils import update_state_runner
import pytest

@allure.epic('iot自动化测试')
@allure.feature('update_state测试')
@allure.story('battery::battery-level测试')
@pytest.mark.battery_battery_level
def test_update_state_battery_battery_level(simulator):
    
    my_val = {}
    data = load_yaml("tests/update_state_yaml/test_update_state_battery_battery_level.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            update_state_runner(simulator,k,v,my_val)




