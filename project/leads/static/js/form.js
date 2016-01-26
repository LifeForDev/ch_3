function addForm(type) {
    var form_idx = $('#id_'+type+'-TOTAL_FORMS').val();
    var elem = $('#formset-template > .form-group').clone(true, true);
    elem.html(elem.html().replace(/__prefix__/g, form_idx));
    elem.attr('data-id', form_idx);
    elem
        .find('label').html('');
    elem
        .find('.btn')
        .html('Remove')
        .removeAttr('onclick')
        .on('click', function(event) {
            event.preventDefault();
            var element = $(event.target).parents('.form-group').parents('.form-group');
            removeForm('languages', element);
        });
    $('#'+type).append(elem);

    $('#id_'+type+'-TOTAL_FORMS').val(parseInt(form_idx) + 1);
}

function removeForm(type, elem) {
    var elem_id = elem.data('id');
    $('#id_'+type+'-'+elem_id+'-DELETE').val("1");
    elem.hide();
}

$(document).ready(function() {
    var elems = $('#languages .form-group');
    $.each(elems, function(index) {
        $(this).attr('data-id', index);
        if ($('#id_languages-'+ index +'-DELETE').val() == 1) {
            $(this).hide();
        }
    })

    first_button = $('#languages > .form-group').first();
    remove_button = $('#languages > .form-group').slice(1)
    remove_button.find('label').html('');
    remove_button
        .find('.btn')
        .html('Remove')
        .on('click', function(event) {
            event.preventDefault();
            var element = $(event.target).parents('.form-group');
            removeForm('languages', element);
        });
    first_button
        .find('.btn')
        .on('click', function(event) {
            event.preventDefault();
            addForm('languages');
        });
});
