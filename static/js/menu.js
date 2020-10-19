const burger_menu = document.querySelector("#burger-menu");
const menu = document.querySelector("#menu");

burger_menu.addEventListener("click", () => {
  if (menu.classList.contains("hidden")) {
    menu.classList.remove("hidden");
  } else {
    menu.classList.add("hidden");
  }
});
