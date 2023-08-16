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
 * This function takes an array of bytes and returns the corresponding base64 decoded string.
 * @param {Uint8Array} bytes Bytes to be encoded
 * @returns {string} Return decoded base64 string
 */
function encodeBytesToBase64(bytes) {
  let content = "";
  for (let i = 0; i < bytes.length; i++) {
    content += String.fromCharCode(bytes[i]);
  }
  return btoa(content);
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
