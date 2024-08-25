document.getElementById('questionsBtn').addEventListener('click', function () {
    const nQuestions = document.getElementById('nQuestions').value;
    const questions = document.getElementById('questions');

    for (let i = 1; i <= nQuestions; i++) {
        questions.innerHTML += '<br>' +
            '<label for="question_' + i + '">Question ' + i + '</label>' +
            '<br>' +
            '<input type="text" name="question_' + i + '" placeholder="the question" id="question_' + i + '" required />' +
            '<br>' +
            '<label for="mark">The mark for the question</label>' +
            '<br>' +
            '<input type="number" name="mark" placeholder="mark for the question" id="mark" required />' +
            '<br>' +
            '<label for="nChoices">Number of choices</label>' +
            '<br>' +
            '<input type="number" name="nChoices" placeholder="number of choices" id="nChoices" required />' +
            '<br>' +
            '<button class="btn" id="choicesBtn">Enter choices</button>' +
            '<br><br>' +
            '<div id="choices"></div>';

        document.getElementById('choicesBtn').addEventListener('click', function () {
            let nChoices = document.getElementById('nChoices').value;
            let choices = document.getElementById('choices');

            for (let j = 1; j <= nQuestions; j++) {
                choices.innerHTML += '<br>' +
                    '<label for="choice_' + j + '">Choice ' + j + '</label>' +
                    '<br>' +
                    '<input type="text" name="choice_' + j + '" placeholder="the choice" id="choice_' + j + '" required>'
            }

        })
    }

})



