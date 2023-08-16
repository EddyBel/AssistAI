// Event that controls the formation of the sphere

ELEMENTS.inputAnimationSphere.addEventListener("click", () => {
  const state = ELEMENTS.inputAnimationSphere.checked;

  if (state) store.dispatch({ type: TYPES.ACTIVATE_ROTATION });
  else store.dispatch({ type: TYPES.DEACTIVATE_ROTATION });
});

function sphereRotationActivateAndDeactivate(stateRotation) {
  if (stateRotation) {
    sphere.cancelAnimation();
    sphere.rotateSphere();
  } else {
    sphere.cancelAnimation();
  }
}
