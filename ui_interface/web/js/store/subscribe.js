store.subscribe(() => {
  const state = store.getState();
  console.log("subscribe", state);

  // Render conversations and subtitles of the elements
  renderOfChats(state.conversation.conversation);
  renderSubtitle(state.conversation.lastResponse);
  renderOfInformationBubbles(state.information);

  sphereRotationActivateAndDeactivate(state.DOM.isRotatingSphere);
  updateVolumeAudio(state.configuration.voiceVolume);
});
