let room_name = document.querySelectorAll(".room-name");
let last_chat = document.querySelectorAll(".last_chat_log");
let message = document.querySelector(".message");
let user_chat = document.querySelectorAll(".user_chat");
let all_chat = document.querySelector(".all_chat");
let chat = document.querySelectorAll(".chat");
let room_id = document.querySelectorAll(".room_id");
let limit_time = document.querySelector(".limit_time");
let id_from = JSON.parse(document.getElementById("my-id").textContent);
let main = document.querySelector(".main")
let no_chats = document.querySelector(".no_chats")


let list = [];
let list3 = [];
let list4 = [];

let total = new WebSocket(
  "ws://" + window.location.host + "/ws/ac/TotalConsumer-" + id_from + "/"
);

total.addEventListener("open", function (event) {
  console.log("Total websocket connect...", event);
});

total.addEventListener("message", function (event) {
  console.log(event);
  let new_event = JSON.parse(event.data);
  let type = new_event["type"];
  if (type == "request_chat") {
    if (no_chats != null){
      all_chat.removeChild(no_chats)
    }
    
    let new_room = new_event["request"];
    if (list4.includes(new_room["room_name"]) == false) {
      console.log(list4);
      list.push(
        new WebSocket(
          "ws://" +
            window.location.host +
            "/ws/ac/" +
            new_room["room_name"] +
            "/"
        )
      );
      list3.push(new_room["room_id"]);
      list4.push(new_room["room_name"]);
      console.log(parseFloat(new_room["User_id"]));
      new_room["User_id"] = new_room["User_id"].replace('"', "");
      console.log("New contact!");
      all_chat.innerHTML +=
        "<a href='/kodburg/main/chat/" +
        parseFloat(new_room["User_id"]) +
        id_from +
        "/' class='row col-12 justify-content-between align-items-center g-2 border-bottom border-top p-3 flex-nowrap a_black list chat'>" +
        '<div class="img">' +
        '<img src="' +
        new_room["image"] +
        '" class="col" alt="">' +
        "</div>" +
        '<div class="row justify-content-center align-items-center g-2">' +
        '<div class="row justify-content-center align-items-center g-2">' +
        '<div class="col a_black text-decoration-underline user_chat">' +
        new_room["user_chat"] +
        "</div>" +
        "</div>" +
        '<div class="row col-12 justify-content-start last_chat_log">' +
        '<div class="col-10 text-start message" style="word-break: break-all;">Напишите первое сообщение!' +
        "<div class='new_mes'></div>" +
        "</div>" +
        "</div>" +
        "</div>" +
        "<div class='room-name' style='display: none;'>" +
        new_room["room_name"] +
        "</div>" +
        "<script class='User_id' type='application/json'>" +
        new_room["User_id"] +
        "</script>" +
        "</a>";

      console.log(user_chat);

      for (let i = 0; i < list.length; i++) {
        list[i].addEventListener("open", function (event) {
          console.log("Websocket connected...", event);
        });

        list[i].addEventListener("message", function (event) {
          console.log("You got message...", event);
          message = JSON.parse(event.data)["msg"];

          for (let i = 0; i < list4.length; i++) {
            let all_chat = document.querySelector(".all_chat");
            let chat = document.querySelectorAll(".chat");
            let last_chat = document.querySelectorAll(".last_chat_log");
            let user_chat = document.querySelectorAll(".user_chat");
            if (message["user_from"] != "") {
              console.log(last_chat);
              console.log(
                message["msg"],
                user_chat[i].textContent,
                message["user_from"]
              );
              if (message["user_from"] == user_chat[i].textContent) {
                last_chat[i].innerHTML =
                  '<div class="col-10 text-start message" style="word-break: break-all;">' +
                  message["user_from"] +
                  ": " +
                  message["msg"] +
                  "</div>" +
                  '<div class="new_mes"></div>';
                let new_mes = chat[i];
                all_chat.removeChild(new_mes);
                all_chat.prepend(new_mes);
                // sound_message.play();
                break;
              }
            }
            if (message["user_from"] == "") {
              if (
                (message["user_read"] + id_from == list3[i]) |
                (id_from + message["user_read"] == list3[i])
              ) {
                last_chat[i].removeChild(document.querySelector(".new_mes"));
                console.log(1);
                break;
              } else {
                console.log(2);
              }
            }
          }
        });

        list[i].addEventListener("error", function (event) {
          console.log("Websocket brocken...", event);
        });

        list[i].addEventListener("close", function (event) {
          console.log("Websocket disconnected...", event);
          limit_time.innerHTML =
            '<div class="alert alert-danger" role="alert"><strong>Время ожидания вышло! </strong><a href="' +
            window.location +
            '" class="alert-link">Пожалуйста, перезагрузите страницу</a></div>';
        });
      }
    }
  }
});

for (let i = 0; i < room_name.length; i++) {
  list.push(
    new WebSocket(
      "ws://" +
        window.location.host +
        "/ws/ac/" +
        room_name[i].textContent +
        "/"
    )
  );
}

for (let i = 0; i < room_id.length; i++) {
  list3.push(room_id[i].textContent);
}

for (let i = 0; i < room_name.length; i++) {
  list4.push(room_name[i].textContent);
}

console.log(list);

for (let i = 0; i < list.length; i++) {
  list[i].addEventListener("open", function (event) {
    console.log("Websocket connected...", event);
  });

  list[i].addEventListener("message", function (event) {
    console.log("You got message...", event);
    message = JSON.parse(event.data)["msg"];
    for (let i = 0; i < room_name.length; i++) {
      if (message["user_from"] != "") {
        console.log(
          message["msg"],
          user_chat[i].textContent,
          message["user_from"]
        );
        if (message["user_from"] == user_chat[i].textContent) {
          last_chat[i].innerHTML =
            '<div class="col-10 text-start message" style="word-break: break-all;">' +
            message["user_from"] +
            ": " +
            message["msg"] +
            "</div>" +
            '<div class="new_mes"></div>';
          let chat_message = chat[i];
          all_chat.removeChild(chat_message);
          all_chat.prepend(chat_message);
          sound_message.play();

          break;
        }
      }
      if (message["user_from"] == "") {
        if (
          (message["user_read"] + id_from == list3[i]) |
          (id_from + message["user_read"] == list3[i])
        ) {
          last_chat[i].removeChild(document.querySelector(".new_mes"));
          console.log(1);
          break;
        } else {
          console.log(2);
        }
      }
    }
  });

  list[i].addEventListener("error", function (event) {
    console.log("Websocket brocken...", event);
  });

  list[i].addEventListener("close", function (event) {
    console.log("Websocket disconnected...", event);
    limit_time.innerHTML =
      '<div class="alert alert-danger" role="alert"><strong>Время ожидания вышло!</strong><a href="' +
      window.location +
      '" class="alert-link">Пожалуйста, перезагрузите страницу</a></div>';
  });
}

// ac.addEventListener("open", function(event){
//     console.log("Websocket connected...", event)
// })

// ac.addEventListener("message", function (event) {
//   console.log("You got message...", event);

// });

// ac.addEventListener("error", function (event) {
//   console.log("Websocket brocken...", event);
// });

// ac.addEventListener("close", function (event) {
//   console.log("Websocket disconnected...", event);
//   alert(
//     "Время ожидания вышло! Пожалуйста, перезагрузите страницу прежде чем продолжить пользоваться ею. В противном случае это может привести к некторым неудобствам, которые в конечном итоге вынудят Вас перезагрузить страницу."
//   );
// })
