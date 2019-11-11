import sys
from Crypto.Hash import SHA256


def main(file_path):
    blocks = extract_chunks(file_path)
    hexValue = validate_hash(blocks)
    print(hexValue)


def extract_chunks(file_path):
    blocks = []
    with open(file_path, 'rb') as file_data:
        while True:
            chunk = file_data.read(1024)
            if chunk:
                blocks.append((chunk))
            else:
                break
    return blocks


def validate_hash(blocks):
    hashes = []
    for chunk in reversed(blocks):
        h = SHA256.new()
        if blocks.index(chunk) == (len(blocks) - 1):
            h.update(chunk)
            hashes.insert(0, h.digest())
        else:
            h.update(chunk+hashes[0])
            hashes.insert(0, h.digest())
            if blocks.index(chunk) == 0:
                hexValue = h.hexdigest()
    return hexValue


if __name__ == "__main__":
    file_path = sys.argv[1]
    main(file_path)
