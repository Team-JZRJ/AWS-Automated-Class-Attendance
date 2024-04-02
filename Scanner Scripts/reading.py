import nfc
import sys
import nfc.tag


def on_connect(tag):
    print(f"Tag detected: {tag}")
    return tag


def read_nfc():
    clf = nfc.ContactlessFrontend("usb")  # Assuming NFC reader is connected via USB
    if clf:
        print("NFC reader detected and ready for a tag.")
        try:
            return clf.connect(rdwr={"on-connect": on_connect})
        finally:
            clf.close()
    else:
        print("Unable to initialize the NFC reader.")
        sys.exit(1)


if __name__ == "__main__":
    read_nfc()
