

/*
    Account
*/
$(document).on('click', function(evt){
    let button_name = (evt.target.name);
    if (button_name == 'person'){
        $('#menu_company_direction').show();
        $('#menu_person').slideUp();
    } else if (button_name == 'company_direction'){
        $('#menu_company').show();
        $('#menu_company_direction').slideUp();
    } else if (button_name == 'company_direction-back'){
        $('#menu_person').slideDown();
        $('#menu_company_direction').slideDown();
        $('#menu_company_direction').hide(500);
    } else if (button_name == 'company_back'){
        $('#menu_company_direction').slideDown();
        $('#menu_company').slideDown();
        $('#menu_company').hide(500);
    }
});

// change document icon color
$(document).on('change', function(evt){
    let reader = new FileReader();
    reader.onload = function(e){
        let image_name = evt.target.name;
        console.log('#'+'doc_'+ image_name);
        $('#doc_'+ image_name).css({'color': 'rgb( 46, 204, 113)'});
    }
    reader.readAsDataURL(evt.target.files[0])
});


$(document).on('keyup','#id_cp', function(evt){
    if( $(this).val().length == 5 ){
        request = $.ajax({
                url: '/api/get-direction/',
                type: 'GET',
                data: {
                    'cp': $(this).val()
                }
         });
        request.done(function(data){
            $('#id_state').val(data.state);
            $('#id_city').val(data.city);
        });
        request.fail(function(data){
            console.log('error de envio')
        });
    }
});
