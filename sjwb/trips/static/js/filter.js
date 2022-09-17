var check=function(){
    var select_s=$('#filter-s').val();
    console.log(select_s)
    const filter_url = $('#filter-s').attr('action')
    const pathname = window.location.pathname
    $.ajax({
        url: filter_url,
        data: {'select_s':select_s, 'pathname':pathname},
        type:"GET",
        success: function(message){
            console.log(message);
        },

        error:   function(jqXHR, textStatus, errorThrown){ 
            console.log(errorThrown); 
        }
    });
}  