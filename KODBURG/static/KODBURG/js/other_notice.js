let UserId = JSON.parse(document.getElementById("UserId").textContent);
let user_from = JSON.parse(document.getElementById("user_from").textContent);
let my__id = JSON.parse(document.getElementById("my-id").textContent);
let connect_from = JSON.parse(document.getElementById("con_user-from").textContent)
let connect_to = JSON.parse(document.getElementById("con_user-to").textContent);
let friend_button = document.querySelector(".friend");
let ac_web = new WebSocket("ws://" + window.location.host + "/ws/ac/" + connect_from + ".web." + connect_to + "/");


let ac = new WebSocket(
  "ws://" + window.location.host + "/ws/ac/TotalConsumer-" + UserId + "/"
);

ac.addEventListener("open", function (event) {
  console.log("Websocket connect...", event);
  ac.send(JSON.stringify({
    type: "request_notice",
    id_from: UserId
  }))
});

ac.addEventListener("error", function (event) {
  console.log("Websocket broke...", event);
});

ac.addEventListener("close", function (event) {
  console.log("Websocket disconnect...", event);
});

if (friend_button != null) {
  friend_button.addEventListener("click", function () {
    console.log("click!")
    let image_to = JSON.parse(document.getElementById("image_to").textContent);
    let to_user = JSON.parse(document.getElementById("user_to").textContent);
    ac_web.send(
      JSON.stringify({
        user_from: from_user,
        user_to: to_user,
        id_from: my__id,
        id_to: UserId,
        img_from: image_from,
        img_to: image_to,
        type: "Friend",
      })
    );
  });
}