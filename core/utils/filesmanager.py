import base64


class FileManager:
    def __init__(self) -> None:
        pass

    def removeBytesSuffix(self, body: str):
        """This function removes the extra characters added by python when extracting bytes from a file.

        Args:
            body (str): Content bytes as string

        Returns:
            str: Content modified without the characters
        """

        if body.startswith("b'"):
            body = body[2:]

        if body.endswith("'"):
            body = body[:-1]
        return body

    def readFileBytes(self, name_file: str):
        """This function reads a file and returns the bytes of the file as a string encoded in "base64".

        Args:
            name_file (str): Name of the file to search

        Returns:
            str: Bytes as string
        """

        with open(name_file, "rb") as file:
            body = file.read()
        body = base64.b64encode(body)
        body = self.removeBytesSuffix(str(body))
        return body
