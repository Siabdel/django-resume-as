//resume processing forms wizardview

function dupliquer(e, id_step) {
        e.preventDefault();
        var id_total = "#id_" + id_step + "-TOTAL_FORMS";

        console.log("this.id  = " + id_total);

        //var Total_Forms = parseInt($(".method_form_1").find("#id_{{STEP_NUMBER}}-TOTAL_FORMS").val());
        var self = $(e.target);
        var clone_row = $(".formation-list").clone().find("div.form-row-local").hide().appendTo(".formation-list-plus").slideDown(300);
        // numeroté les id et name des balises input
        var Total_Forms_output = parseInt($(id_total).val());

        if(Total_Forms_output){

            $(".formation-list-plus").find(".form-row-local:last-child").each(
              function () {

                $(".formation-list-plus").find(".form-field-input").each(
                   function () {
                     var regular_exp = new RegExp('(' + id_step + '-\\d+-)');
                     var replacement = id_step + "-" + Total_Forms_output + "-";
                     console.log("this.id  = " + replacement);

                     if ($(this).attr("for")) $(this).attr("for", $(this).attr("for").replace(regular_exp, replacement));
                     if (this.id) this.id = this.id.replace(regular_exp, replacement);
                     if (this.name) this.name = this.name.replace(regular_exp, replacement);
                     $(this).val("")
                     $(this).removeAttr('value');
                     return true
                   }
                 );
                 return true

               }
             );
            //$(clone_row).insertAfter(".form").slideDown(30);

        // incrementer le TOTAL_FORMS
        $(".method_form_1").find("#id_" + id_step + "-TOTAL_FORMS").val(Total_Forms_output + 1);

      }
    };

//suppression
function supprimer_ligne(event, id_step) {
    event.preventDefault();

    Total_Forms = $(".form-row-local").length;

    if (Total_Forms > 1) {

        $(event.target).parent().parent().remove();
        console.log("supprimer_ligne = " +  id_step);

        $(".method_form_1").find("#id_" + id_step +  "-TOTAL_FORMS").val($(".form-row-local").length);
        form_name = $(".form-row-local");

        for (i = 0; i < Total_Forms; i++) {
            $(form_name.get(i)).find(".form-field-input").each(
                function () {
                    var regular_exp = new RegExp('(' + id_step + '-\\d+-)');
                    var replacement = id_step +  "-" + i + "-";
                    if ($(this).attr("for")) $(this).attr("for", $(this).attr("for").replace(regular_exp, replacement));
                    if (this.id) this.id = this.id.replace(regular_exp, replacement);
                    if (this.name) this.name = this.name.replace(regular_exp, replacement);

                    return false;
                }
            )
        }
    }

}
