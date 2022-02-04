
$(document).on('click', '.add-form-row-output', function (e) {
        e.preventDefault();

        var Total_Forms_output = parseInt($("#id_step3-TOTAL_FORMS").val());
        var clone_row = $(".experience-list").clone().find("div.form-row-output").hide().appendTo(".form-row-output-plus").slideDown(300);

        if(Total_Forms){

          $(".experience-list-plus").find(".form-row-output:last-child").each(
            function () {

              $(".experience-list-plus").find(".form-field-input").each(
                 function () {
                   var regular_exp = new RegExp('(' + 'step3' + '-\\d+-)');
                   var replacement = "step3-" + Total_Forms + "-";
                   if ($(this).attr("for")) $(this).attr("for", $(this).attr("for").replace(regular_exp, replacement));
                   if (this.id) this.id = this.id.replace(regular_exp, replacement);
                   if (this.name) this.name = this.name.replace(regular_exp, replacement);
                   $(this).val("")
                   $(this).removeAttr('value');
                    console.log("this.id  = " + this.id);

                    return true
                 }
               );
               return true

             }
           );

          // incremente nbre form
          $(".method_form_2").find("#id_step3-TOTAL_FORMS").val(Total_Forms_output + 1);
          console.log("this.id  = " + Total_Forms_output);

        }
    })


$(document).on("click",".delete-form-row-output",function (event) {
    event.preventDefault();
})
