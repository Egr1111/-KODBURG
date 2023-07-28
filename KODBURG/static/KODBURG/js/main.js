console.log("main.py");

let burger_menu = document.querySelector(".burger-choice").classList;
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
let notice_box = document.querySelector(".right-column");
let friends = document.querySelector(".friends");
let descriptions = document.querySelector(".descr");
let other_box = document.querySelector(".left-column");
let image_from = JSON.parse(document.getElementById("image_from").textContent);
let from_user = JSON.parse(document.getElementById("user_from").textContent);
let my_id = JSON.parse(document.getElementById("my-id").textContent);
let connected = document.querySelectorAll(".connect");
let messaged = document.querySelectorAll(".chat_connect");
let choices = document.querySelectorAll(".choice");
let messager_choices = document.querySelectorAll(".messager");
let like = document.querySelectorAll(".like");
let dislike = document.querySelectorAll(".dislike");
let header = document.querySelector(".header-main");
let input_user = document.querySelector(".user-input");
let users = document.querySelectorAll(".user-reach");
let all_users = document.querySelector(".all-users");
let window_check = window.pageYOffset;
let box_top = window_check + "";

let my_clients = [];
let clients = [];
let my_chats = [];
let chats = [];

let sound_message = new Audio(
  "http://" + window.location.host + "/static/KODBURG/sounds/sound_message.mp3"
);

let my_total = new WebSocket(
  "ws://" + window.location.host + "/ws/ac/TotalConsumer-" + my_id + "/"
);

if (notice_box != null) {
  notice_box.style.top = box_top + "px";
  other_box.style.top = box_top + "px";
}

document.addEventListener("scroll", function () {
  let window_check = window.pageYOffset;
  let box_top = window_check + "";

  console.log(window_check, box_top);
  notice_box.style.top = box_top + "px";
  other_box.style.top = box_top + "px";
});

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
              "last_description_to",
              no_descriptions
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
              "last_description_from",
              no_descriptions
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
              "last_description_from",
              no_descriptions
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
      '<a href="main/my_notice/" class="col-12 a_black">Уведомления</a></h3>';
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
    "/main/" +
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
    "/main/" +
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
          '<a href="/main/' +
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
  console.log(no_descriptions);
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
    "/main/" +
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
  last_description_to,
  no_descriptions
) {
  for (let i = 0; i < descriptions.querySelectorAll("a").length; i++) {
    if (
      descriptions.querySelectorAll("a")[i].innerText ==
      new_event["msg_data"][user_from]
    ) {
      descriptions.removeChild(descriptions.querySelectorAll("a")[i]);
      if (new_event[last_description_to] != "") {
        descriptions.innerHTML +=
          '<a href="/main/' +
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
  if (
    descriptions.querySelectorAll("a").length == 1 &&
    no_descriptions == null
  ) {
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
            sound_message.play();
          }
        }
      }
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

my_total.addEventListener("open", function (event) {
  console.log("My websocket connect...", event);
});

my_total.addEventListener("message", function (event) {
  console.log("My websocket get message...", event);
  let new_event = JSON.parse(event.data);
  let type = new_event["type"];
  if (type == "results_search") {
    let results = new_event["results"];
    if (results != {}) {
      all_users.innerHTML = "";
      for (let [key, value] of Object.entries(results)) {
        let user = document.createElement("a");
        let user_img = document.createElement("img");
        let user_username = document.createElement("div");

        user.href = "/main/" + value[0] + "/" + key + "/viewing/";
        user.className = "col-lg-4 col-sm-2 col-12 row user-reach p-2";

        user_img.src = "http://" + window.location.host + "/media/" + value[1];
        user_img.className = "col-sm-10 col-3";

        user_username.className = "col-sm-12 col username";
        user_username.innerHTML = value[0];

        user.append(user_img);
        user.append(user_username);

        all_users.prepend(user);
      }
    }
  }
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
        '<a href="main/my_notice/" class="col-12 a_black">Уведомления</a></h3>';
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
  alert("Неожиданная ошибка! Перезагрузите страницу!");
});

burger_button.addEventListener("click", function () {
  burger_menu.toggle("active");
});

for (let i = 0; i < like.length; i++) {
  like[i].addEventListener("click", function () {
    my_total.send(
      JSON.stringify({
        id: like[i].id,
        type_post: like[i].name,
        type: "like",
      })
    );
    if (like[i].classList.contains("a_like")) {
      like[i].classList.remove("a_like");
      like[i].classList.remove("btn-outline-danger");
      like[i].classList.add("btn-danger");

      like[i].textContent = parseInt(like[i].textContent) + 1;
    } else {
      like[i].classList.add("a_like");
      like[i].classList.add("btn-outline-danger");
      like[i].classList.remove("btn-danger");
      if (parseInt(like[i].textContent) > 0)
        like[i].textContent = parseInt(like[i].textContent) - 1;
    }
    if (!dislike[i].classList.contains("a_dislike")) {
      dislike[i].classList.add("a_dislike");
      dislike[i].classList.add("btn-outline-dark");
      dislike[i].classList.remove("btn-dark");
      if (parseInt(dislike[i].textContent) > 0)
        dislike[i].textContent = parseInt(dislike[i].textContent) - 1;
    }
  });
}

for (let i = 0; i < dislike.length; i++) {
  dislike[i].addEventListener("click", function () {
    console.log(dislike[i].attributes["id"]);
    my_total.send(
      JSON.stringify({
        id: dislike[i].id,
        type_post: dislike[i].name,
        type: "dislike",
      })
    );
    if (dislike[i].classList.contains("a_dislike")) {
      dislike[i].classList.remove("a_dislike");
      dislike[i].classList.remove("btn-outline-dark");
      dislike[i].classList.add("btn-dark");
      dislike[i].textContent = parseInt(dislike[i].textContent) + 1;
    } else {
      dislike[i].classList.add("a_dislike");
      dislike[i].classList.add("btn-outline-dark");
      dislike[i].classList.remove("btn-dark");

      if (parseInt(dislike[i].textContent) > 0)
        dislike[i].textContent = parseInt(dislike[i].textContent) - 1;
    }

    if (!like[i].classList.contains("a_like")) {
      like[i].classList.add("a_like");
      like[i].classList.add("btn-outline-danger");
      like[i].classList.remove("btn-danger");

      like[i].textContent = parseInt(like[i].textContent) - 1;
    }
  });
}
if (input_user != null) {
  input_user.addEventListener("input", function () {
    all_users.innerHTML = "";
    my_total.send(
      JSON.stringify({
        text: input_user.value,
        type: "search",
      })
    );
  });
}
