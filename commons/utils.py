import time
import os
import select
from commons.cloud_controller.cloud_controller import IoTCloud
from commons.simulator_controller import SimulatorController
from commons.extract_utils import extract_state,extract_event
def wait_for_cloud_state_update(cloud:IoTCloud, key, expected, timeout=8, interval=0.5):
    start = time.time()
    while time.time() - start < timeout:
        resp = cloud.get_property(key)
        actual = extract_state(resp, key)
        if actual == expected:
            return actual
        time.sleep(interval)
    raise TimeoutError(f"Cloud did not update to expected value {expected} within {timeout} seconds.")

def wait_for_cloud_event_update(cloud:IoTCloud, key, timeout=8, interval=0.5):
    start = time.time()
    while time.time() - start < timeout:
         resp = cloud.get_event_history(key)
         data = resp.get("data")
         if data != []:
            event_name,event_params = extract_event(data[0])
            return event_name,event_params
         time.sleep(interval)
    raise TimeoutError(f"Cloud did not update to event {event_name} within {timeout} seconds.")

def wait_for_sim_stdout_update(sim:SimulatorController, timeout=10, interval=0.5):
    time.sleep(5)  # 等待标准输出的信息更新完
    start_time = time.time()
    while time.time() - start_time < timeout:
        output = sim.get_sim_stdout()
        if output:  
            return output
        time.sleep(interval)
    raise TimeoutError(f"Sim stdout did not within {timeout} seconds.")

def wait_for_cloud_push_ready(fifo_path="./tmp/msgfifo",timeout=10):
    if not os.path.exists(fifo_path):
        os.mkfifo(fifo_path)
    fifo = os.open(fifo_path, os.O_RDONLY | os.O_NONBLOCK)
    try:
        rlist, _, _ = select.select([fifo], [], [], timeout)
        if rlist:
            msg = os.read(fifo, 1024)
            return msg
        raise TimeoutError(f"cloud push ready did not within {timeout} seconds.")
    finally:
        os.close(fifo)
    
       
