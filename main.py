from flask import Flask, render_template
from PythonCode.DockerUIInfo import DockerUIInfo
from PythonCode.DockerUIImage import DockerUIImage
from PythonCode.DockerUIContainers import DockerUIContainers


app = Flask(__name__)


@app.route("/")
def index():
    try:
        docker_ui_info = DockerUIInfo()
        # docker_info = docker_ui_info.docker_info()
        system_ip = docker_ui_info.get_ip()
        system_info_cpu = docker_ui_info.system_info_cpu()
        system_info_virtual = docker_ui_info.system_info_virtual()
        system_info_disk = docker_ui_info.system_info_disk()
        return render_template(
            "index.html",
            title="主页",
            # docker_info=docker_info,
            system_ip=system_ip,
            system_info_cpu=system_info_cpu,
            system_info_virtual=system_info_virtual,
            system_info_disk=system_info_disk
            )
    except Exception as e:
        return render_template("error.html", error="主机详情获取错误")


@app.route("/image")
def image():
    try:
        docker_image = DockerUIImage()
        docker_list_image = docker_image.docker_list_image()
        return render_template(
            "image.html",
            title="镜像",
            docker_list_image=docker_list_image
            )
    except Exception as e:
        return render_template("error.html", error="镜像获取错误")


@app.route("/containers")
def containers():
    try:
        docker_container = DockerUIContainers()
        docker_list_container = docker_container.docker_list_containers()
        return render_template(
            "containers.html",
            title="容器",
            docker_list_container=docker_list_container
            )
    except Exception as e:
        return render_template("error.html", error="容器获取错误")


app.run(host="0.0.0.0", port=5000, debug=True)
