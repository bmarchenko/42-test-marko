    $(document).ready(function(){
      var options = {
        dataType: 'json',
        beforeSubmit: beforeForm,
        success: processJson
      };
      $('#My_form').submit(function () {
        $(this).ajaxSubmit(options);
        return false;
      })
    });

    function beforeForm() {
      // disable form inputs
      $("#My_form input").attr('disabled', 'disabled');
      $("#My_form textarea").attr('disabled', 'disabled');

      $(".errorlist").remove(); // get rid of any old errors
      $("#emsg").fadeOut("slow"); // get rid of the main error message
      return true;
    }

    function processJson(data) {
      var e_msg = "Ajax error: no data received. ";
      if (data) {
        e_msg = "Data updated, thank you.";
        data = eval(data)
        if (data.bad) {
          e_msg = "Please check your form";
          errors = data.errs;
          $.each(errors, function(fieldname, errmsg) {
            id = "#id_" + fieldname;
            $(id).parent().before(errmsg);
          });
        }
      }
      $("#emsg").text(e_msg).fadeIn("slow")
      $("#My_form input").attr('disabled', false);
      $("#My_form textarea").attr('disabled', false);
    }

