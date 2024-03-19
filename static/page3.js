let score = document.querySelector(".score");
function getValue(){
  let inputValue = parseInt(document.getElementById('id').value);
  if (isNaN(inputValue)) {
    alert("Please enter a valid number.");
    return;
  }
  let needle = document.querySelector(".needle");
  needle.style.setProperty("--score", inputValue);
  score.innerText=inputValue;
}