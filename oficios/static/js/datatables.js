$(document).ready( function () {
    var table = $('#TableT').DataTable({
        
        initComplete: function () {
            this.api().columns('.select-filter').every( function () {
                var column = this;
               
                var select = $('<select class="form-control id="rubro"><option value="">Todos</option></select>')
                    .appendTo( $('div.filtro>div.rubro') )
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
 
                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );
 
                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                } );
            } );
        },
        "language": {
            "lengthMenu": "Mostrar _MENU_ registros",
            "zeroRecords": "No se encontraron resultados",
            "info": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "infoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "infoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sSearch": "Buscar:",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast":"Último",
                "sNext":"Siguiente",
                "sPrevious": "Anterior"
             },
             "sProcessing":"Procesando...",
        },
        createdRow: function ( row, data, index ) {
            if (data.length>4){
                $(row).attr('data-url','/Trabajadores/MostrarPerfil/'+data[data.length-1])
            }
            
         } 
    });
    table.order([ 0, 'desc' ] ).draw(false);

    var zonaFiltro = function(){
        option=$(this)

        $.ajax({
          data:{'zona':option.val()},
          type:option.parent().parent().attr('method'),
          url:option.parent().parent().attr('action'),
          dataType:'json',
          success:function(dato){
            rows=dato['datos']
            pk=dato['pk']
            table.clear()
            table.rows.add(rows);
            table.draw();
          }
          
        });
    
    
      }
      $('#zonas').on('change',zonaFiltro);

} );