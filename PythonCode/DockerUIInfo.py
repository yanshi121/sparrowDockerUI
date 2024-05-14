import docker
import psutil
import requests
import pwd


class DockerUIInfo(object):
    def __init__(self):
        self.docker_env = docker.from_env()
        self.docker_version = self.docker_env.version()

    def refresh_docker_information(self):
        self.docker_env = docker.from_env()
        self.docker_version = self.docker_env.version()

    def docker_info(self):
        self.refresh_docker_information()
        docker_platform = self.docker_version['Platform']['Name']
        docker_os = self.docker_version['Os']
        docker_arch = self.docker_version['Arch']
        docker_version = self.docker_version['Version']
        docker_api_version = self.docker_version['ApiVersion']
        docker_min_API_version = self.docker_version['MinAPIVersion']
        docker_git_commit = self.docker_version['GitCommit']
        docker_go_version = self.docker_version['GoVersion']
        docker_kernel_version = self.docker_version['KernelVersion']
        docker_build_time = self.docker_version['BuildTime']
        return {
            "docker_platform": docker_platform,
            "docker_os": docker_os,
            "docker_arch": docker_arch,
            "docker_version": docker_version,
            "docker_api_version": docker_api_version,
            "docker_min_API_version": docker_min_API_version,
            "docker_git_commit": docker_git_commit,
            "docker_go_version": docker_go_version,
            "docker_kernel_version": docker_kernel_version,
            "docker_build_time": docker_build_time
        }

    def system_info_cpu(self):
        # CPU逻辑数量
        cpu_count = psutil.cpu_count()
        # CPU物理核心
        cpu_count_logical = psutil.cpu_count(logical=False)
        return {
            "cpu_count": cpu_count,
            "cpu_count_logical": cpu_count_logical
        }
    
    def system_info_cpu_percent(self):
        # interval：每隔0.5s刷新一次
        # percpu：查看所有的cpu使用率
        cpu_percent = psutil.cpu_percent(interval=0.5, percpu=True)
        return {
            "cpu_percent": cpu_percent
        }
    
    def system_info_virtual(self):
        # 输出总内存
        virtual_memory_total = round(psutil.virtual_memory()[0] / 1024 /1024, 2)
        # 输出可用内存
        virtual_memory_available = round(psutil.virtual_memory()[1] / 1024 /1024, 2)
        # 输出内存使用率
        virtual_memory_percent = psutil.virtual_memory()[2]
        # 输出已使用内存
        virtual_memory_used = round(psutil.virtual_memory()[3] / 1024 /1024, 2)
        return {
            "virtual_memory_total": virtual_memory_total,
            "virtual_memory_available": virtual_memory_available,
            "virtual_memory_percent": virtual_memory_percent,
            "virtual_memory_used": virtual_memory_used
        }
    
    def system_info_disk(self):
        # 磁盘分区信息
        disk_partitions = psutil.disk_partitions()
        # 磁盘总大小
        disk_usage_total = round(psutil.disk_usage('/')[0] / 1024 /1024 /1024, 2)
        # 磁盘已使用大小
        disk_usage_used = round(psutil.disk_usage('/')[1] / 1024 /1024 /1024, 2)
        # 磁盘剩余大小
        disk_usage_free = round(psutil.disk_usage('/')[2] / 1024 /1024 /1024, 2)
        # 磁盘使用率
        disk_usage_percent = psutil.disk_usage('/')[3]
        return {
            "disk_partitions": disk_partitions,
            "disk_usage_total": disk_usage_total,
            "disk_usage_used": disk_usage_used,
            "disk_usage_free": disk_usage_free,
            "disk_usage_percent": disk_usage_percent
        }
    
    def system_info_net(self):
        # 查询网络发送的字节数
        net_io_counters_bytes_sent = psutil.net_io_counters()[0]
        # 查询网络接收的字节数
        net_io_counters_bytes_recv = psutil.net_io_counters()[1]
        # 查询网络发送的包数据量
        net_io_counters_packets_sent = psutil.net_io_counters()[2]
        # 查询网络接收的包数据量
        net_io_counters_packets_recv = psutil.net_io_counters()[3]
        # 查询网络接收包时, 出错的次数
        net_io_counters_err_in = psutil.net_io_counters()[4]
        # 查询网络发送包时, 出错的次数
        net_io_counters_err_out = psutil.net_io_counters()[5]
        # 查询网络接收包时, 丢弃的次数
        net_io_counters_drop_in = psutil.net_io_counters()[6]
        # 查询网络发送包时, 丢弃的次数
        net_io_counters_drop_out = psutil.net_io_counters()[7]
        return {
            "net_io_counters_bytes_sent": net_io_counters_bytes_sent,
            "net_io_counters_bytes_recv": net_io_counters_bytes_recv,
            "net_io_counters_packets_sent": net_io_counters_packets_sent,
            "net_io_counters_packets_recv": net_io_counters_packets_recv,
            "net_io_counters_err_in": net_io_counters_err_in,
            "net_io_counters_err_out": net_io_counters_err_out,
            "net_io_counters_drop_in": net_io_counters_drop_in,
            "net_io_counters_drop_out": net_io_counters_drop_out
        }
    
    def system_info_pid(self):
        # 所有进程ID
        pids_info = []
        pids = psutil.pids()
        for pid in pids:
            # 获取指定进程
            p = psutil.Process(pid)
            # 进程名称
            name = p.name()
            # 进程的exe路径
            exe_path = p.exe()
            # 进程的工作目录
            cwd_path = p.cwd()
            memory_infos = []
            # 进程信息
            memory_info = p.memory_info()
            # 进程常驻内存大小
            memory_rss = memory_info[0]
            # 进程虚拟内存大小
            memory_vms = memory_info[1]
            # 进程共享内存
            memory_shared = memory_info[2]
            # 进程专用于可执行代码的内存量
            memory_text = memory_info[3]
            # 进程共享库使用的内存
            memory_lib = memory_info[4]
            # 进程用于非可执行代码的物理内存量
            memory_data = memory_info[5]
            # 进程脏页数
            memory_dirty = memory_info[6]
            memory_infos.append(
                {
                    "memory_rss": memory_rss,
                    "memory_vms": memory_vms,
                    "memory_shared": memory_shared,
                    "memory_text": memory_text,
                    "memory_lib": memory_lib,
                    "memory_data": memory_data,
                    "memory_dirty": memory_dirty,
                    }
                    )
            pids_info.append(
                {
                    "ID": pid, 
                    "name": name, 
                    "exe_path": exe_path, 
                    "cwd_path": cwd_path, 
                    "memory_info": memory_infos
                    }
                    )
        return {
            "pids_info": pids_info
        }
    
    def system_users(self):
        return [user.pw_name for user in pwd.getpwall()]
    
    def get_ip(self):
        res = requests.get('http://myip.ipip.net', timeout=5).text
        ip = res.split("  来自于：")[0].split("IP：")[1]
        addres = res.split("  来自于：")[1].split(" ")[0] + "-" + res.split("  来自于：")[1].split(" ")[1] + "-" + res.split("  来自于：")[1].split(" ")[2]
        shop = res.split("  来自于：")[1].split(" ")[-1].replace("\n", '')
        return {"ip":ip, "addres": addres, "shop": shop}
    
    def login_docker(self, user_name: str, user_password: str, registry="https://index.docker.io/v1/"):
        self.docker_env.login(user_name, user_password, registry)

if __name__ == '__main__':
    run = DockerUIInfo()
    print(run.system_info_pid())



