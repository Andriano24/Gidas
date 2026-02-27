import os
import random
import time

from datetime import datetime

import psutil

from constants import SEPARATOR_LINE, SEPARATOR_TIMES

class Benchmark:
    def __init__(self):
        self.process = psutil.Process(os.getpid())
        num_cores = psutil.cpu_count()

        if num_cores and num_cores > 2:
            selected_core = random.randint(2, num_cores - 1)
            self.process.cpu_affinity([selected_core])
            self.cpu_core = selected_core
        else:
            self.process.cpu_affinity([0])
            self.cpu_core = 0
        
        self.process.cpu_percent()
        self.start_time = time.perf_counter()
        
        self.total_loops = 0
        self.total_snaps = 0
        
        self.cpu = [0.0, float('inf'), 0.0, 0.0]
        self.ram = [0.0, float('inf'), 0.0, 0.0]
        self.loop = [0.0, float('inf'), 0.0, 0.0]

    def update(self, start=0.0, end=0.0, force=False):
        if not force:
            duration_ms = (end - start) * 1000
            self.total_loops += 1
            self.loop[0] = duration_ms
            self.loop[1] = min(self.loop[1], duration_ms)
            self.loop[2] += duration_ms
            self.loop[3] = max(self.loop[3], duration_ms)

        if self.total_loops % 20 == 0 or force:
            self.total_snaps += 1
            cpu = self.process.cpu_percent()
            ram = self.process.memory_full_info().uss / (1024 * 1024)

            self.cpu[0] = cpu

            if cpu > 0.0:
                self.cpu[1] = min(self.cpu[1], cpu)

            self.cpu[2] += cpu
            self.cpu[3] = max(self.cpu[3], cpu)

            self.ram[0] = ram
            self.ram[1] = min(self.ram[1], ram)
            self.ram[2] += ram
            self.ram[3] = max(self.ram[3], ram)

    def get_summary(self):
        self.update(force=True)

        num_cores = psutil.cpu_count() or 1
        runtime = int(time.perf_counter() - self.start_time)
        h, r = divmod(runtime, 3600)
        m, s = divmod(r, 60)

        def get_stats(data, count, divisor=1):
            if count == 0: 
                return (0.0, 0.0, 0.0, 0.0)
            
            now = data[0] / divisor
            low = data[1]  / divisor
            avg = (data[2] / count) / divisor
            high = data[3] / divisor

            return (now, low, avg, high)

        c_now, c_min, c_avg, c_max = get_stats(self.cpu, self.total_snaps, num_cores)
        r_now, r_min, r_avg, r_max = get_stats(self.ram, self.total_snaps)
        l_now, l_min, l_avg, l_max = get_stats(self.loop, self.total_loops)
        
        print("\n" + SEPARATOR_LINE)
        print(f"{"BENCHMARK SUMMARY":^{SEPARATOR_TIMES}}")
        print(SEPARATOR_LINE)
        print(f"{f' Runtime: {h:02}:{m:02}:{s:02}':<{SEPARATOR_TIMES // 2}}{f'Core: {self.cpu_core}':>{SEPARATOR_TIMES // 2}}")
        print(f"  CPU (%)   | {c_now:>6.2f} | Low: {c_min:>6.2f} | Avg: {c_avg:>6.2f} | High: {c_max:>6.2f}")
        print(f"  RAM (MB)  | {r_now:>6.1f} | Low: {r_min:>6.1f} | Avg: {r_avg:>6.1f} | High: {r_max:>6.1f}")
        print(f"  Loop (ms) | {l_now:>6.1f} | Low: {l_min:>6.1f} | Avg: {l_avg:>6.1f} | High: {l_max:>6.1f}")
        print(f"{f' Loops: {self.total_loops}':<{SEPARATOR_TIMES // 2}}{f'Snaps: {self.total_snaps}':>{SEPARATOR_TIMES // 2}}")
        print(SEPARATOR_LINE + "\n")