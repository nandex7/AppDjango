let div_error = document.querySelector("#error_message");
 function message_error(obj){
    var html = '';
     if(typeof(obj) === 'object'){
        html = '<ul>';
        $.each(obj, function(key, value){
            html+= '<li>' + key + ': ' + value + '</li>'
        });
        html+= '</ul>';
    }
    else{
        html = '<li>' + obj + '</li>';
    }
    

    if(Object.keys(obj).length !== 0){
        div_error.innerHTML = html;
        div_error.style.display = 'block'
    }
    
}

function submit_con_ajax(url_return, parameters, callback){
     $.confirm({
        theme: 'material',
        title: 'Confirmación!',
        icon: 'fa fa-info',
        content: '¿Estas seguro de realizar la siguiente acción?',
        columnClass: 'medium',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: 'Si',
                btnClass: 'btn-primary',
                action: function(){
                    $.ajax({
                        url: url_return,
                        type: 'POST',
                        data: parameters,
                        dataType: 'json'
                     }).done(function(data){
                         if(!data.hasOwnProperty('error')){
                             callback();
                            return false;
                        }
                         message_error(data.error);
                    }).fail(function(jqXHR, textStatus, errorThrown){
                          
                    }).always(function(data){
                        
                    });
                }
            },
            danger:{
                text: 'No',
                btnClass: 'btn-red',
                action: function(){

                }
            },
        }
    })
}

 