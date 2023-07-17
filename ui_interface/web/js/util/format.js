/**
 * This function takes a base64 encoded string and returns the corresponding bytes.
 * @param {string} body Bytes in base64 format
 * @returns {Uint8Array} Return decoded bytes
 */
function decodeBase64ToBytes(body) {
  const content = atob(body);

  const bytes = new Uint8Array(content.length);
  for (let i = 0; i < content.length; i++) {
    bytes[i] = content.charCodeAt(i);
  }

  return bytes;
}

/**
 * This function creates a URL based on the bytes passed by parameter and the file type.
 * @param {Uint8Array} bytes Bytes to create the file url
 * @param {string} type Type of file to be created
 * @returns {string} New Url for content
 */
function createURLByBytes(bytes, type = "audio/mp3") {
  const blob = new Blob([bytes], { type: type });
  return URL.createObjectURL(blob);
}
