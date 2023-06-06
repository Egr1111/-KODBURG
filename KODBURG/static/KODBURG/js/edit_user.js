let email = document.querySelector(".email")
let email_confirm = document.querySelector(".email_confirm")

let email_now = email_confirm.href.split("/")
console.log(email_now[4])

email.addEventListener("input", function(){
    email_confirm.href = email_now[0] + "//" + email_now[2] + "/" + email_now[3] + "/" + email.value + "/"
})
