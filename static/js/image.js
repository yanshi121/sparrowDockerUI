function image_search_button(){
    let value = document.getElementById("image_search_input").value
    if (value == null || value == '') {
        alert("镜像名不能为空")
        return false
    }else{
        return true
    }
}

function get_image_button(name){
    document.getElementById("get_image").innerHTML = "镜像拉取中..."
    document.getElementById("get_image").style.color = "red"
    send_post(
        {"image_name": name},
        WEB_URL + "/api/get_image", 
        function(json){  
            if (json['result']){
                alert("拉取成功")
                location.href = WEB_URL + "/image"
            }
            else{
                alert(json['result'])
            }
        }
        )
}

function image_remove_button(name){
    send_post(
        {"image_name": name},
        WEB_URL + "/api/image_remove", 
        function(json){  
            if (json['result']){
                alert("删除成功")
                location.href = WEB_URL + "/image"
            }
            else{
                alert(json['result'])
            }
        }
        )
}