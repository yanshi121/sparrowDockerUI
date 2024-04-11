import docker


class DockerUIContainers(object):
    def __init__(self):
        self.docker_env = docker.from_env()

    def refresh_docker_information(self):
        self.docker_env = docker.from_env()

    def docker_run_containers(self, image_name: str, user: str, name: str, port: dict, environment: dict or list,
                              command="/bin/bash"):
        """
        创建并运行容器
        :param image_name: 镜像名字
        :param user: 所属用户
        :param name: 容器名称
        :param port: 映射端口{“3306/tcp”：3300}，容器3306映射到主机3300
        :param environment: 设置容器环境变量，数组或字典形式，["MYSQL_ROOT_PASSWORD='123456'"]或{“MYSQL_ROOT_PASSWORD”： “123456”}
        :param command: 创建时执行的命令，默认“/bin/bash”
        :return: 创建成功返回True，失败返回错误信息
        """
        self.refresh_docker_information()
        try:
            if port == "" and environment == "" and command == "":
                self.docker_env.containers.run(image=image_name, user=user, name=name, detach=True)
            elif port != "" and environment != "" and command != "":
                self.docker_env.containers.run(image=image_name, command=command, user=user, name=name, detach=True,
                                               port=port, environment=environment)
            elif port == "" and environment != "" and command != "":
                self.docker_env.containers.run(image=image_name, command=command, user=user, name=name, detach=True,
                                               environment=environment)
            elif port != "" and environment == "" and command != "":
                self.docker_env.containers.run(image=image_name, command=command, user=user, name=name, detach=True,
                                               port=port)
            elif port != "" and environment != "" and command == "":
                self.docker_env.containers.run(image=image_name, user=user, name=name, detach=True, port=port,
                                               environment=environment)
            elif port == "" and environment == "" and command != "":
                self.docker_env.containers.run(image=image_name, command=command, user=user, name=name, detach=True)
            elif port == "" and environment != "" and command == "":
                self.docker_env.containers.run(image=image_name, command=command, user=user, name=name, detach=True,
                                               environment=environment)
            elif port != "" and environment == "" and command == "":
                self.docker_env.containers.run(image=image_name, user=user, name=name, detach=True, port=port)
            return True
        except Exception as e:
            return str(e)

    # TODO
    def docker_create_containers(self, image_name: str, user: str, name: str, port: dict, environment: dict or list,
                                 command="/bin/bash"):
        """
        创建并运行容器
        :param image_name: 镜像名字
        :param user: 所属用户
        :param name: 容器名称
        :param port: 映射端口{“3306/tcp”：3300}，容器3306映射到主机3300
        :param environment: 设置容器环境变量，数组或字典形式，["MYSQL_ROOT_PASSWORD='123456'"]或{“MYSQL_ROOT_PASSWORD”： “123456”}
        :param command: 创建时执行的命令，默认“/bin/bash”
        :return: 创建成功返回True，失败返回错误信息
        """
        self.refresh_docker_information()
        try:
            if port == "" and environment == "" and command == "":
                self.docker_env.containers.create(image=image_name, user=user, name=name, detach=True)
            elif port != "" and environment != "" and command != "":
                self.docker_env.containers.create(image=image_name, command=command, user=user, name=name, detach=True,
                                                  port=port, environment=environment)
            elif port == "" and environment != "" and command != "":
                self.docker_env.containers.create(image=image_name, command=command, user=user, name=name, detach=True,
                                                  environment=environment)
            elif port != "" and environment == "" and command != "":
                self.docker_env.containers.create(image=image_name, command=command, user=user, name=name, detach=True,
                                                  port=port)
            elif port != "" and environment != "" and command == "":
                self.docker_env.containers.create(image=image_name, user=user, name=name, detach=True, port=port,
                                                  environment=environment)
            elif port == "" and environment == "" and command != "":
                self.docker_env.containers.create(image=image_name, command=command, user=user, name=name, detach=True)
            elif port == "" and environment != "" and command == "":
                self.docker_env.containers.create(image=image_name, command=command, user=user, name=name, detach=True,
                                                  environment=environment)
            elif port != "" and environment == "" and command == "":
                self.docker_env.containers.create(image=image_name, user=user, name=name, detach=True, port=port)
            return True
        except Exception as e:
            return str(e)

    def docker_list_containers(self):
        """
        查询所有容器的信息
        :return: 查询成功返回数据，失败返回错误信息
        """
        self.refresh_docker_information()
        try:
            containers_infos = []
            containers_list = self.docker_env.containers.list(True)
            for containers_info in containers_list:
                containers_infos.append(
                    {
                        containers_info.name: self.docker_get_containers(containers_info.name)
                    }
                )
            return containers_infos
        except Exception as e:
            return str(e)

    def docker_get_containers(self, image_name: str):
        """
        查询某个容器
        :param image_name: 镜像名字
        :return: 查询成功返回数据，失败返回错误信息
        """
        self.refresh_docker_information()
        try:
            container = self.docker_env.containers.get(image_name)
            return {
                "name": container.name,
                "id": container.id,
                "image": container.image,
                "attrs": container.attrs,
                "labels": container.labels,
                "short_id": container.short_id,
                "status": container.status
            }
        except Exception as e:
            return str(e)

    def docker_stop_containers(self, image_name: str):
        """
        停止某个容器
        :param image_name: 镜像名字
        :return: 停止成功返回True，失败返回错误信息
        """
        self.refresh_docker_information()
        try:
            self.docker_env.containers.get(image_name).stop()
            return True
        except Exception as e:
            return str(e)

    def docker_restart_containers(self, image_name: str):
        """
        重启某个容器
        :param image_name: 镜像名字
        :return: 重启成功返回True，失败返回错误信息
        """
        self.refresh_docker_information()
        try:
            self.docker_env.containers.get(image_name).restart()
            return True
        except Exception as e:
            return str(e)

    def docker_remove_containers(self, image_name: str):
        """
        删除某个容器
        :param image_name: 镜像名字
        :return: 删除成功返回True，失败返回错误信息
        """
        self.refresh_docker_information()
        try:
            self.docker_env.containers.get(image_name).remove()
            return True
        except Exception as e:
            return str(e)

    def docker_rename_containers(self, image_name: str):
        """
        重命名某个容器
        :param image_name: 镜像名字
        :return: 重命名成功返回True，失败返回错误信息
        """
        self.refresh_docker_information()
        try:
            self.docker_env.containers.get(image_name).rename()
            return True
        except Exception as e:
            return str(e)

    def docker_start_containers(self, image_name: str):
        """
        启动某个容器
        :param image_name: 镜像名字
        :return: 启动成功返回True，失败返回错误信息
        """
        self.refresh_docker_information()
        try:
            self.docker_env.containers.get(image_name).start()
            return True
        except Exception as e:
            return str(e)

    def docker_wait_containers(self, image_name: str):
        """
        等待某个容器停止
        :param image_name: 镜像名字
        :return: 等待成功返回True，失败返回错误信息
        """
        self.refresh_docker_information()
        try:
            self.docker_env.containers.get(image_name).wait()
            return True
        except Exception as e:
            return str(e)

    def docker_exec_run_containers(self, image_name: str, command: str):
        """
        在某个容器内执行某个命令
        :param image_name: 镜像名字
        :param command: 执行的命令
        :return: 执行成功返回执行信息，失败返回错误信息
        """
        self.refresh_docker_information()
        try:
            exec_result = self.docker_env.containers.get(image_name).exec_run(command)
            return {
                "exit_code": exec_result.exit_code,
                "output": str(exec_result.output, 'utf-8')
            }
        except Exception as e:
            return str(e)

    def docker_commit_containers(self, image_name: str):
        """
        提交某个容器
        :param image_name: 镜像名字
        :return: 提交成功返回True，失败返回错误信息
        """
        self.refresh_docker_information()
        try:
            self.docker_env.containers.get(image_name).commit()
            return True
        except Exception as e:
            return str(e)


if __name__ == '__main__':
    run = DockerUIContainers()
    a = run.docker_list_containers()
    print(a)



