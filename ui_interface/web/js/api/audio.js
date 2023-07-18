// En el archivo de javascript
function createAudioByLastResponse() {
  eel.get_audio_from_response()(function (response) {
    // Decodes the content in base64
    const bytes = decodeBase64ToBytes(response);

    // Create the new url
    const url = createURLByBytes(bytes);

    ELEMENTS.audioVoice.src = url;
    ELEMENTS.audioVoice.addEventListener("loadedmetadata", function () {
      const duration = ELEMENTS.audioVoice.duration;

      console.log("segundos", duration);
      console.log("milisegundos", duration * 1000);

      setTimeout(
        () => ELEMENTS.canvasSphere.classList.remove("animate"),
        (duration + 0.5) * 1000
      );

      ELEMENTS.canvasSphere.classList.add("animate");
      ELEMENTS.audioVoice.play();
    });
  });
}

function createAudioByText(text) {
  ELEMENTS.containerBackendLoader.classList.add("view");
  eel.get_audio(text)(function (response) {
    // Decodes the content in base64
    const bytes = decodeBase64ToBytes(response);

    // Create the new url
    const url = createURLByBytes(bytes);

    ELEMENTS.audioVoice.src = url;
    ELEMENTS.audioVoice.addEventListener("loadedmetadata", function () {
      const duration = ELEMENTS.audioVoice.duration;

      console.log("segundos", duration);
      console.log("milisegundos", duration * 1000);

      setTimeout(
        () => ELEMENTS.canvasSphere.classList.remove("animate"),
        (duration + 0.5) * 1000
      );

      ELEMENTS.canvasSphere.classList.add("animate");
      ELEMENTS.audioVoice.play();
      ELEMENTS.containerBackendLoader.classList.remove("view");
    });
  });
}
