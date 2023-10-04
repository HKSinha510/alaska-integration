import psutil
import json

class allinfo:
    cpufreq = 0
    cpuusage = 0

    def __init__(self) -> None:
        self.fetchcpu()

    def fetchcpu(self) -> dict:
        try:
            self.cpufreq = psutil.cpu_freq().current     #MHz       cpu frequency
            self.cpuusage = psutil.cpu_percent()          #%        cpu current ussage percentage 
        except Exception as E:
            print(E)

    def group_values(self) -> dict:
        class_vars = vars(self)
        stat = {}

        for variable, value in class_vars.items():
            stat[variable] = value

        return stat

if __name__ == '__main__':
    inst = allinfo()
    print(inst.group_values())