const chatMenu = document.querySelector(".section-chat");
const mainContent = document.querySelector(".content");
const buttonChat = document.querySelector(".navbar-button-menu");

buttonChat.addEventListener("click", () => {
  chatMenu.classList.add("view");
  get_updated_conversation();
});
mainContent.addEventListener("click", () => {
  chatMenu.classList.remove("view");
});
