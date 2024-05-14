function start_stop(){
    let start_stop = document.getElementsByClassName("container_start_stop")
    let status = document.getElementsByClassName("container_status")
    for (let index = 0; index < start_stop.length; index++) {
        let start_stop_button = start_stop[index]
        let status_text = status[index].innerHTML
        if (status_text === "running") {
            start_stop_button.innerHTML = "停止"
        }else{
            start_stop_button.innerHTML = "启动"
        }
    }
}

function container_start_stop_button(status, name){
    send_post(
        {"container_name": name, "status":status}, 
        WEB_URL + "/api/container_start_stop", 
        function(json){
            if (json['result']){
                alert(json['code'])
                location.href = WEB_URL + "/containers"
            }
            else{
                alert(json['result'])
            }
        }
        )
}

function container_rename_button(name){
    let value = document.getElementById("container_rename_input_" + name).value
    let all_name = document.getElementsByClassName("container_name")
    let all_name_list = []
    for (let index = 0; index < all_name.length; index++) {
        let name = all_name[index].innerHTML;
        all_name_list.push(name)
        
    }
    if(value === null || value === ""){
        alert("重命名不能为空")
    }
    else if(all_name_list.includes(value)){
        alert("不能与其他容器名相同")
    }
    else{
        send_post(
            {"container_name": name, "new_name": value}, 
            WEB_URL + "/api/container_rename", 
            function(json){  
                if (json['result']){
                    alert("重命名成功")
                    location.href = WEB_URL + "/containers"
                }
                else{
                    alert(json['result'])
                }
            }
            )
    }
}

function container_restart_button(name){
    send_post(
        {"container_name": name}, 
        WEB_URL + "/api/container_restart", 
        function(json){  
            if (json['result']){
                alert("重启成功")
                location.href = WEB_URL + "/containers"
            }
            else{
                alert(json['result'])
            }
        }
        )
}

function container_remove_button(name){
    send_post(
        {"container_name": name}, 
        WEB_URL + "/api/container_delete", 
        function(json){  
            if (json['result']){
                alert("删除成功")
                location.href = WEB_URL + "/containers"
            }
            else{
                alert(json['result'])
            }
        }
        )
}

function container_create_not_null(form){
    if(form.container_create_name.value === null || form.container_create_name.value === ""){
        alert("容器名称不能为空")
        return false
    }
    if(form.container_create_in_port.value === null || form.container_create_in_port.value === ""){
        if(form.container_create_out_port.value === null || form.container_create_out_port.value === ""){
            return true
        }
        alert("已填写宿主机端口时,必须填写容器内端口")
        return false
    }
    if(form.container_create_out_port.value === null || form.container_create_out_port.value === ""){
        if(form.container_create_in_port.value === null || form.container_create_in_port.value === ""){
            return true
        }
        alert("已填写容器内端口时,必须填写宿主机端口")
        return false
    }
    return true;
}