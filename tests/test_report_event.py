import allure
from commons.yaml_utils import load_yaml
from commons.runner_utils import report_event_runner
import pytest

@allure.epic('iot自动化测试')
@allure.feature('report_event测试')
@allure.story('ring-doorbell::ring-doorbell测试')
@pytest.mark.ring_doorbell_ring_doorbell
def test_report_event_ring_doorbell_ring_doorbell(simulator):
    
    my_val = {}
    data = load_yaml("tests/report_event_yaml/test_report_event_ring_doorbell_ring_doorbell.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            report_event_runner(simulator,k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('report_event测试')
@allure.story('lock::door-event测试')
@pytest.mark.lock_door_event
def test_report_event_lock_door_event(simulator):
    
    my_val = {}
    data = load_yaml("tests/report_event_yaml/test_report_event_lock_door_event.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            report_event_runner(simulator,k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('report_event测试')
@allure.story('battery::low-battery测试')
@pytest.mark.battery_low_battery
def test_report_event_battery_low_battery(simulator):
    
    my_val = {}
    data = load_yaml("tests/report_event_yaml/test_report_event_battery_low_battery.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            report_event_runner(simulator,k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('report_event测试')
@allure.story('lock::door-abnormal测试')
@pytest.mark.lock_door_abnormal
def test_report_event_lock_door_abnormal(simulator):
    
    my_val = {}
    data = load_yaml("tests/report_event_yaml/test_report_event_lock_door_abnormal.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            report_event_runner(simulator,k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('report_event测试')
@allure.story('lock::wrong-attempts-warning-passcode测试')
@pytest.mark.lock_wrong_attempts_warning_passcode
def test_report_event_lock_wrong_attempts_warning_passcode(simulator):
    
    my_val = {}
    data = load_yaml("tests/report_event_yaml/test_report_event_lock_wrong_attempts_warning_passcode.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            report_event_runner(simulator,k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('report_event测试')
@allure.story('lock::wrong-attempts-warning-palm测试')
@pytest.mark.lock_wrong_attempts_warning_palm
def test_report_event_lock_wrong_attempts_warning_palm(simulator):
    
    my_val = {}
    data = load_yaml("tests/report_event_yaml/test_report_event_lock_wrong_attempts_warning_palm.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            report_event_runner(simulator,k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('report_event测试')
@allure.story('lock::lock-abnormal测试')
@pytest.mark.lock_lock_abnormal
def test_report_event_lock_lock_abnormal(simulator):
    
    my_val = {}
    data = load_yaml("tests/report_event_yaml/test_report_event_lock_lock_abnormal.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            report_event_runner(simulator,k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('report_event测试')
@allure.story('lock::lock-event测试')
@pytest.mark.lock_lock_event
def test_report_event_lock_lock_event(simulator):
    
    my_val = {}
    data = load_yaml("tests/report_event_yaml/test_report_event_lock_lock_event.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            report_event_runner(simulator,k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('report_event测试')
@allure.story('lock::unlock-event测试')
@pytest.mark.lock_unlock_event
def test_report_event_lock_unlock_event(simulator):
    
    my_val = {}
    data = load_yaml("tests/report_event_yaml/test_report_event_lock_unlock_event.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            report_event_runner(simulator,k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('report_event测试')
@allure.story('lock::passcode-event测试')
@pytest.mark.lock_passcode_event
def test_report_event_lock_passcode_event(simulator):
    
    my_val = {}
    data = load_yaml("tests/report_event_yaml/test_report_event_lock_passcode_event.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            report_event_runner(simulator,k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('report_event测试')
@allure.story('lock::palm-vein-event测试')
@pytest.mark.lock_palm_vein_event
def test_report_event_lock_palm_vein_event(simulator):
    
    my_val = {}
    data = load_yaml("tests/report_event_yaml/test_report_event_lock_palm_vein_event.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            report_event_runner(simulator,k,v,my_val)