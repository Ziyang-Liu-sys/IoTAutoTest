import jsonpath
import json
import ast
def extract_state(resp:dict, prop_key):
    try:
        payload = resp.get("data")
        state_value = payload.get("props")[prop_key]
        return state_value
    except (json.JSONDecodeError, AttributeError) as e:
        print("提取失败:", e)
        return None
    
def extract_event(payload:dict):
    try:
        event_name = payload.get("event")
        params = payload.get("params")
        if isinstance(params, str):
            try:
                params = ast.literal_eval(params)  
            except Exception as e:
                print("params 解析失败:", e)
                return event_name, {}
        # 移除 key 和 value 的包裹引号
        event_params = {}
        for k, v in params.items():
            k_clean = k.strip("'\"")
            if isinstance(v, str):
                v_clean = v.strip("'\"")
            else:
                v_clean = v
            event_params[k_clean] = v_clean
        return event_name, event_params
    except (json.JSONDecodeError, AttributeError) as e:
        print("提取失败:", e)
        return None, None
    
def extract_set_property(json_str,set_property_name):
    try:
        data = json.loads(json_str)
        payload = data.get("payload")
        props = payload.get("props")
        set_property_value = props.get(set_property_name)
        tid = payload.get("tid")
        return set_property_name, set_property_value, tid
    except (json.JSONDecodeError, AttributeError) as e:
        print("提取失败:", e)
        return None, None, None
    
def extract_run_action(json_str):
    try:
        data = json.loads(json_str)
        payload = data.get("payload")
        action_name = payload.get("action")
        action_params = payload.get("params")
        tid = payload.get("tid")
        return action_name, action_params, tid
    except (json.JSONDecodeError, AttributeError) as e:
        print("提取失败:", e)
        return None, None, None