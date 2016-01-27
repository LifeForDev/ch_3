function selectAll(event) {
    var checked = $(event.target).prop('checked');
    $('.check-selected').each(function() {
       $(this).prop('checked', checked);
    });
}

function deletePatch(event) {
    event.preventDefault();
    var ids = [];
    $('.check-selected:checked').each(function() {
       ids.push($(this).val());
    });

    if (ids.length === 0) {
        return false;
    } else {
        if (confirm('Are you sure to delete this Lead(s)?')) {
            $('#deleteForm_ids').val(ids);
            $('#deleteForm').submit();
        }
    }
}

function deleteLead(event, id) {
    event.preventDefault();
    if (confirm('Are you sure to delete this Lead(s)?')) {
        $('#deleteForm_ids').val(id);
        $('#deleteForm').submit();
    }
}
