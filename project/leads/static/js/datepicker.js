$(document).ready(function() {
    $('#datepicker').datepicker({
        changeYear: true,
        dateFormat: "yy-mm-dd",
        showmonth: true,
    }).attr('readonly', 'true');
});
