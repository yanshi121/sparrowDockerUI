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

function start_stop_button(name, status){

}

function container_restart_button(name){

}

