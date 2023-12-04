function checkAnswer() {
  var userAnswer = document.getElementById("answer").value;

  var correctAnswer = "yourAnswer";
  if (userAnswer.toLowerCase() === correctAnswer.toLowerCase()) {
      openPopup("correct.html");
  } else {
   openPopup("incorrect.html");
  }
}
function openPopup(page) {
  window.open(page, "_blank");
}
function tryAgain() {
  window.close();
}
function nextMission() {
  window.close();
}


function exitClick(){
    openPopup('exit.html')
}