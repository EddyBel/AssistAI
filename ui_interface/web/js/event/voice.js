ELEMENTS.buttonMicrofone.addEventListener("mousedown", () =>
  voiceRecording.startRecording()
);

ELEMENTS.buttonMicrofone.addEventListener("mouseup", () =>
  voiceRecording.stopRecording()
);
