var sec = 10;
function timer(){
    var timer = setInterval(function(){
        document.getElementById('timerdisplay').innerHTML=sec;
        sec--;
        if (sec < 0) {
            clearInterval(timer);
            checkscore();
        }
    }, 1000);
}

timer();

var score = 0;

function clicked(){
    if (sec > -1){
        score = score + 1;
        document.getElementById('scoredisplay').innerHTML=score;
        var average = score / 10;
        document.getElementById('avgnum').innerHTML=average + " per second";
    }
}


function restart(){
    if (sec > 0){
        sec = 10;
    }

    else if(sec <= 0){
        sec = 10;
        timer();
    };

    score = 0;
    document.getElementById('timerdisplay').innerHTML=sec;
    document.getElementById('scoredisplay').innerHTML=score;
    document.getElementById('results').classList.remove('hidden');
}


function checkscore(){
    if (score < 5){
        document.getElementById('results').innerHTML="Pretty bad...";
    }
    if (score >= 5 && score < 10){
        document.getElementById('results').innerHTML="Not terrible...";  
    }
    else if (score >= 10 && score < 15){
        document.getElementById('results').innerHTML="Decent..."; 
    }
    else if (score >= 15 && score < 20){
        document.getElementById('results').innerHTML="Not bad..."; 
    }
    else if (score >= 20 && score < 40){
        document.getElementById('results').innerHTML="Nice"; 
    }
    else if (score >= 40 && score < 80){
        document.getElementById('results').innerHTML="Epic"; 
    }
    else if (score >= 80 && score < 120){
        document.getElementById('results').innerHTML="Pro Gamer"; 
    }
    else if (score >= 120){
        document.getElementById('results').innerHTML="Legend"; 
    }
}