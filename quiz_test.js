//quiz and score test with js//

fetch("https://opentdb.com/api.php?amount=5&category=18&difficulty=medium&type=multiple&encode=url3986")
  .then(response => response.json())
  .then(data => {

    const questions = data.questions;

    let currentQuestion = 0;
    displayQuestion(questions[currentQuestion]);

    function displayQuestion(question) {
        console.log(question.text);

      
      for (let i = 0; i < question.choices.length; i++) {
        console.log(`${i + 1}. ${question.choices[i]}`);
      }

      
      let answer = prompt("Enter your answer (1, 2, 3, or 4):");

      
      if (answer == question.answer) {
        console.log("Correct!");
      } else {
        console.log("Incorrect.");
      }

      currentQuestion++;
      if (currentQuestion < questions.length) {
        displayQuestion(questions[currentQuestion]);
      } else {
        console.log("The game is over.");
      }
    }
  });
