const initialState = {
  conversation: {
    conversation: [],
    lastResponse: "",
  },
  information: {},
  configuration: {
    voiceVolume: 50,
  },
  DOM: {
    isRotatingSphere: false,
    isShowConversations: false,
    isShowConfigurations: false,
  },
};

const store = Redux.createStore(reducer, initialState);
