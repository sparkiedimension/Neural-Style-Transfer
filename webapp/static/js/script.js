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
});
