var score = 0;
var errors = 0;
var startTime = null;
var timer = null;
var ranking = [];

$(document).ready(function() {
    $('#start-button').click(startGame);
    $('#reset-button').click(resetGame);

    $('#typed-word').on('input', function() {
        var typed = $(this).val();
        var displayed = $('#word-display').text();

        if (typed === displayed) {
            $(this).val('');
            $(this).removeClass('incorrect');
            $(this).addClass('correct');
            score++;
            $('#score').text(score);
            startGame();
        } else if (displayed.indexOf(typed) !== 0) {
            $(this).addClass('incorrect');
            $(this).removeClass('correct');
            errors++;
            $('#errors').text(errors);
        } else {
            $(this).removeClass('incorrect');
            $(this).addClass('correct');
        }

        var elapsedTime = (Date.now() - startTime) / 1000;
        var speed = score / elapsedTime * 60;
        $('#speed').text(speed.toFixed(2));

        var accuracy = score / (score + errors) * 100;
        $('#accuracy').text(accuracy.toFixed(2));
    });
});

function startGame() {
    if (startTime === null) {
        startTime = Date.now();
        var time = 100;  // 初期値を設定
        $('#time').text(time);

        timer = setInterval(function() {
            time -= 1;  // 1秒減算
            $('#time').text(time);
            if (time <= 0) {
                endGame();
            }
        }, 1000);
    }

    $('#typed-word').keyup(function() {
        // ユーザーがタイプしたときの処理をここに書く
    });    

    getRandomWord(); // ここで新しい単語を取得
}

function getRandomWord() {
    $.get('/api/word', function(data) {
        $('#word-display').text(data.word);
        $('#typed-word').prop('disabled', false); // タイプ可能にする
        $('#typed-word').focus(); // 入力フィールドにフォーカスを移す
    });
}

function resetGame() {
    // ゲームの状態をリセット
    score = 0;
    errors = 0;
    startTime = null;
    $('#score').text(score);
    $('#errors').text(errors);
    $('#time').text('100');
    $('#speed').text('0');
    $('#accuracy').text('0');
    $('#word-display').text('');
    $('#typed-word').val('');
    $('#typed-word').removeClass('correct incorrect');
    $('#start-button').prop('disabled', false);
    $('#typed-word').prop('disabled', true); // 入力フィールドを無効化する
    if (timer !== null) {
        clearInterval(timer);
        timer = null;
    }
}

function endGame() {
    alert("Game Over");
    resetGame();
}
