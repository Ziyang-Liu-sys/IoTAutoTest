from commons.simulator_controller import SimulatorController
from commons.cloud_controller.cloud_controller import IoTCloud
from commons.cloud_controller.config import Config
from commons.extract_utils import extract_set_property,extract_run_action
from commons.utils import wait_for_cloud_state_update,wait_for_cloud_event_update,wait_for_sim_stdout_update,wait_for_cloud_push_ready
from commons.sim_handlers import UPDATE_STATE_HANDLERS,REPORT_EVENT_HANDLERS

def update_state_runner(sim:SimulatorController,k:str,v:dict,my_val:dict):
    match k:
        case "request":
            update_state_name = v.get("update_state_name")
            update_state_value = v.get("update_state_value")
            handler = UPDATE_STATE_HANDLERS.get(update_state_name)
            handler(sim,update_state_value)
            my_val["expected_result"] = update_state_value   
        case "receive":
            config = Config()
            cloud = IoTCloud(config)
            property_name = v.get("get_property")
            expected = my_val.get("expected_result")  
            my_val["actual_result"] = wait_for_cloud_state_update(cloud, property_name, expected)
        case "check":
            actual_value = my_val["actual_result"]
            expected_value = v.get("expected_result")
            print("\n")
            print(actual_value)
            print(expected_value)
            assert actual_value == expected_value  


def report_event_runner(sim:SimulatorController,k:str,v:dict,my_val:dict):
     match k:
        case "request":
            report_event_name = v.get("report_event_name")
            report_event_params = v.get("report_event_params")
            handler = REPORT_EVENT_HANDLERS.get(report_event_name)
            handler(sim,report_event_params)
        case "receive":
            config = Config()
            cloud = IoTCloud(config)
            get_event = v.get("get_event")
            event_name,event_params = wait_for_cloud_event_update(cloud,get_event)
            my_val["actual_event_name"] = event_name
            my_val["actual_event_params"] = event_params
        case "check":
            actual_event_name = my_val["actual_event_name"]
            actual_event_params = my_val["actual_event_params"]
            expected_event_name = v.get("expected_event_name_result")
            expected_event_params = v.get("expected_event_params_result")
            print("\n")
            print(actual_event_name)
            print(expected_event_name)
            print(actual_event_params)
            print(expected_event_params)
            assert (
                    actual_event_name == expected_event_name and
                    actual_event_params == expected_event_params
                )

def set_property_runner(k:str,v:dict,my_val:dict):
    match k:
        case "request":
            config = Config()
            cloud = IoTCloud(config)
            set_property_name = v.get("set_property_name")
            set_property_value = v.get("set_property_value")
            tid = v.get("tid")
            cloud.set_property(set_property_name, set_property_value, tid)
        case "receive":
            msg = wait_for_cloud_push_ready()
            # print("收到数据：", msg.decode().strip())
            set_property_name = v.get("set_property_name")
            name, value, tid = extract_set_property(msg,set_property_name)
            my_val["actual_set_property_name"] = name
            my_val["actual_set_property_value"] = value
            my_val["actual_tid"] = tid     
        case "check":
            expected_set_property_name = v.get("expected_set_property_name")
            expected_set_property_value = v.get("expected_set_property_value")
            expected_tid = v.get("expected_tid")
            actual_set_property_name = my_val["actual_set_property_name"] 
            actual_set_property_value = my_val["actual_set_property_value"] 
            actual_tid = my_val["actual_tid"]
            print("\n")
            print(expected_set_property_name)
            print(actual_set_property_name)
            print(expected_set_property_value)
            print(actual_set_property_value)
            print(expected_tid)
            print(actual_tid)
            assert (
                    expected_tid == actual_tid and
                    expected_set_property_name == actual_set_property_name and
                    expected_set_property_value == actual_set_property_value
                )
           
def run_action_runner(k:str,v:dict,my_val:dict):
     match k:
        case "request":
            config = Config()
            cloud = IoTCloud(config)
            run_action_name = v.get("run_action_name")
            run_action_params = v.get("run_action_params")
            tid = v.get("tid")
            cloud.run_action(run_action_name, run_action_params, tid)
        case "receive":
            msg = wait_for_cloud_push_ready()
            # print("收到数据：", msg.decode().strip())
            name, params, tid = extract_run_action(msg)
            my_val["actual_run_action_name"] = name
            my_val["actual_run_action_params"] = params
            my_val["actual_tid"] = tid
        case "check":
            expected_run_action_name = v.get("expected_run_action_name")
            expected_run_action_params = v.get("expected_run_action_params")
            expected_tid = v.get("expected_tid")
            actual_run_action_name = my_val["actual_run_action_name"] 
            actual_run_action_params = my_val["actual_run_action_params"] 
            actual_tid = my_val["actual_tid"]
            print("\n")
            print(expected_run_action_name)
            print(actual_run_action_name)
            print(expected_run_action_params)
            print(actual_run_action_params)
            print(expected_tid)
            print(actual_tid)
            assert (
                expected_tid == actual_tid and
                expected_run_action_name == actual_run_action_name and
                expected_run_action_params == actual_run_action_params
                )

def run_action_connect_state_runner(sim:SimulatorController,k:str,v:dict,my_val:dict):
     match k:
        case "request":
            config = Config()
            cloud = IoTCloud(config)
            run_action_name = v.get("run_action_name")
            run_action_params = v.get("run_action_params")
            tid = v.get("tid")
            cloud.run_action(run_action_name, run_action_params, tid)
        case "receive":
            output = wait_for_sim_stdout_update(sim)
            my_val["sim_stdout"] = output
        case "check":
            sim_stdout_msg = my_val["sim_stdout"]
            expected_token1 = v.get("expected_token1")
            expected_token2 = v.get("expected_token2")
            expected_token3 = v.get("expected_token3")
            found_token1 = False
            found_token2 = False
            found_token3 = False
            start_checking = False
            for line in sim_stdout_msg:
                if expected_token1 and expected_token1 in line:
                    print(line)
                    print(expected_token1)
                    print("-----------------------")
                    found_token1 = True
                    start_checking = True
                # 找到token1后 再开始找token2 和 token3 确保token2和token3是在server-migration后新更新的
                if start_checking:    
                    if expected_token2 and expected_token2 in line:
                        print(line)
                        print(expected_token2)
                        print("-----------------------")
                        found_token2 = True
                    if expected_token3 and expected_token3 in line:
                        print(line)
                        print(expected_token3)
                        print("-----------------------")
                        found_token3 = True
            assert (found_token1 and found_token2 and found_token3)
            
             
            
          
            

            
         