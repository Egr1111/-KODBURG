let room_name = JSON.parse(document.getElementById("room-name").textContent);
let chat_log = document.querySelector(".chat_log");
let chat_message = document.getElementById("chat_message");
let chat_button = document.getElementById("chat_button");
let user_from = JSON.parse(document.getElementById("user_from").textContent);
let user_to = JSON.parse(document.getElementById("user_to").textContent);
let image = JSON.parse(document.getElementById("image").textContent);
let msg_to = document.querySelectorAll(".msg_to");
let msg_to_msg = document.querySelector(".msg_to");
let msg_from = document.querySelector(".msg_from");
let msg_from_msg = document.querySelectorAll(".msg_from");
let non_read = document.querySelectorAll(".non_read");
let non_viewed = document.querySelectorAll(".non_viewed");
let first_message = document.querySelector(".first_message");
let UserId = JSON.parse(document.getElementById("User_id").textContent);
let main_notmain = document.querySelector(".main-notmain");
let my__id = JSON.stringify(document.getElementById("my_id").textContent);
let room_id = JSON.stringify(document.getElementById("room-id").textContent);
let Visible = function (target) {
  // Все позиции элемента
  console.log(target);
  var targetPosition = {
      top: window.pageYOffset + target.getBoundingClientRect().top,
      left: window.pageXOffset + target.getBoundingClientRect().left,
      right: window.pageXOffset + target.getBoundingClientRect().right,
      bottom: window.pageYOffset + target.getBoundingClientRect().bottom,
    },
    // Получаем позиции окна
    windowPosition = {
      top: window.pageYOffset,
      left: window.pageXOffset,
      right: window.pageXOffset + document.documentElement.clientWidth,
      bottom: window.pageYOffset + document.documentElement.clientHeight,
    };

  if (
    targetPosition.bottom > windowPosition.top && // Если позиция нижней части элемента больше позиции верхней чайти окна, то элемент виден сверху
    targetPosition.top < windowPosition.bottom && // Если позиция верхней части элемента меньше позиции нижней чайти окна, то элемент виден снизу
    targetPosition.right > windowPosition.left && // Если позиция правой стороны элемента больше позиции левой части окна, то элемент виден слева
    targetPosition.left < windowPosition.right
  ) {
    // Если позиция левой стороны элемента меньше позиции правой чайти окна, то элемент виден справа
    // Если элемент полностью видно, то запускаем следующий код
    // setInterval(1000, target.style.background = "white")

    let msg = target.querySelector(".message");
    let msg_id = msg.textContent;
    console.log(msg_id);
    console.log(UserId);
    ac.send(
      JSON.stringify({
        user_from: "",
        msg_id: msg_id,
        my_id: my_id,
        user_read: UserId,
      })
    );
    target.classList.add("read");
    target.classList.remove("non_read");
    let non_read = document.querySelectorAll(".non_read");
    console.log(non_read);
  }
};

let total = new WebSocket(
  "ws://" + window.location.host + "/ws/ac/TotalConsumer-" + UserId + "/"
);

let ac = new WebSocket(
  "ws://" + window.location.host + "/ws/ac/" + room_name + "/"
);

total.addEventListener("open", function (event) {
  console.log("Total websocket connect...", event);
  total.send(
    JSON.stringify({
      room_name: room_name,
      room_id: room_id,
      user_from_username: user_from,
      user_from: my__id,
      image: image,
      type: "request_msg",
    })
  );
});
total.addEventListener("close", function (event) {
  console.log("Total websocket disconnect...", event);
});

let vis = "";
ac.addEventListener("open", function (event) {
  console.log("Websocket connect...", event);
  if (event) {
    if (non_read.length != 0) {
      for (let i = 0; i < non_read.length; i++) {
        Visible(non_read[i]);
      }
    }
    window.addEventListener("mousemove", function () {
      let non_read = document.querySelectorAll(".non_read");
      if (non_read.length != 0) {
        for (let i = 0; i < non_read.length; i++) {
          Visible(non_read[i]);
        }
      }
    });
  }
});

ac.addEventListener("message", function (event) {
  console.log("You get message...", event);

  let new_event = JSON.parse(event.data);
  let type = new_event["type"];
  console.log(type, new_event["msg"]["user_from"]);
  if (type == "check_msg-check_viewed") {
    console.log(type, new_event["msg"]["my_id"]);
    if (new_event["msg"]["my_id"] == my_id) {
      messager_choices.forEach((i) => {
        i.removeChild(document.querySelector(".new_mes"));
      });
    }
  }
  if (type == "check_msg") {
    if (new_event["msg"]["user_from"] != "") {
      if (new_event["msg"]["user_to"] == from_user) {
        messager_choices.forEach((i) => {
          i.innerHTML =
            "<div class='col p-0 m-0'>Messager</div> <div class='new_mes'></div>";
        });
      }
    }
  }

  msg = JSON.parse(event.data)["msg"];
  console.log(msg);

  if (msg["user_from"] != "") {
    if (msg["user_from"] == user_from) {
      chat_log.innerHTML +=
        '<div class="msg_from col-12">' +
        '<div class="col-10 row align-self-start justify-content-end">' +
        '<div class="row col-12 justify-content-end text-end">' +
        '<div class="col text-decoration-underline">' +
        msg["user_from"] +
        "</div>" +
        "</div>" +
        '<div class="col-12 message">' +
        msg["msg"] +
        "</div>" +
        "</div>" +
        '<div class="img"><img src="' +
        msg["image"] +
        '" class="col" alt="">' +
        "</div>" +
        '<script class="non_viewed" type="application/json">' +
        msg["msg"] +
        "</script>" +
        "</div>";
      console.log("1");
      chat_log.scrollBy(0, chat_log.scrollHeight);
      if (no_messages != null) {
        console.log("2.1");
        console.log(no_messages);
        chat_log.removeChild(no_messages);
      }
    } else {
      chat_log.innerHTML +=
        '<div class="msg_to col-12 non_read">' +
        '<div class="col-10 row align-self-start">' +
        '<a href="/kodburg/main/' +
        msg["user_from"] +
        "/" +
        UserId +
        '/viewing" class="col-12 text-decoration-underline a_black">' +
        msg["user_from"] +
        "</a>" +
        '<div class="col-12 message">' +
        msg["msg"] +
        "</div>" +
        "</div>" +
        '<div class="img"><img src="' +
        msg["image"] +
        '" class="col" alt="">' +
        "</div>" +
        '<script class="non_viewed" type="application/json">' +
        msg["msg_id"] +
        "</script>" +
        "</div>";
      console.log("1");

      // if (no_messages != null) {
      //   console.log("2.1");
      //   console.log(no_messages);
      //   no_messages.remove(chat_log);

      // }
      let non_read = document.querySelectorAll(".non_read");
      Visible(non_read[non_read.length - 1]);
    }
  } else {
    let msg_from_msg = document.querySelectorAll(".msg_from");
    console.log(msg_from_msg);
    if (msg["user_read"] != my__id) {
      console.log("log");
      for (let i = 0; i < msg_from_msg.length; i++) {
        if (
          msg_from_msg[i].classList.contains("read") == false &&
          msg_from_msg[i].querySelector(".message").textContent == msg["msg_id"]
        ) {
          msg_from_msg[i].classList.add("read");
        }
      }
    }
  }
});

ac.addEventListener("error", function (event) {
  console.log("Websocket break from error...", event);
});

ac.addEventListener("close", function (event) {
  console.log("Websocket disconnect...", event);
  alert("Неожиданная ошибка! Перезагрузите страницу.");
});

let no_messages = document.querySelector(".no_messages");

function first_mess(message) {
  console.log(message.getBoundingClientRect().top);
  chat_log.scrollBy(0, message.getBoundingClientRect().top);
}
console.log(first_message);
if (first_message != null) {
  first_mess(first_message);
} else {
  chat_log.scrollBy(0, chat_log.scrollHeight);
}
// else{
//   chat_log.scrollBy(0, chat_log.scrollHeight)
// }

chat_button.addEventListener("click", function () {
  console.log("click!");
  console.log(chat_message.value);
  if (chat_message.value != "") {
    ac.send(
      JSON.stringify({
        user_from: user_from,
        user_to: user_to,
        image: image,
        msg: chat_message.value,
        id: my__id,
        type: "chat_msg",
      })
    );
    chat_message.value = "";
  }
});
