
//funcion captura de nombre de usuario y envio a mediante de petición ajax
function login(){
    objetoVariables = {
        username: $('#txt_user_name').val()
    }
    ajaxPeticionJS('POST', `${Config.URL}/login`, objetoVariables);
}


//Funcion ajax reutilizable
function ajaxPeticionJS(metodo, ruta, request = []){
    // alert(request);
    $.ajax({
        method: metodo,
        url : ruta,
        data : request,
    })
    .done(function(response){
        if(response){
            LocalStorage.setKeys(response);
            console.log(response);
            window.location.href = `${Config.URL}/chat_room`;
        }
    });
}
