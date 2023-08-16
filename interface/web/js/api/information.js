eel.get_info_model()((response) => {
  store.dispatch({ type: TYPES.UPDATE_INFORMATION, payload: response });
});
