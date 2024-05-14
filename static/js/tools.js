function send_post(data_value, url, fn) {
    let json
    let httpRequest = new XMLHttpRequest
    httpRequest.open('POST', url, true)
    httpRequest.setRequestHeader('Content-Type', 'application/json')
    let dataJson = { "data": data_value }
    httpRequest.send(JSON.stringify(dataJson))
    httpRequest.onreadystatechange = function () {
        if (httpRequest.readyState === 4 && httpRequest.status === 200) {
            json = httpRequest.responseText
            fn(JSON.parse(json))
        }
    }
}

function get_time() {
    let newDate = new Date();
    let date = newDate.toLocaleString()
    return date
}

function save_data_localStorage(data) {
    let str_jsonDate = JSON.stringify(data)
    localStorage.setItem('localStorage', str_jsonDate)
}

function get_data_localStorage() {
    let data = localStorage.getItem('localStorage')
    let dataJson = JSON.parse(data)
    return dataJson
}

function remove_data_localStorage() {
    localStorage.removeItem('localStorage')
}

function remove_cookie(cookieName) {
    let cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
        if (cookies[i].indexOf(" ") == 0) {
            cookies[i] = cookies[i].substring(1);
        }
        if (cookies[i].indexOf(cookieName) == 0) {
            let exp = new Date();
            exp.setTime(exp.getTime() - 60 * 1000);
            document.cookie = cookies[i] + ";expires=" + exp.toUTCString();
            break;
        }
    }
}

function set_cookies(cookieName, cookieValue) {
    document.cookie = cookieName + "=" + cookieValue
}

function get_cookies(cookieName) {
    let cookies = document.cookie.split("; ");
    for (let i = 0; i < cookies.length; i++) {
        let name = cookies[i].split("=")[0];
        let value = cookies[i].split("=")[1];
        if (name == cookieName) return value
    }
}

function change_cookies(cookieName, cookieValue) {
    let cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
        if (cookies[i].indexOf(" ") == 0) {
            cookies[i] = cookies[i].substring(1);
        }
        if (cookies[i].indexOf(cookieName) == 0) {
            let exp = new Date();
            exp.setTime(exp.getTime() - 60 * 1000);
            document.cookie = cookies[i] + ";expires=" + exp.toUTCString();
            break;
        }
    }
    document.cookie = cookieName + "=" + cookieValue
}



