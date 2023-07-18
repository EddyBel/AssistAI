function hiddenAndWatchConversationsMenu(state) {
  if (state) ELEMENTS.menuConversation.classList.add("view");
  else ELEMENTS.menuConversation.classList.remove("view");
}
