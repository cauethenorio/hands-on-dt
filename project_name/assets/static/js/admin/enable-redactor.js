(function () {
    "use strict";

    var text_css = __admin_media_prefix__.replace('grappelli/', '') + 'css/admin/redactor-text.css';

    jQuery(document).ready(function() {
        jQuery("textarea[id^='id_answer']").redactor({
            focus:true,
            iframe:true,
            css:text_css,
            lang:jQuery('html').attr('lang').replace('-', '_'),
            buttons:['html', '|', 'formatting', '|', 'bold',
                'italic', 'deleted', '|', 'unorderedlist',
                'orderedlist', 'outdent', 'indent', '|',
                'image', 'video', 'table', 'link', '|', 'alignment']
        });

    });
}());
