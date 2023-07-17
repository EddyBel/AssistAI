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
    isRotatingSphere: true,
  },
};

const store = Redux.createStore(reducer, initialState);
