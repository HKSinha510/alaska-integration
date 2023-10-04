import psutil
import json

class allinfo:
    cpufreq = 0
    cpuusage = 0
    

    def __init__(self) -> None:
        self.fetchallinfo()

    def fetchallinfo(self) -> dict:
        #cpu
        try:
            self.cpufreq = psutil.cpu_freq().current     #MHz
            self.cpuusage = psutil.cpu_percent()          #%
            print('g')
        except Exception as E:
            print(E)

    def group_values(self) -> dict:
        class_var = vars(allinfo)
        stat = {}
        for key, value in class_var.items():
            stat[key] = value

        return stat

if __name__ == '__main__':
    print(allinfo.group_values(allinfo()))