const burger_menu = document.querySelector("#burger-menu");
const menu = document.querySelector("#menu");
const message = document.querySelector("#alert-message");

burger_menu.addEventListener("click", () => {
  if (menu.classList.contains("hidden")) {
    menu.classList.remove("hidden");
  } else {
    menu.classList.add("hidden");
  }
});

const fadeout = () => {
  message.classList.add("hidden");
};

setTimeout(fadeout, 3000);
