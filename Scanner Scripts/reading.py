import nfc
import sys
import nfc.tag


def on_connect(tag):
    print(f"Tag detected: {tag}")
    # Attempt to read NDEF data
    print(tag.ndef)
    if tag.ndef:
        for record in tag.ndef.records:
            print(record.text)
            # Check if the record is a Text Record
            if record.type == "urn:nfc:wkt:T":
                text = record.text
                print(f"Text record found: {text}")
            else:
                print(f"Non-text record found, type: {record.type}")
    else:
        print("This tag is not NDEF formatted.")
    return True


def read_nfc():
    clf = nfc.ContactlessFrontend("usb")  # Assuming NFC reader is connected via USB
    if clf:
        print("NFC reader detected and ready for a tag.")
        try:
            clf.connect(rdwr={"on-connect": on_connect})
        finally:
            clf.close()
    else:
        print("Unable to initialize the NFC reader.")
        sys.exit(1)


if __name__ == "__main__":
    read_nfc()
