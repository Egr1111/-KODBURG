let burger_menu = document.querySelector(".burger-choice").classList;

// let burger_button_img_src = document.querySelector(".burger-img").src
let burger_button_img = document.querySelector(".burger-img").classList;
let burger_button = document.querySelector(".burger");
let list_counter = document.querySelectorAll(".list");
let no_blog = document.querySelector(".no_blog");
let no_projects = document.querySelector(".no_project");
let no_blog1 = document.querySelector(".no_blog1");
let no_projects1 = document.querySelector(".no_project1");
let no_other_blog = document.querySelectorAll(".trig-blog");
let no_other_projects = document.querySelectorAll(".trig_project");
let textarea = document.querySelector("textarea");
let notice = document.querySelector(".notice");
let friends = document.querySelector(".friends");
let descriptions = document.querySelector(".descr");
let image_from = JSON.parse(document.getElementById("image_from").textContent);
let from_user = JSON.parse(document.getElementById("user_from").textContent);
let my_id = JSON.parse(document.getElementById("my-id").textContent);
let connected = document.querySelectorAll(".connect");
let messaged = document.querySelectorAll(".chat");
let choices = document.querySelectorAll(".choice");

let my_clients = [];
let clients = [];
let my_chats = [];
let chats = [];

function Connections() {
  for (let i = 0; i < my_clients.length; i++) {
    my_clients[i].addEventListener("message", function (event) {
      let no_notice = document.querySelector(".no_notice");
      let no_friends = document.querySelector(".no_friends");
      let no_descriptions = document.querySelector(".no_descriptions");

      let new_event = JSON.parse(event.data);
      let type = new_event["type"];
      console.log("You got new message", new_event);
      let h_friends = friends.querySelector("h4");
      let h_notice = "";
      let h_descriptions = descriptions.querySelector("h4");

      if (type == "Friend") {
        if (new_event["msg_data"]["user_from"] != from_user) {
          if (new_event["type_notice"] == "NewDescription") {
            Notice(
              notice,
              h_notice,
              no_notice,
              new_event,
              "user_from",
              "id_from",
              "msg_to"
            );

            if (friend_button != null) {
              friend_button.innerHTML = "Принять заявку";
            }
          }
          if (new_event["type_notice"] == "NewFriend") {
            Notice(
              notice,
              h_notice,
              no_notice,
              new_event,
              "user_from",
              "id_from",
              "msg_to"
            );

            Friend_add(
              friends,
              h_friends,
              no_friends,
              new_event,
              "user_from",
              "id_from",
              "img_from"
            );
            Description_del(
              descriptions,
              new_event,
              "user_from",
              "last_description_to"
            );

            if (friend_button != null) {
              friend_button.innerHTML = "Удалить из друзей";
            }
          }
          if (new_event["type_notice"] == "DelDescription") {
            Notice(
              notice,
              h_notice,
              no_notice,
              new_event,
              "user_from",
              "id_from",
              "msg_to"
            );

            if (friend_button != null) {
              friend_button.innerHTML = "Добавить в друзья";
            }
          }
          if (new_event["type_notice"] == "DelFriend") {
            Notice(
              notice,
              h_notice,
              no_notice,
              new_event,
              "user_from",
              "id_from",
              "msg_to"
            );

            Description_add(
              descriptions,
              h_descriptions,
              no_descriptions,
              new_event,
              "user_from",
              "id_from",
              "img_from"
            );
            Friend_del(friends, new_event, "user_from", "last_friend_to");

            if (friend_button != null) {
              friend_button.innerHTML = "Отписаться";
            }
          }
        } else {
          if (new_event["type_notice"] == "NewDescription") {
            Notice(
              notice,
              h_notice,
              no_notice,
              new_event,
              "user_to",
              "id_to",
              "msg_from"
            );
            Description_add(
              descriptions,
              h_descriptions,
              no_descriptions,
              new_event,
              "user_to",
              "id_to",
              "img_to"
            );

            if (friend_button != null) {
              friend_button.innerHTML = "Отписаться";
            }
          }
          if (new_event["type_notice"] == "NewFriend") {
            Notice(
              notice,
              h_notice,
              no_notice,
              new_event,
              "user_to",
              "id_to",
              "msg_from"
            );
            Friend_add(
              friends,
              h_friends,
              no_friends,
              new_event,
              "user_to",
              "id_to",
              "img_to"
            );

            Description_del(
              descriptions,
              new_event,
              "user_to",
              "last_description_from"
            );

            if (friend_button != null) {
              friend_button.innerHTML = "Удалить из друзей";
            }
          }
          if (new_event["type_notice"] == "DelDescription") {
            Notice(
              notice,
              h_notice,
              no_notice,
              new_event,
              "user_to",
              "id_to",
              "msg_from"
            );
            Description_del(
              descriptions,
              new_event,
              "user_to",
              "last_description_from"
            );

            if (friend_button != null) {
              friend_button.innerHTML = "Добавить в друзья";
            }
          }
          if (new_event["type_notice"] == "DelFriend") {
            Notice(
              notice,
              h_notice,
              no_notice,
              new_event,
              "user_to",
              "id_to",
              "msg_from"
            );
            Friend_del(friends, new_event, "user_to", "last_friend_from");

            if (friend_button != null) {
              friend_button.innerHTML = "Принять заявку";
            }
          }
        }
      }
    });

    my_clients[i].addEventListener("error", function (event) {
      console.log("My websocket broken...", event);
    });

    my_clients[i].addEventListener("close", function (event) {
      console.log("My websocket disconnect...", event);
    });
  }
}

function Notice(
  notice,
  h_notice,
  no_notice,
  new_event,
  user_from,
  id_from,
  msg_to
) {
  if (notice.querySelector("h3") != null) {
    h_notice = notice.querySelector("h3");
  } else {
    h_notice = notice.querySelector("h4");
    h_notice.outerHTML =
      '<h3 class="card-title title-card col-12 text-center" >' +
      '<a href="kodburg/main/my_notice/" class="col-12 a_black">Уведомления</a></h3>';
    h_notice = notice.querySelector("h3");
  }
  if (no_notice == null) {
    if (notice.querySelectorAll("a").length > 3) {
      notice.removeChild(
        notice.querySelectorAll("a")[notice.querySelectorAll("a").length - 1]
      );
    }
  } else {
    notice.removeChild(no_notice);
  }
  notice.removeChild(h_notice);

  let new_not = document.createElement("a");
  new_not.href =
    "/kodburg/main/" +
    new_event["msg_data"][user_from] +
    "/" +
    new_event["msg_data"][id_from] +
    "/viewing/";
  new_not.className =
    "row col-12 text-center user-friend align-items-center m-0 p-0 flex-row flex-nowrap";
  new_not.innerHTML =
    "<div class = 'col new_notice'>" + new_event[msg_to] + "</div>";
  notice.prepend(new_not);
  notice.prepend(h_notice);
}

function Friend_add(
  friends,
  h_friends,
  no_friends,
  new_event,
  user_from,
  id_from,
  image_from
) {
  if (no_friends == null) {
    if (friends.querySelectorAll("a").length > 3) {
      friends.removeChild(
        friends.querySelectorAll("a")[friends.querySelectorAll("a").length - 1]
      );
    }
  } else {
    friends.removeChild(no_friends);
  }

  friends.removeChild(h_friends);
  let new_friend = document.createElement("a");
  new_friend.href =
    "/kodburg/main/" +
    new_event["msg_data"][user_from] +
    "/" +
    new_event["msg_data"][id_from] +
    "/viewing/";
  new_friend.className =
    "row col-12 text-center user-friend align-items-center m-0 p-0 flex-row flex-nowrap";
  new_friend.innerHTML =
    '<img src="' +
    new_event["msg_data"][image_from] +
    '" class="col-3" alt="">' +
    "<div class = 'col'>" +
    new_event["msg_data"][user_from] +
    "</div>";

  friends.prepend(new_friend);
  friends.prepend(h_friends);
}

function Friend_del(friends, new_event, user_from, last_friend_to) {
  for (let i = 0; i < friends.querySelectorAll("a").length; i++) {
    console.log(friends.querySelectorAll("a")[i]);
    if (
      friends.querySelectorAll("a")[i].innerText ==
      new_event["msg_data"][user_from]
    ) {
      friends.removeChild(friends.querySelectorAll("a")[i]);
      if (new_event[last_friend_to] != "") {
        friends.innerHTML +=
          '<a href="/kodburg/main/' +
          new_event[last_friend_to][0] +
          "/" +
          new_event[last_friend_to][1] +
          '/viewing/"' +
          'class="row col-12 text-center user-friend align-items-center m-0 p-0 flex-row flex-nowrap">' +
          '<img src="' +
          new_event[last_friend_to][2] +
          '" class="col-3" alt="">' +
          '<div class="col-9">' +
          new_event[last_friend_to][0] +
          "</div>" +
          "</a>";
      }
    }
  }
  if (friends.querySelectorAll("a").length == 1) {
    let new_noFriends = document.createElement("div");
    new_noFriends.className =
      "row justify-content-center align-items-center text-center g-2 no_friends";
    new_noFriends.innerHTML = '<div class="col">У Вас пока нет друзей</div>';
    friends.appendChild(new_noFriends);
  }
}

function Description_add(
  descriptions,
  h_descriptions,
  no_descriptions,
  new_event,
  user_from,
  id_from,
  img_from
) {
  if (no_descriptions == null) {
    if (descriptions.querySelectorAll("a").length > 3) {
      descriptions.removeChild(
        descriptions.querySelectorAll("a")[
          descriptions.querySelectorAll("a").length - 1
        ]
      );
    }
  } else {
    descriptions.removeChild(no_descriptions);
  }
  descriptions.removeChild(h_descriptions);

  let new_desc = document.createElement("a");
  new_desc.href =
    "/kodburg/main/" +
    new_event["msg_data"][user_from] +
    "/" +
    new_event["msg_data"][id_from] +
    "/viewing/";
  new_desc.className =
    "row col-12 text-center user-friend align-items-center m-0 p-0 flex-row flex-nowrap";
  new_desc.innerHTML =
    '<img src="' +
    new_event["msg_data"][img_from] +
    '" class="col-3" alt="">' +
    "<div class = 'col'>" +
    new_event["msg_data"][user_from] +
    "</div>";
  descriptions.prepend(new_desc);
  descriptions.prepend(h_descriptions);
}

function Description_del(
  descriptions,
  new_event,
  user_from,
  last_description_to
) {
  for (let i = 0; i < descriptions.querySelectorAll("a").length; i++) {
    if (
      descriptions.querySelectorAll("a")[i].innerText ==
      new_event["msg_data"][user_from]
    ) {
      descriptions.removeChild(descriptions.querySelectorAll("a")[i]);
      if (new_event[last_description_to] != "") {
        descriptions.innerHTML +=
          '<a href="/kodburg/main/' +
          new_event[last_description_to][0] +
          "/" +
          new_event[last_description_to][1] +
          '/viewing/"' +
          'class="row col-12 text-center user-friend align-items-center m-0 p-0 flex-row flex-nowrap">' +
          '<img src="' +
          new_event[last_description_to][2] +
          '" class="col-3" alt="">' +
          '<div class="col-9">' +
          new_event[last_description_to][0] +
          "</div>" +
          "</a>";
      }
    }
  }
  if (descriptions.querySelectorAll("a").length == 1) {
    let new_noDescriptions = document.createElement("div");
    new_noDescriptions.className =
      "row justify-content-center align-items-center text-center g-2 no_descriptions";
    new_noDescriptions.innerHTML =
      '<div class="col">Вы пока ни на кого не подписаны</div>';
    descriptions.appendChild(new_noDescriptions);
  }
}
if (messaged != null) {
  messaged.forEach((i) => {
    chats.push(i.textContent);
    my_chats.push(
      new WebSocket(
        "ws://" + window.location.host + "/ws/ac/" + i.textContent + "/"
      )
    );
  });
  for (let i = 0; i < my_chats.length; i++) {
    my_chats[i].addEventListener("message", function (event) {
      sound_message.play();
    });
  }
}

if (connected != null) {
  connected.forEach((i) => {
    clients.push(i.textContent);
    my_clients.push(
      new WebSocket(
        "ws://" + window.location.host + "/ws/ac/" + i.textContent + "/"
      )
    );
  });
  Connections();
}
let sound_message = new Audio(
  "http://" + window.location.host + "/static/KODBURG/sounds/sound_message.mp3"
);

let my_total = new WebSocket(
  "ws://" + window.location.host + "/ws/ac/TotalConsumer-" + my_id + "/"
);

my_total.addEventListener("open", function (event) {
  console.log("My websocket connect...", event);
});

my_total.addEventListener("message", function func(event) {
  console.log("My websocket get message...", event);
  let new_event = JSON.parse(event.data);
  let type = new_event["type"];

  if (type == "new_client") {
    let bool = false;
    if (
      clients.includes(new_event["request_id"] + ".web." + my_id) ||
      clients.includes(my_id + ".web." + new_event["request_id"])
    )
      bool = true;
    if (
      clients.includes(new_event["request_id"] + ".web." + my_id) == false &&
      bool == false
    ) {
      console.log(bool);
      my_clients.push(
        new WebSocket(
          "ws://" +
            window.location.host +
            "/ws/ac/" +
            new_event["request_id"] +
            ".web." +
            my_id +
            "/"
        )
      );
      clients.push(new_event["request_id"] + ".web." + my_id);
      my_total.send(
        JSON.stringify({
          type: "new_client",
          id_from: new_event["request_id"],
        })
      );
      Connections();
      bool = true;
    }

    if (
      clients.includes(my_id + ".web." + new_event["request_id"]) == false &&
      bool == false
    ) {
      console.log(bool);
      my_clients.push(
        new WebSocket(
          "ws://" +
            window.location.host +
            "/ws/ac/" +
            my_id +
            ".web." +
            new_event["request_id"] +
            "/"
        )
      );
      clients.push(my_id + ".web." + new_event["request_id"]);
      my_total.send(
        JSON.stringify({
          type: "new_client",
          id_from: new_event["request_id"],
        })
      );
      Connections();
      bool = true;
    }
  }

  if (type == "check_notice") {
    if (new_event["new_notice"] && notice.querySelectorAll("h4")) {
      let h_notice = "";

      h_notice = notice.querySelector("h4");
      h_notice.outerHTML =
        '<h3 class="card-title title-card col-12 text-center" >' +
        '<a href="kodburg/main/my_notice/" class="col-12 a_black">Уведомления</a></h3>';
      h_notice = notice.querySelector("h3");
    }
  }
  if (type == "request_chat") {
    if (chats.includes(new_event["request"]["room_name"]) == false) {
      my_chats.push(
        new WebSocket(
          "ws://" +
            window.location.host +
            "/ws/ac/" +
            new_event["request"]["room_name"] +
            "/"
        )
      );
      chats.push(new_event["request"]["room_name"]);
      for (let i = 0; i < my_chats.length; i++) {
        my_chats[i].addEventListener("message", function (event) {
          sound_message.play();
          choices[2].innerHTML += "<div class='new_mes'></div>";
        });
      }
    }
  }
});
my_total.addEventListener("error", function (event) {
  console.log("My websocket break...", event);
});

my_total.addEventListener("close", function (event) {
  console.log("My websocket disconnect...", event);
});

function burger_open_close() {
  burger_menu.toggle("active");
}

burger_button.addEventListener("click", burger_open_close);
