function reducer(state, action) {
  const type = action.type;
  const payload = action.payload;

  switch (type) {
    case TYPES.ACTIVATE_ROTATION:
      return {
        ...state,
        DOM: {
          ...state.DOM,
          isRotatingSphere: true,
        },
      };

    case TYPES.DEACTIVATE_ROTATION:
      return {
        ...state,
        DOM: {
          ...state.DOM,
          isRotatingSphere: false,
        },
      };

    case TYPES.UPDATE_CONVERSATION:
      return {
        ...state,
        conversation: {
          ...state.conversation,
          conversation: payload,
        },
      };

    case TYPES.UPDATE_LAST_MESSAGE:
      return {
        ...state,
        conversation: {
          ...state.conversation,
          lastResponse: payload,
        },
      };

    case TYPES.UPDATE_INFORMATION:
      return {
        ...state,
        information: payload,
      };

    case TYPES.UPDATE_VOLUMEN_VOICE:
      return {
        ...state,
        configuration: {
          ...state.configuration,
          voiceVolume: payload,
        },
      };

    case TYPES.SHOW_CONVERSATION:
      return {
        ...state,
        DOM: {
          ...state.DOM,
          isShowConversations: true,
        },
      };

    case TYPES.HIDDEN_CONVERSATION:
      return {
        ...state,
        DOM: {
          ...state.DOM,
          isShowConversations: false,
        },
      };

    default:
      return state;
  }
}
