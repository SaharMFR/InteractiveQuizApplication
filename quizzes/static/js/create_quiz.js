document.getElementById('questionsBtn').addEventListener('click', function (event) {
    event.preventDefault();  // Prevent form submission

    const nQuestions = document.getElementById('nQuestions').value;
    const questions = document.getElementById('questions');

    // Clear previous questions to avoid multiple appends
    questions.innerHTML = '';

    for (let i = 1; i <= nQuestions; i++) {
        questions.innerHTML += '<br>' +
            '<label for="question_' + i + '">Question ' + i + '</label>' +
            '<br>' +
            '<input type="text" name="question_' + i + '" placeholder="the question" id="question_' + i + '" required />' +
            '<br>' +
            '<label for="mark_' + i + '">The mark for the question</label>' +
            '<br>' +
            '<input type="number" name="mark_' + i + '" placeholder="mark for the question" id="mark_' + i + '" required />' +
            '<br>' +
            '<label for="nChoices_' + i + '">Number of choices</label>' +
            '<br>' +
            '<input type="number" name="nChoices_' + i + '" placeholder="number of choices" id="nChoices_' + i + '" required />' +
            '<br>' +
            '<button class="btn" type="button" id="choicesBtn_' + i + '">Enter choices</button>' +
            '<br><br>' +
            '<div id="choices_' + i + '"></div>' +
            '<br><br>' +
            '<label for="answer_' + i + '">The right choice</label>' +
            '<br>' +
            '<input type="text" name="answer_' + i + '" placeholder="the right choice (with THE SAME capital and small letters)" id="answer_' + i + '" required />' +
            '<br><br><br>';
    }

    // Attach event listeners to the newly created "Enter choices" buttons
    for (let i = 1; i <= nQuestions; i++) {
        document.getElementById('choicesBtn_' + i).addEventListener('click', function (event) {
            event.preventDefault();  // Prevent form submission

            const nChoices = document.getElementById('nChoices_' + i).value;
            const choices = document.getElementById('choices_' + i);

            // Clear previous choices to avoid multiple appends
            choices.innerHTML = '';

            for (let j = 1; j <= nChoices; j++) {
                choices.innerHTML += '<br>' +
                    '<label for="choice_' + j + '_for_' + i + '">Choice ' + j + '</label>' +
                    '<br>' +
                    '<input type="text" name="choice_' + j + '_for_' + i + '" placeholder="the choice" id="choice_' + j + '_for_' + i + '" required>';
            }
        });
    }
});


// document.getElementById('questionsBtn').addEventListener('click', function () {
//     const nQuestions = document.getElementById('nQuestions').value;
//     const questions = document.getElementById('questions');
//
//     for (let i = 1; i <= nQuestions; i++) {
//         questions.innerHTML += '<br>' +
//             '<label for="question_' + i + '">Question ' + i + '</label>' +
//             '<br>' +
//             '<input type="text" name="question_' + i + '" placeholder="the question" id="question_' + i + '" required />' +
//             '<br>' +
//             '<label for="mark_' + i + '">The mark for the question</label>' +
//             '<br>' +
//             '<input type="number" name="mark_' + i + '" placeholder="mark for the question" id="mark_' + i + '" required />' +
//             '<br>' +
//             '<label for="nChoices_' + i + '">Number of choices</label>' +
//             '<br>' +
//             '<input type="number" name="nChoices_' + i + '" placeholder="number of choices" id="nChoices_' + i + '" required />' +
//             '<br>' +
//             '<button class="btn" id="choicesBtn_' + i + '">Enter choices</button>' +
//             '<br><br>' +
//             '<div id="choices_' + i + '"></div>' +
//             '<br><br>';
//
//         document.getElementById('choicesBtn_' + i).addEventListener('click', function () {
//             let nChoices = document.getElementById('nChoices_' + i).value;
//             let choices = document.getElementById('choices_' + i);
//
//             for (let j = 1; j <= nChoices; j++) {
//                 choices.innerHTML += '<br>' +
//                     '<label for="choice_' + j + '_for_' + i + '">Choice ' + j + '</label>' +
//                     '<br>' +
//                     '<input type="text" name="choice_' + j + '_for_' + i + '" placeholder="the choice" id="choice_' + j + '_for_' + i + '" required>';
//             }
//
//         });
//     }
//
// });
//
// // document.getElementById('choicesBtn').addEventListener('click', function () {
// //     let nChoices = document.getElementById('nChoices').value;
// //     let choices = document.getElementById('choices');
// //
// //     for (let j = 1; j <= nChoices; j++) {
// //         choices.innerHTML += '<br>' +
// //             '<label for="choice_' + j + '">Choice ' + j + '</label>' +
// //             '<br>' +
// //             '<input type="text" name="choice_' + j + '" placeholder="the choice" id="choice_' + j + '" required>';
// //     }
// //
// // });
//
//
//
