import psutil

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

    def __init__(self) -> None:
        self.fetchcpu()
        self.fetchmemory()

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
        stat = {}

        for variable, value in class_vars.items():
            stat[variable] = value

        return stat
    
    def discord_procedure(self):
        #store data from new.json to old.json, add new data in new.json, send same copy to frontend and to discord
        pass

if __name__ == '__main__':
    inst = allinfo()
    print(inst.group_values())