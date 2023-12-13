function check_pass(){
    let new_pass = $("#new-password").val();
    let new_conf_pass = $("#new-conf-password").val();
    
    if(new_pass == new_conf_pass) {
        $("#new-password").css("border","1px solid green");
        $("#new-conf-password").css("border","1px solid green");
        //$("#new-password").removeClass("alert alert-danger").addClass("alert alert-success");
        //$("#new-conf-password").removeClass("alert alert-danger").addClass("alert alert-success");

        $("#submit_button").removeAttr("disabled");
    }
    else {
        $("#new-password").css("border","1px solid red");
        $("#new-conf-password").css("border","1px solid red");
        //$("#new-password").removeClass("alert alert-success").addClass("alert alert-danger");
        //$("#new-conf-password").removeClass("alert alert-success").addClass("alert alert-danger");

        $("#submit_button").attr("disabled","disabled");
    }
}



