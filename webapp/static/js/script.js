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
});
