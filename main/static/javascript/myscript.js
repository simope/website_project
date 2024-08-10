async function startGame(hand){
    // Hide the game fields while preparing for the new game
    hideFields();
  
    // Retain the hover opacity on the hand that is being played
    document.getElementById(hand).style.opacity = 1;
  
    // Put the selected hand in the game field, player's side
    changeHand(hand, "player");
  
    // Generate a random hand for the computer
    randomNum = Math.floor(Math.random() * 3) + 1;
  
    // Put it in the computer's field
    changeHand(randomNum, "comp");
  
    // Write "Loading"
    gameText("Loading...");
  
    await sleep(1000);
  
    // Show the game fields
    showFields();
  
    // Checking result of the match
    var result = checkResult(hand, randomNum);
    console.log(result);
  
    // Write Win, Lose or Tie
    gameText(result);
  
    // Remove the opacity from the selected hand
    document.getElementById(hand).style.opacity = 0.3;
  
    // Save to DB
    saveToDB(result);
  }
  
  function gameText(string){
    document.getElementById("gameText").innerHTML = string;
  }
  
  function hideFields(){
    let playersHand = document.getElementById("playersHandImg");
    let computersHand = document.getElementById("computersHandImg");
    playersHand.style.opacity = 0;
    computersHand.style.opacity = 0;
  }
  
  function showFields(){
    let playersHand = document.getElementById("playersHandImg");
    let computersHand = document.getElementById("computersHandImg");
    playersHand.style.opacity = 1;
    computersHand.style.opacity = 1;
  }
  
  function changeHand(hand, field) {
    if (field === "player"){
      var id = "playersHandImg";
    }else{
      var id = "computersHandImg";
    }
  
    switch (true){
      case (hand == 'rock' || hand == 1):
        document.getElementById(id).src = rock;
        break;
      case (hand == 'paper' || hand == 2):
          document.getElementById(id).src = paper;
          break;
      case (hand == 'scissors' || hand == 3):
        document.getElementById(id).src = scissors;
        break;
    }
  }
  
  function sleep(ms = 0) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
  function checkResult(hand, randomNum){
    switch (hand){
      case 'rock':
        switch (randomNum){
          case 1:
            result = "Tie";
            break;
          case 2:
            result = "Lose";
            break;
          case 3:
            result = "Win";
            break;
        }
        break;
  
      case 'paper':
        switch (randomNum){
          case 1:
            result = "Win";
            break;
          case 2:
            result = "Tie";
            break;
          case 3:
            result = "Lose";
            break;
        }
        break;
  
      case 'scissors':
        switch (randomNum){
          case 1:
            result = "Lose";
            break;
          case 2:
            result = "Win";
            break;
          case 3:
            result = "Tie";
            break;
        }
        break;
    }
    return result;
  }
  
  function saveToDB(res){
    // Send POST request with the result of the match
    const resultData = {result: res};
  
    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'save-to-DB/', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(resultData));
  }
  
  function reload(){
    location.reload();
  }