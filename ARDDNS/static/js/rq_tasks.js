/**
 * Created by uxio on 18/11/14.
 */

function check_task_until_ready(key, timeout, callback) {
    //var url = '{% url 'get-task-status' key='no_key' %}'.replace('no_key', key);
    var url = '/rq-task/status/' + key;
    $.getJSON(url, null, function(result) {
        if (result && result.finished) {
            if (callback) {
                callback(result);
            }
        } else {
            setTimeout(function() {
                check_task_until_ready(key, timeout, callback);
            }, timeout);
        }
    });
}
