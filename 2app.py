import psutil
import time
import datetime
import os


def time_now ():
    active_time = time.time()
    print(datetime.datetime.fromtimestamp(active_time).strftime('The time is now: %Y-%m-%d %H:%M:%S'))


def time_usage():
    time_ = time.strftime("%H:%M:%S", time.gmtime(psutil.boot_time()))
    print(f"Working time: {time_}\n")


def cpu_usage(cpu : list):
    for i in range(len(cpu)):
        cpu_percent = (cpu[i] / 2)
        cpu_scale = '■' * int(cpu_percent) + '-' * (50 - int(cpu_percent))     
        print(f"Core {i + 1} |{cpu_scale}|{cpu[i]}%  ", end="\n", flush=True)
             

def mem_usage(mem : list):
    mem_total = round((mem[0] / 1024 ** 3), 2)
    mem_used = round((mem[3] / 1024 ** 3), 2)
    mem_scale = '■' * int(mem[2] / 2) + '-' * (50 - int(mem[2] / 2))
    print(f"\nMemory |{mem_scale}|{mem_used}G|{mem_total}G", flush=True)


def process_usage():
    n = 0
    print('{:-<7}'.format('PID') + '{:-<21}'.format(' USERNAME') + '{:-<13}'.format(' TIME') + '{:-<53}'.format(' NAME'))
    for proc in psutil.process_iter():
        pinfo = proc.as_dict(attrs=['pid', 'name', 'username', 'create_time'])
        time_proc = time.strftime("%H:%M:%S", time.gmtime(pinfo['create_time']))
        print('|{:<7}|'.format(pinfo['pid']) + '{:<20}|'.format(pinfo['username']) + '{:<12}|'.format(time_proc) + '{:<50}|'.format(pinfo['name']))
        
        n += 1
        if n == 40:
                break


def clear_terminal():
    os.system('clear')


while True:
    clear_terminal()
    time_now()
    time_usage()
    cpu_usage(psutil.cpu_percent(percpu=True))
    mem_usage(psutil.virtual_memory())
    process_usage()
    time.sleep(1)