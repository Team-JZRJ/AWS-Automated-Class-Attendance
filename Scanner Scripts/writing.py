import nfc


def write_text_to_nfc(text):
    with nfc.ContactlessFrontend("usb") as clf:
        print("Place the NFC tag close to the reader.")
        # Try to sense different types of tags with a longer timeout
        target = clf.sense(
            timeout=500, technologies=["iso14443a", "iso14443b", "iso15693"]
        )
        if target is None:
            print(
                "No NFC tag detected. Ensure the tag is near the reader and try again."
            )
            return

        tag = nfc.tag.activate(clf, target)
        if not tag.ndef:
            print("NFC tag is not NDEF formatted or not writable.")
            return

        message = nfc.ndef.Message(nfc.ndef.TextRecord(text))
        try:
            tag.ndef.message = message
            print("Text written to NFC tag successfully.")
        except Exception as e:
            print(f"Failed to write to NFC tag: {e}")


if __name__ == "__main__":
    text_input = input("Enter the text to write to the NFC card: ")
    write_text_to_nfc(text_input)
