/** This javascript object will be in charge of storing all the calls to the dom of the different elements. */
const ELEMENTS = {
  // Container elements
  menuConversation: document.querySelector(".section-chat"),
  conversationContainer: document.querySelector(".chat-container-chats"),
  assistantSubtitle: document.querySelector(".context-text-subtitle"),
  informationContainer: document.querySelector(".navbar-data-container"),
  canvasSphere: document.querySelector(".canvas-sphere"),
  bodyPage: document.querySelector(".content"),
  containerBackendLoader: document.querySelector(".backend_load_indicators"),

  // Inputs and Buttons
  buttonMicrofone: document.getElementById("button_microfone"),
  buttonSendMessage: document.getElementById("button_send_message"),
  buttonCleanMessage: document.getElementById("button_clean_conversation"),
  buttonShowConversation: document.querySelector(".navbar-button-menu"),
  inputMessage: document.getElementById("input_from_message"),
  inputAnimationSphere: document.getElementById("checkboxAnimationSphere"),

  // Audio controls
  audioVoice: document.getElementById("audio-voice-response"),
  audioVolume: document.getElementById("volume-voice"),
  audioEffectRecordingVoiceStart: document.getElementById(
    "effect_voice_recording_start"
  ),
  audioEffectRecordingVoiceEnd: document.getElementById(
    "effect_voice_recording_end"
  ),
};
