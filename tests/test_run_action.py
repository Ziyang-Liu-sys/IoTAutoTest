import allure
from commons.yaml_utils import load_yaml
from commons.runner_utils import run_action_runner
import pytest

@allure.epic('iot自动化测试')
@allure.feature('run_action测试')
@allure.story('lock::lock测试')
@pytest.mark.lock_lock
def test_run_action_lock_lock(simulator):
    
    my_val = {}
    data = load_yaml("tests/run_action_yaml/test_run_action_lock_lock.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_runner(k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('run_action测试')
@allure.story('lock::unlock测试')
@pytest.mark.lock_unlock
def test_run_action_lock_unlock(simulator):
    
    my_val = {}
    data = load_yaml("tests/run_action_yaml/test_run_action_lock_unlock.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_runner(k,v,my_val)


@allure.epic('iot自动化测试')
@allure.feature('run_action测试')
@allure.story('lock::lock-install-mode-check测试')
@pytest.mark.lock_lock_install_mode_check
def test_run_action_lock_lock_install_mode_check(simulator):
    
    my_val = {}
    data = load_yaml("tests/run_action_yaml/test_run_action_lock_lock_install_mode_check.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_runner(k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('run_action测试')
@allure.story('lock::gyroscope-calibration测试')
@pytest.mark.lock_gyroscope_calibration
def test_run_action_lock_gyroscope_calibration(simulator):
    
    my_val = {}
    data = load_yaml("tests/run_action_yaml/test_run_action_lock_gyroscope_calibration.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_runner(k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('run_action测试')
@allure.story('lock::add-passcode测试')
@pytest.mark.lock_add_passcode
def test_run_action_lock_add_passcode(simulator):
    
    my_val = {}
    data = load_yaml("tests/run_action_yaml/test_run_action_lock_add_passcode.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_runner(k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('run_action测试')
@allure.story('lock::delete-passcode测试')
@pytest.mark.lock_delete_passcode
def test_run_action_lock_delete_passcode(simulator):
    
    my_val = {}
    data = load_yaml("tests/run_action_yaml/test_run_action_lock_delete_passcode.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_runner(k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('run_action测试')
@allure.story('lock::add-palm-vein测试')
@pytest.mark.lock_add_palm_vein
def test_run_action_lock_add_palm_vein(simulator):
    
    my_val = {}
    data = load_yaml("tests/run_action_yaml/test_run_action_lock_add_palm_vein.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_runner(k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('run_action测试')
@allure.story('lock::delete-palm-vein测试')
@pytest.mark.lock_delete_palm_vein
def test_run_action_lock_delete_palm_vein(simulator):
    
    my_val = {}
    data = load_yaml("tests/run_action_yaml/test_run_action_lock_delete_palm_vein.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_runner(k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('run_action测试')
@allure.story('lock::add-one-time-code测试')
@pytest.mark.lock_add_one_time_code
def test_run_action_lock_add_one_time_code(simulator):
    
    my_val = {}
    data = load_yaml("tests/run_action_yaml/test_run_action_lock_add_one_time_code.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_runner(k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('run_action测试')
@allure.story('lock::get-one-time-code测试')
@pytest.mark.lock_get_one_time_code
def test_run_action_lock_get_one_time_code(simulator):
    
    my_val = {}
    data = load_yaml("tests/run_action_yaml/test_run_action_lock_get_one_time_code.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_runner(k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('run_action测试')
@allure.story('lock::clear-one-time-code测试')
@pytest.mark.lock_clear_one_time_code
def test_run_action_lock_clear_one_time_code(simulator):
    
    my_val = {}
    data = load_yaml("tests/run_action_yaml/test_run_action_lock_clear_one_time_code.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_runner(k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('run_action测试')
@allure.story('iot-device::restart测试')
@pytest.mark.iot_device_restart
def test_run_action_iot_device_restart(simulator):
    
    my_val = {}
    data = load_yaml("tests/run_action_yaml/test_run_action_iot_device_restart.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_runner(k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('run_action测试')
@allure.story('iot-device::upgrade-2测试')
@pytest.mark.iot_device_upgrade_2
def test_run_action_iot_device_upgrade_2(simulator):
    
    my_val = {}
    data = load_yaml("tests/run_action_yaml/test_run_action_iot_device_upgrade_2.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_runner(k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('run_action测试')
@allure.story('iot-device::submit-log测试')
@pytest.mark.iot_device_submit_log
def test_run_action_iot_device_submit_log(simulator):
    
    my_val = {}
    data = load_yaml("tests/run_action_yaml/test_run_action_iot_device_submit_log.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_runner(k,v,my_val)

@allure.epic('iot自动化测试')
@allure.feature('run_action测试')
@allure.story('iot-device::reset测试')
@pytest.mark.iot_device_reset
def test_run_action_iot_device_reset(simulator):
    
    my_val = {}
    data = load_yaml("tests/run_action_yaml/test_run_action_iot_device_reset.yaml")
    # print(data)
    allure.title(data["name"])
    for step in data["steps"]:
        for k,v in step.items():
            run_action_runner(k,v,my_val)