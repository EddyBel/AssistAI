ELEMENTS.buttonSendMessage.addEventListener("click", () => {
  const message = ELEMENTS.inputMessage.value;
  sendMessageToBot(message);

  ELEMENTS.inputMessage.value = "";
  ELEMENTS.conversationContainer.scrollTo({
    top: ELEMENTS.conversationContainer.scrollHeight,
    left: 0,
    behavior: "smooth",
  });
});

ELEMENTS.buttonCleanMessage.addEventListener("click", () => {
  resetConversation();

  ELEMENTS.conversationContainer.scrollTo({
    top: ELEMENTS.conversationContainer.scrollHeight,
    left: 0,
    behavior: "smooth",
  });
});
