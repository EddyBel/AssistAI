ELEMENTS.audioVolume.addEventListener("mousemove", (evt) => {
  const volume = evt.target.value;
  store.dispatch({ type: TYPES.UPDATE_VOLUMEN_VOICE, payload: volume });
});

function updateVolumeAudio(volume) {
  if (volume < 0 || volume > 100) volume = 0.5;
  else volume = volume / 100;

  ELEMENTS.audioVoice.volume = volume;
}
