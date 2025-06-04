from commons.simulator_controller import SimulatorController
from typing import Callable

UPDATE_STATE_HANDLERS:dict[str, Callable[[SimulatorController, any], None]] = {
    
    "battery_level": lambda sim, value: sim.update_battery_level(value),
    
}

REPORT_EVENT_HANDLERS:dict[str, Callable[[SimulatorController, any], None]] = {
    
    "lock_door_event": lambda sim, value: sim.report_door_state(value),
    "ring_doorbell_event": lambda sim, value: sim.report_ring_doorbell(value),
    "battery_low_battery": lambda sim, value: sim.report_low_battery_alarm(value),
    "lock_door_abnormal": lambda sim, value: sim.report_door_abnormal_alarm(value),
    "lock_wrong_attempts_warning_passcode": lambda sim, value: sim.report_wrong_attempts_warning_passcode(value),
    "lock_wrong_attempts_warning_palm": lambda sim, value: sim.report_wrong_attempts_warning_palm(value),
    "lock_lock_abnormal": lambda sim, value: sim.report_lock_lock_abnormal(value),
    "lock_lock_event": lambda sim, value: sim.report_lock_lock_event(value),
    "lock_unlock_event": lambda sim, value: sim.report_lock_unlock_event(value),
    "lock_passcode_event": lambda sim, value: sim.report_lock_passcode_event(value),
    "lock_palm_vein_event": lambda sim, value: sim.report_lock_palm_vein_event(value),
}