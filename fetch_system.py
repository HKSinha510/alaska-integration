import psutil, json
from datetime import datetime

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

class allinfo:
    cpufreq = 0
    cpuusage = 0
    memper = 0
    stat = {}
    json_stat = {}

    def __init__(self) -> None:
        self.fetchcpu()
        self.fetchmemory()
        self.group_values()

    def fetchcpu(self) -> None:
        try:
            self.cpufreq = psutil.cpu_freq().current     #MHz       cpu frequency
            self.cpuusage = psutil.cpu_percent()          #%        cpu current ussage percentage 
        except Exception as e:
            print(e)

    def fetchmemory(self) -> None:
        try:
            self.memper = psutil.virtual_memory().percent        #%      memory ussage percentage

        except Exception as e:
            print(e)

    def fetchdisk(self) -> None:
        try:
            #self.disk = calculate after adding file saving                          https://thepythoncode.com/article/get-hardware-system-information-python
            pass

        except Exception as e:
            print(e)

    def group_values(self) -> dict:
        class_vars = vars(self)

        for variable, value in class_vars.items():
            if variable not in ['stat', 'json_stat']:
                self.stat[variable] = value

        self.stat['time'] = str(datetime.now())
    
    def store_files(self):
        fn = open('newdata.json', 'w+')
        fo = open('olddata.json', 'w+')

        json.dump(self.json_stat, fn)

        #fn.write(str(self.stat))


if __name__ == '__main__':
    inst = allinfo()
    print(inst.group_values())
    print(inst.json_stat)
    inst.store_files()