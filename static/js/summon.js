
function tryToSummon() {
    let pointsCount = document.getElementById('pointsCount')
    let result = document.getElementById('result')
    let img = document.getElementById('result-image')

    fetch("/game/summon", {
        method: "POST"
      }).then(res => {
        res.json().then(data => {
            pointsCount.innerHTML = "Your current Blue Coins: " + data.blue_coins
            result.innerHTML = data.message
            if (data.img != '') {
                fetch(data.img)
                  .then(response => response.blob())
                  .then(imageBlob => {
                      let imageObjectURL = URL.createObjectURL(imageBlob)
                      img.src = imageObjectURL
                      img.style.visibility = "visible"
                  });
            } else {
                img.style.visibility = "hidden"
            }
        })
      });
}
