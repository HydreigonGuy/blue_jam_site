
function select(id) {
    fetch("/game/select", {
        method: "POST",
        body: JSON.stringify({'id':id})
      }).then(res => {
      });
}
