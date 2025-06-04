import subprocess
import time
import threading
import queue
class SimulatorController:
    def __init__(self):
        self.process = subprocess.Popen(
            ['./build/apps/iot3_0_device_simulator/iot3_0_device_simulator_x86'],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,cwd=".."
        )
        self.output_queue = queue.Queue()
        self._start_stdout_thread()
        time.sleep(3)  # 等待模拟器初始化完成

    def _start_stdout_thread(self):
        def read_stdout():
            for line in self.process.stdout:
                if line:
                    self.output_queue.put(line.strip())
        threading.Thread(target=read_stdout, daemon=True).start()

    def get_sim_stdout(self):
        lines = []
        while not self.output_queue.empty():
            lines.append(self.output_queue.get())
        return lines
    
    def update_battery_level(self, level):
        cmd = f"update_state battery::battery-level {level}\n"
        self.process.stdin.write(cmd)
        self.process.stdin.flush()
        time.sleep(1)

    def report_door_state(self, state):
        cmd = f"report_event lock::door-event {state}\n"
        self.process.stdin.write(cmd)
        self.process.stdin.flush()
        time.sleep(1)

    def report_ring_doorbell(self, params):
        cmd = f"report_event ring-doorbell::ring-doorbell {params}\n"
        self.process.stdin.write(cmd)
        self.process.stdin.flush()
        time.sleep(1)

    def report_low_battery_alarm(self, params):
        cmd = f"report_event battery::low-battery {params}\n"
        self.process.stdin.write(cmd)
        self.process.stdin.flush()
        time.sleep(1)

    def report_door_abnormal_alarm(self, params):
        cmd = f"report_event lock::door-abnormal {params}\n"
        self.process.stdin.write(cmd)
        self.process.stdin.flush()
        time.sleep(1)

    def report_wrong_attempts_warning_passcode(self, params):
        cmd = f"report_event lock::wrong-attempts-warning-passcode {params}\n"
        self.process.stdin.write(cmd)
        self.process.stdin.flush()
        time.sleep(1)

    def report_wrong_attempts_warning_palm(self, params):
        cmd = f"report_event lock::wrong-attempts-warning-palm {params}\n"
        self.process.stdin.write(cmd)
        self.process.stdin.flush()
        time.sleep(1)

    def report_lock_lock_abnormal(self, params):
        cmd = f"report_event lock::lock-abnormal {params}\n"
        self.process.stdin.write(cmd)
        self.process.stdin.flush()
        time.sleep(1)

    def report_lock_lock_event(self, params):
        cmd = f"report_event lock::lock-event {params}\n"
        self.process.stdin.write(cmd)
        self.process.stdin.flush()
        time.sleep(1)

    def report_lock_unlock_event(self, params):
        cmd = f"report_event lock::unlock-event {params}\n"
        self.process.stdin.write(cmd)
        self.process.stdin.flush()
        time.sleep(1)

    def report_lock_passcode_event(self, params):
        cmd = f"report_event lock::passcode-event {params}\n"
        self.process.stdin.write(cmd)
        self.process.stdin.flush()
        time.sleep(1)

    def report_lock_palm_vein_event(self, params):
        cmd = f"report_event lock::palm-vein-event {params}\n"
        self.process.stdin.write(cmd)
        self.process.stdin.flush()
        time.sleep(1)

    def close(self):
        self.process.terminate()
        # output = self.process.stdout.read()
        # print("模拟器输出:", output)
        # print("模拟器退出:")

     
                      
                  
          
   