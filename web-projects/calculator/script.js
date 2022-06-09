clearoutput = () => {
    document.getElementById("output").innerHTML = "0";
}

removeZero = () => {
    var value = document.getElementById("output").innerHTML;
    if (value == "0") {
        value = " ";
        document.getElementById("output").innerHTML = value;
    }
}


percent = () => {
    var value = document.getElementById("output").innerHTML;
    value = value / 100;
    document.getElementById("output").innerHTML = value;
}

updateDisplay = value => {
    removeZero()
    document.getElementById("output").innerHTML += value;
}

solve = () => {
    var equation = document.getElementById("output").innerHTML;
    if (equation != "0"){
        var solved = eval(equation);
        document.getElementById("output").innerHTML = solved;
    }
}

keyboard_codes = [
    "1", "2", "3", "4", "5", "6", "7", "8",
    "9", "0", "*", "/", "%", "+", "Enter", "-",
    "Backspace", "."
]

keyboard_numbers = (event) => {
    if (keyboard_codes.includes(event.key)) {
        if (event.key === "Enter"){
            solve();
        }
        else if (event.key === "Backspace" && document.getElementById("output").innerHTML.length > 2){
            var input = document.getElementById("output").innerHTML;
            document.getElementById("output").innerHTML = input.slice(0, input.length-1);
        }
        else if (event.key === "Backspace" && document.getElementById("output").innerHTML.length == 1 ){
            document.getElementById("output").innerHTML = "0";
        }
        else if (event.key === "Backspace" && document.getElementById("output").innerHTML.length == 2 ){
            document.getElementById("output").innerHTML = "0";
        }
        else if (event.key === "%"){
            percent();
        }
        else{
            updateDisplay(event.key);
        }
    }
}

addEventListener("keydown", keyboard_numbers);