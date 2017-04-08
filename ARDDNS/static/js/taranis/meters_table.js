function getCheckedIds() {
    var id_list = $('input[type=checkbox]:checked').map(function(){ return $(this).attr('data-id-meter')}).get();
    return id_list;
}
function getReportType() {
    return $('[data-report-type]:selected').attr('data-report-type');
}
function buildUrl(report_type, id_list) {
    var url = '/reports/make/' + report_type + '/' + id_list.join(',');
    return url
}
function set_checkAll(status) {
    $('input[type=checkbox]').prop('checked', status);
}
$(function(){
    $(document).on('click', '[data-js-check-all]', function() {
        set_checkAll(true);
    });
    $(document).on('click', '[data-js-uncheck-all]', function() {
        set_checkAll(false);
    });
    $(document).on('click', '[data-js-get-report]', function() {
        var id_list = getCheckedIds();
        if (id_list.length) {
            var url = buildUrl(getReportType(), getCheckedIds());
            window.location.href = url;
        }
    });
    // Selecting checkbox clicking on TR---
    $(document).on('click', 'input[type=checkbox]', function(event) {
        event.stopPropagation();
    });

    $(document).on('click', '[data-js-check]', function() {
        if ($(this).type == 'checkbox') {
            return;
        }
        var checkbox = $(this).find('input[type=checkbox]');
        checkbox.prop("checked", !checkbox.prop("checked"));
    });
    //-------------------------------------
});
