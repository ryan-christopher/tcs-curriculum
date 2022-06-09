//constants
const colors = [
  "rgb(255, 0, 0)",
  "rgb(0, 255, 0)",
  "rgb(0, 0, 255)",
  "rgb(255, 0, 255)",
  "rgb(255, 255, 0)",
  "rgb(0, 255, 255)",
];

//select element
const squares = document.querySelectorAll(".square");

const colorDisplay = document.getElementById("colorDisplay");

const message = document.getElementById("message");

//helper functions
const pickColor = () => {
  //get random number between 0 and 5, inclusive
  const random = Math.floor(Math.random() * colors.length);
  return colors[random];
};

//choose winning color:
let pickedColor = pickColor();

//update color display
colorDisplay.textContent = pickedColor;

//set up squares
for (let i = 0; i < squares.length; i++) {
  squares[i].style.backgroundColor = colors[i];

  //add event listener
  squares[i].addEventListener("click", function () {
    //get color of picked square
    const clickedColor = this.style.backgroundColor;
    //compare that to pickedColor
    if (clickedColor === pickedColor) {
      message.textContent = "Correct! :-}";
      changeColors(pickedColor);
    } else {
      message.textContent = "You suck :{";
      this.style.backgroundColor = "#252525";
    }
  });
}

const changeColors = (color) => {
  squares.forEach((square) => {
    square.style.backgroundColor = color;
  });
};
