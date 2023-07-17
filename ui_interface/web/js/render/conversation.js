function renderOfChats(conversation) {
  ELEMENTS.conversationContainer.innerHTML = "";

  conversation.map((message) => {
    const role = message.role;
    const body = message.content;

    const bubbleBox = document.createElement("div");
    bubbleBox.setAttribute("class", `chat-bubble ${role}`);

    const bubbleRole = document.createElement("p");
    bubbleRole.setAttribute("class", "bubble-role");
    bubbleRole.innerHTML = role;

    const bubbleText = document.createElement("p");
    bubbleText.innerHTML = body;

    bubbleBox.appendChild(bubbleRole);
    bubbleBox.appendChild(bubbleText);
    ELEMENTS.conversationContainer.appendChild(bubbleBox);
  });
}

function renderSubtitle(message) {
  ELEMENTS.assistantSubtitle.innerHTML = message;
}
