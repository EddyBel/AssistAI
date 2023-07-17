/** This javascript object will be in charge of storing all the calls to the dom of the different elements. */
const ELEMENTS = {
  // Container elements
  conversationContainer: document.querySelector(".chat-container-chats"),
  assistantSubtitle: document.querySelector(".context-text-subtitle"),
  informationContainer: document.querySelector(".navbar-data-container"),
  canvasSphere: document.querySelector(".canvas-sphere"),

  // Inputs and Buttons
  buttonSendMessage: document.getElementById("button_send_message"),
  buttonCleanMessage: document.getElementById("button_clean_conversation"),
  inputMessage: document.getElementById("input_from_message"),
  inputAnimationSphere: document.getElementById("checkboxAnimationSphere"),
  audioVoice: document.getElementById("audio-voice-response"),
  audioVolume: document.getElementById("volume-voice"),
};
