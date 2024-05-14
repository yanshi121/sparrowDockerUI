import time
from flask import Flask, render_template, request, redirect, url_for
from PythonCode.DockerUIInfo import DockerUIInfo
from PythonCode.DockerUIImage import DockerUIImage
from PythonCode.DockerUIContainers import DockerUIContainers


app = Flask(__name__)


@app.route("/")
def index():
    docker_ui_info = DockerUIInfo()
    docker_info = docker_ui_info.docker_info()
    system_ip = docker_ui_info.get_ip()
    system_info_cpu = docker_ui_info.system_info_cpu()
    system_info_virtual = docker_ui_info.system_info_virtual()
    system_info_disk = docker_ui_info.system_info_disk()
    system_info_cpu_percent = docker_ui_info.system_info_cpu_percent()
    return render_template(
        "index.html",
        title="主页",
        docker_info=docker_info,
        system_ip=system_ip,
        system_info_cpu=system_info_cpu,
        system_info_virtual=system_info_virtual,
        system_info_disk=system_info_disk,
        system_info_cpu_percent=system_info_cpu_percent
        )


@app.route("/image")
def image():
    docker_image = DockerUIImage()
    docker_list_image = docker_image.docker_list_image()
    return render_template(
        "image.html",
        title="镜像",
        docker_list_image=docker_list_image
        )


@app.route("/containers")
def containers():
    docker_container = DockerUIContainers()
    docker_list_container = docker_container.docker_list_containers()
    return render_template(
        "containers.html",
        title="容器",
        docker_list_container=docker_list_container
        )

@app.route("/container_create", methods=["POST", "GET"])
def container_create():
    if request.method == "POST":
        docker_container = DockerUIContainers()
        image_name = request.form.get("container_create_image")
        user_name = request.form.get("container_create_user")
        container_name = request.form.get("container_create_name")
        in_port = request.form.get("container_create_in_port")
        out_port = request.form.get("container_create_out_port")
        environment = request.form.get("container_create_environment")
        command = request.form.get("container_create_command")
        if command == None or command == '':
            if in_port == None or in_port == '':
                docker_container.docker_run_containers(image_name, user_name, container_name, '', environment)
            else:
                docker_container.docker_run_containers(image_name, user_name, container_name, {f"{in_port}/tcp": int(out_port)}, environment)
        else:
            if in_port == None or in_port == '':
                docker_container.docker_run_containers(image_name, user_name, container_name, '', environment, command)
            else:
                docker_container.docker_run_containers(image_name, user_name, container_name, {f"{in_port}/tcp": int(out_port)}, environment, command)
        return redirect(url_for("containers"))
    else:
        docker_ui_info = DockerUIInfo()
        docker_image = DockerUIImage()
        docker_list_image = docker_image.docker_list_image()
        system_users = docker_ui_info.system_users()
        return render_template(
            "container/create.html",
            title="新建容器",
            docker_list_image=docker_list_image,
            system_users=system_users
            )


@app.route("/search_image", methods=["POST"])
def search_image():
    docker_image = DockerUIImage()
    image_name = request.form.get("image_name")
    docker_search_image = docker_image.docker_search_image(image_name)
    return render_template(
        "image/search.html",
        title="镜像搜索",
        docker_search_image=docker_search_image
    )


@app.route("/api/get_image", methods=["POST"])
def get_image():
    print(request.get_json())
    docker_image = DockerUIImage()
    image_name = request.get_json()['data']['image_name']
    result = docker_image.docker_pull_image(image_name)
    return {"result": result}


@app.route("/api/image_remove", methods=["POST"])
def image_remove():
    print(request.get_json())
    docker_image = DockerUIImage()
    image_name = request.get_json()['data']['image_name']
    result = docker_image.docker_remove_image(image_name)
    return {"result": result}


@app.route("/api/container_delete", methods=["POST"])
def container_delete():
    container_name = request.get_json()['data']['container_name']
    docker_container = DockerUIContainers()
    result = docker_container.docker_remove_containers(container_name)
    return {"result": result}


@app.route("/api/container_restart", methods=["POST"])
def container_restart():
    container_name = request.get_json()['data']['container_name']
    docker_container = DockerUIContainers()
    result = docker_container.docker_restart_containers(container_name)
    return {"result": result}


@app.route("/api/container_rename", methods=["POST"])
def container_rename():
    container_name = request.get_json()['data']['container_name']
    container_new_name = request.get_json()['data']['new_name']
    docker_container = DockerUIContainers()
    result = docker_container.docker_rename_containers(container_name, container_new_name)
    return {"result": result}


@app.route("/api/container_start_stop", methods=["POST"])
def container_start_stop():
    container_name = request.get_json()['data']['container_name']
    status = request.get_json()['data']['status']
    docker_container = DockerUIContainers()
    if status == 'running':
        result = docker_container.docker_stop_containers(container_name)
        return {"result": result, "code": "停止成功"}
    else:
        result = docker_container.docker_start_containers(container_name)
        return {"result": result, "code": "启动成功"}


@app.route("/api/getvirtual_memory", methods=["POST"])
def getvirtual_memory():
    docker_ui_info = DockerUIInfo()
    system_info_virtual = docker_ui_info.system_info_virtual()
    return system_info_virtual


@app.route("/api/disk_usage", methods=["POST"])
def disk_usage():
    docker_ui_info = DockerUIInfo()
    system_info_disk = docker_ui_info.system_info_disk()
    return system_info_disk


@app.route("/api/system_info_cpu_percent", methods=["POST"])
def system_info_cpu_percent():
    docker_ui_info = DockerUIInfo()
    system_info_cpu_percent = docker_ui_info.system_info_cpu_percent()
    return system_info_cpu_percent


app.run(host="0.0.0.0", port=5000, debug=True)
