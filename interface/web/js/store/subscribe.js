const prevState = { ...initialState };

store.subscribe(() => {
  const state = store.getState();

  if (prevState != state) {
    console.log("State: ", state);
  }

  if (prevState.conversation.conversation != state.conversation.conversation) {
    renderOfChats(state.conversation.conversation);
    prevState.conversation.conversation = state.conversation.conversation;
  }

  if (prevState.conversation.lastResponse != state.conversation.lastResponse) {
    renderSubtitleWithEffect(state.conversation.lastResponse);
    prevState.conversation.lastResponse = state.conversation.lastResponse;
  }

  if (prevState.information != state.information) {
    renderOfInformationBubbles(state.information);
    prevState.information = state.information;
  }

  sphereRotationActivateAndDeactivate(state.DOM.isRotatingSphere);
  // if (prevState.DOM.isRotatingSphere != state.DOM.isRotatingSphere) {
  //   sphereRotationActivateAndDeactivate(state.DOM.isRotatingSphere);
  //   prevState.DOM.isRotatingSphere = state.DOM.isRotatingSphere;
  // }

  if (prevState.configuration.voiceVolume != state.configuration.voiceVolume) {
    updateVolumeAudio(state.configuration.voiceVolume);
    prevState.configuration.voiceVolume = state.configuration.voiceVolume;
  }

  if (prevState.DOM.isShowConversations != state.DOM.isShowConversations) {
    hiddenAndWatchConversationsMenu(state.DOM.isShowConversations);
    prevState.DOM.isShowConversations = state.DOM.isShowConversations;
  }
});
