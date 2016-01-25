// function addField(event) {

//     var newField = $(event.target).parents('.form-group').clone(true, true);
//     newField.removeClass('has-error');
//     newField.find('.help-block').remove();
//     newField.find('.textinput').val('');
//     newField.find('label').html('');
//     newField
//         .find('.btn')
//         .html('Remove')
//         .removeAttr('onclick')
//         .on('click', removeField);
//         $('#id_languages-TOTAL_FORMS').val(
//             parseInt($('#id_languages-TOTAL_FORMS').val()) + 1)
//     newField.appendTo('.languages_fs');
// }

// function removeField(event) {
//     parent = $(this).parents('.form-group');
//     id = parent.find('input').attr('id').split('-')[1];
//     alert(id);
//     $('.languages_fs').find('#id_languages-' + id + '-DELETE').val('1');
//     parent.remove();
// }

function addForm(type) {
    var form_idx = $('#id_'+type+'-TOTAL_FORMS').val();
    $('#'+type).append($('#formset-template').html().replace(/__prefix__/g, form_idx));

    $('#id_'+type+'-TOTAL_FORMS').val(parseInt(form_idx) + 1);
}

function removeForm(type, elem) {
    var elem_id = elem.data('id');

    // Mark form for deletion
    elem.find('#id_'+type+'-'+elem_id+'-DELETE').val("1");
    elem.hide();
}

$(document).ready(function() {
    first_button = $('.languages > .form-group').first();
    remove_button = $('.languages > .form-group').slice(1)
    remove_button.find('label').html('');
    remove_button
        .find('.btn')
        .html('Remove')
        .on('click', function(event) {
            event.preventDefault();
            var element = $(event.target).closest('.form-group');
            removeForm('languages', element);
        });
    first_button
        .find('.btn')
        .on('click', function(event) {
            event.preventDefault();
            addForm('languages');
        });
});
