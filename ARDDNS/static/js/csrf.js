/**
 * Created by uxio on 16/10/14.
 */

$(function() {
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                var csrftoken = $.cookie('csrftoken');
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            }
        }
    });
});
