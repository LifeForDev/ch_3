function selectAll(event) {
    var checked = $(event.target).prop('checked');
    $('.check-selected').each(function() {
       $(this).prop('checked', checked);
    });
}

$('#deleteForm').submit(function() {
    alert('hello');
});

// function delete-leads() {
//     var ids = [];
//     $('.check-selected:checked').each(function() {
//        ids.push($(this).data('id'));
//     });
//     alert(ids);
// }

// $('#deleteForm').submit(function() {
//   alert('Handler for .submit() called.');
//   return false;
// });
