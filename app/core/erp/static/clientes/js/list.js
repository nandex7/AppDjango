$(function(){
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            }, // parametros
            dataSrc: ""
        },
        columns: [
            { "data": "id"},
            { "data": "nombres"},
            { "data": "nro_documento"},
            { "data": "nro_telefono"},
            { "data": "direccion"},
            { "data": "direccion"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/clientes/update/'+ row.id + '/"><i class="fas fa-user-edit"></i>Editar</a> ';
                    buttons+= '<a href="/erp/clientes/delete/'+ row.id + '/"><i class="fas fa-trash-alt"></i>Eliminar</a>';
                    return buttons;
                }
            },
        ],
        initComplete: function(settings, json) {
           }
        });
});