/**
 *
 * Created by uxio on 5/11/14.
 */

$(function(){
    //Clicking on concentrator check button
    $(document).on('click', '[data-check-url]', function(event) {
        var url = $(event.target).attr('data-check-url');
        $.get(url, null, function(result) {
            //TODO autoupdate, result is true if is alive
            window.location.reload(true);
        });
    });
    //Clicking on UPDATE button
    $(document).on('click', '[data-update-url]', function(event) {
        var jCurrent = $(event.target);
        var url = jCurrent.attr('data-update-url');
        $.get(url, null, function(result) {
            if (result.status == 'enqueued') {
                check_task_until_ready(result.key, 1000, function(result){
                    if (result.result) {
                        alert('Update successful');
                    } else {
                        alert('Error Updating');
                    }
                });
                init_update_bar(jCurrent);
            }
        });
    });
    //When the website is renderized and some concentrators are already updating
    $('[data-fw-is-updating]').each(function(index) {
        var jCurrent = $(this);
        init_update_bar(jCurrent)
    });
    //Show update bar of a concentrator
    function init_update_bar(jCurrent) {
        var tr =  jCurrent.closest('tr');
        var jProgressBar = $('[data-fw-progress-bar]', tr);
        jProgressBar.parent().css('display', '');
        jProgressBar.addClass('active');
        var info_url = tr.attr('data-js-fw-url');
        update_bar(info_url, jProgressBar);
    }
    //Updates the bar asking for info on the JSON API
    function update_bar(info_url, jProgressBar) {
        $.getJSON(info_url, null, function(result) {
            if (result['fw_is_updating']) {
                jProgressBar.css('width', Math.floor(result['fw_updating_process']) + '%');
                jProgressBar.html('<span>' + Math.floor(result['fw_updating_process']) + '%</span>');
                setTimeout(function() {
                    update_bar(info_url, jProgressBar);
                }, 500);
            } else {
                jProgressBar.css('width', 100 + '%');
                jProgressBar.text(100);
                jProgressBar.removeClass('active');
            }
        });
    }
});
