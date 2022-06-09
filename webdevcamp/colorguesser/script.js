var heading;
heading = document.getElementById('colorValue');
var buttons;
buttons = document.getElementsByClassName('colorButton');
var background;
background = document.getElementById("game");



function setButtonColor(button, red, green, blue){
  button.setAttribute('style', 
        'background-color: rgb(' + red + ',' + green + ',' + blue + ');');
}

function makeColorValue(){
  return Math.round(Math.random() * 255);
}

function startGame(){

  var answerButton = Math.round(Math.random() * (buttons.length - 1));
  var answerMessage = document.getElementById('answer');
  
  answerMessage.innerHTML = "Choose a color";
  background.setAttribute('style', 'background-color: #2c2c2c;');

  for (var i = 0; i < buttons.length; i++){
    var red = makeColorValue();
    var green = makeColorValue();
    var blue = makeColorValue();

    setButtonColor(buttons[i],red, green, blue);
    if (i === answerButton){
      heading.innerHTML = `(${red}, ${green}, ${blue})`;
    }

    buttons[i].addEventListener('click', function(){
      if (this === buttons[answerButton]){
        answerMessage.innerHTML = "Correct!";
        background.setAttribute('style', 'background-color: green;');
      }
      else{
        answerMessage.innerHTML = "Wrong! Guess again.";
        background.setAttribute('style', 'background-color: red;');
      }
    });
  }
}
startGame();

document.getElementById('resetButton').addEventListener('click', startGame);