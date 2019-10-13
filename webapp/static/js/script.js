function load_infants() {
    if( $('#dashboard').find('.infant-entry').length > 0 ) {
        let i = 0;
        
        let interval_id = setInterval( function() {
            let all_infants = $('#dashboard .infant-entry');
            let t = 59 - i;
            let time_str = '00:' + (t > 9 ? t : ('0' + t));
            
            for( let i = 0; i < all_infants.length; i++ ) {
                $(all_infants[i]).find('.time-left').text(time_str);
            }
            
            i++;
        }, 1000);
        
        setTimeout( function() {
            clearInterval(interval_id);
            
            let all_infants = $('#dashboard .infant-entry');
            
            for( let i = 0; i < all_infants.length; i++ ) {
                let token = $(all_infants[i]).attr('id');
                let url = '/app/dashboard/?token=' + token;
                
                $.getJSON(url, function( result ) {
                    if ( !jQuery.isEmptyObject(result) ) {
                        let ready_entry = $('#' + result['token']).siblings('.ready-entry');
                        $(ready_entry).find('.title').text( result['title'] );
                        $(ready_entry).find('.final').attr( 'src', result['final'] );
                        $(ready_entry).find('.content').attr( 'src', result['content'] );
                        $(ready_entry).find('.style').attr( 'src', result['style'] );
                        
                        $('#' + result['token']).addClass('d-none');
                        $(ready_entry).removeClass('d-none');
                        $(ready_entry).parent().removeClass('no-shadow');
                    }
                });
            }
            
            load_infants();
        }, 60000);
    }
}

$(document).ready( function() {

    $('#signup-form .submit-btn').click( function() {
        $('#signup-form .alert').addClass('d-none');
        
        let message = ""; 
        let text = "";

        text = $('#signup-form .username').val();
        if ( text.length < 1 ) {
            message = "Fields can't be left empty."
        }
        else if( !(text.length > 0 && text.match(/^[0-9a-zA-Z]+$/) )) {
            message = "Type in a valid username, using only lettters and numbers."
        }
        else {
            text = $('#signup-form .password').val();
            let text_1 = $('#signup-form .re-password').val();
            
            if( text.length < 1 ) {
                message = "Fields can't be left empty."
            }
            else if( !(text.length == text_1.length && text == text_1) ) {
                message = "Passwords didn't match. Please try again."
            }
        }
        
        if( message.length > 0 ) {
            $('#signup-form .alert .alert-text').text(message);
            $('#signup-form .alert').removeClass('d-none');
        }
        else {
            $('#signup-form').submit();
        }
    });
    
    
    
    $('.custom-file-input').change( function() {
        let name = $(this).val();
        name = name.replace(/.*[\/\\]/, '');
    
        $(this).siblings('.custom-file-label').text( name );
    });
    
    
    
    $('#upload-img-modal .submit-btn').click( function() {
        $('#upload-img-modal .alert').addClass('d-none');
        
        let message = "";
        let text = $('#design-title').val();
        
        if( text.length < 1 ) {
            message = "Design Title can't be empty!";
        }
        else {
            text = $('#content-upload').val();
            
            if( !( text.length > 0 || $('#upload-content-img input[type=radio]:checked').length > 0 )) {
                message = "Please upload the Content image.";
            }
            else {
                text = $('#style-upload').val();
            
                if( !( text.length > 0 || $('#upload-style-img input[type=radio]:checked').length > 0 )) {
                    message = "Please upload the Style image.";
                }
            }
        }
        
        if( message.length > 0 ) {
            $('#upload-img-modal .alert .alert-text').text(message);
            $('#upload-img-modal .alert').removeClass('d-none');
        }
        else {
            $('#upload-img-modal form.modal-body').submit();
        }
    });
    
    
    
    $('#dashboard .ready-entry').click( function() {
        let entry_title = $(this).find('.title').html();
        let final_src = $(this).find('.final').attr('src');
        let content_src = $(this).find('.content').attr('src');
        let style_src = $(this).find('.style').attr('src');
        
        final_src = final_src.replace(/preview\//, '');
        content_src = content_src.replace(/preview\//, '');
        style_src = style_src.replace(/preview\//, '');
        
        $('#showcase-modal .modal-title').html(entry_title);
        $('#showcase-modal .modal-body .result-img').attr('src', final_src);
        $('#showcase-modal .modal-body .content-img').attr('src', content_src);
        $('#showcase-modal .modal-body .style-img').attr('src', style_src);
        
        $('#showcase-modal').modal({'show': true});
    });
    
    
    load_infants();
});
