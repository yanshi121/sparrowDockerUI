function get_virtual_memory(){
    send_post("", WEB_URL + "/api/getvirtual_memory", function(json){
        document.getElementById("virtual_memory_total").innerHTML = json.virtual_memory_total + "M"
        document.getElementById("virtual_memory_available").innerHTML = json.virtual_memory_available + "M"
        document.getElementById("virtual_memory_used").innerHTML = json.virtual_memory_used + "M"
        document.getElementById("virtual_memory_percent").innerHTML = json.virtual_memory_percent + "%"
    })
}

function get_disk_usage(){
    send_post("", WEB_URL + "/api/disk_usage", function(json){
        document.getElementById("disk_usage_total").innerHTML = json.disk_usage_total + "G"
        document.getElementById("disk_usage_used").innerHTML = json.disk_usage_used + "G"
        document.getElementById("disk_usage_free").innerHTML = json.disk_usage_free + "G"
        document.getElementById("disk_usage_percent").innerHTML = json.disk_usage_percent + "%"
    })
}

function get_system_info_cpu_percent(){
    send_post("", WEB_URL + "/api/system_info_cpu_percent", function(json){
        for (let index = 0; index < json['cpu_percent'].length; index++) {
            document.getElementById("cpu_percent_" + (index + 1)).innerHTML = json['cpu_percent'][index] + "%"
        }
    })
}

window.setInterval(function(){
    get_virtual_memory()
}, 1000)

window.setInterval(function(){
    get_system_info_cpu_percent()
}, 1000)

window.setInterval(function(){
    get_disk_usage()
}, 10000)