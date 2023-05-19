// game.js
$(document).ready(function() {
    $('#start-button').click(function() {
        $.get('/get_word', function(data) {
            $('#word-display').text(data.word);
        });
    });

    $('#typed-word').keyup(function() {
        // ユーザーがタイプしたときの処理をここに書く
    });
});
