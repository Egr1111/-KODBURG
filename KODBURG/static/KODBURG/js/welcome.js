let errors = document.querySelectorAll(".errorlist");
let container = document.querySelector(".container-fluid");
if (errors != null){
    container.scrollBy(0, errors[errors.length - 1].scrollHeight)
} 