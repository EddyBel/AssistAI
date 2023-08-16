/**
 * This function allows to render the most essential information bubbles of the program configuration in the dom.
 * @param {Object} information Object containing the data to be rendered as bubbles in the navbar.
 */
function renderOfInformationBubbles(information) {
  ELEMENTS.informationContainer.innerHTML = "";

  Object.keys(information).map((key) => {
    const box = document.createElement("div");
    box.setAttribute("class", "navbar-data");

    const text = document.createElement("p");
    text.innerHTML = information[key];

    box.appendChild(text);
    ELEMENTS.informationContainer.appendChild(box);
  });
}
