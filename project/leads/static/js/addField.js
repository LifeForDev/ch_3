function addField(event) {
    var newField = $(event.target).parents('.form-group').clone(true, true);
    newField.find('.textinput').val('');
    newField.find('label').html('');
    newField
        .find('.btn')
        .html('Remove')
        .removeAttr('onclick')
        .on('click', function() {
            $(this).parents('.form-group').remove();
        })
    newField.appendTo('.languages_fs');
}
