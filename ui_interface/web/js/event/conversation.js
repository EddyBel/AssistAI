function createLoaderForConversation() {
  const loader = document.createElement("div");
  loader.setAttribute("class", "loader_conversation");

  for (let i = 0; i <= 10; i++) {
    const circle = document.createElement("div");
    circle.setAttribute("class", "circle");
    loader.appendChild(circle);
  }

  ELEMENTS.conversationContainer.innerHTML = "";
  ELEMENTS.conversationContainer.appendChild(loader);
}

ELEMENTS.buttonSendMessage.addEventListener("click", () => {
  const message = ELEMENTS.inputMessage.value;
  createLoaderForConversation();
  sendMessageToBot(message);

  ELEMENTS.inputMessage.value = "";
  ELEMENTS.conversationContainer.scrollTo({
    top: ELEMENTS.conversationContainer.scrollHeight,
    left: 0,
    behavior: "smooth",
  });
});

ELEMENTS.buttonCleanMessage.addEventListener("click", () => {
  createLoaderForConversation();
  resetConversation();

  ELEMENTS.conversationContainer.scrollTo({
    top: ELEMENTS.conversationContainer.scrollHeight,
    left: 0,
    behavior: "smooth",
  });
});

ELEMENTS.buttonShowConversation.addEventListener("click", () =>
  store.dispatch({ type: TYPES.SHOW_CONVERSATION })
);

ELEMENTS.bodyPage.addEventListener("click", () => {
  store.dispatch({ type: TYPES.HIDDEN_CONVERSATION });
});
