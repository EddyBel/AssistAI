function resetConversation() {
  eel.initial_conversation()((response) => {
    const conversation = response.conversation;
    const message = response.response;

    store.dispatch({ type: TYPES.UPDATE_CONVERSATION, payload: conversation });
    store.dispatch({ type: TYPES.UPDATE_LAST_MESSAGE, payload: message });

    createAudioByText(message);
  });
}

function get_updated_conversation() {
  eel.get_conversation()((response) => {
    store.dispatch({ type: TYPES.UPDATE_CONVERSATION, payload: response });
  });
}

function sendMessageToBot(question) {
  eel.get_response(question)((response) => {
    const message = response.response;
    const conversation = response.conversation;

    store.dispatch({ type: TYPES.UPDATE_CONVERSATION, payload: conversation });
    store.dispatch({ type: TYPES.UPDATE_LAST_MESSAGE, payload: message });

    createAudioByText(message);
  });
}

resetConversation();
