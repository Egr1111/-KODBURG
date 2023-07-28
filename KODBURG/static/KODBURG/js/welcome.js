let container = document.querySelector(".container-fluid");
let errors = document.querySelectorAll(".error");

if (errors.length != 0) {
  container.scrollBy(0, container.scrollHeight);
  console.log(errors);
}
