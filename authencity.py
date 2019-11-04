#!/usr/bin/python
# -*- coding: utf-8 -*-

from Crypto.Hash import SHA256

h = SHA256.new()
file = "./vídeos/video_03.mp4"
blocks = []
hashes = []


with open(file, 'rb') as f:
    while True:
        chunk = f.read(1024)
        if chunk:
            blocks.append((chunk))
        else:
            numBlocks = len(blocks)
            break

for chunk in reversed(blocks):
    if blocks.index(chunk) == (numBlocks - 1):
        h = SHA256.new()
        h.update(chunk)
        hashes.insert(0, h.digest())
    else:
        h = SHA256.new()
        h.update(chunk+hashes[0])
        hashes.insert(0, h.digest())
        if blocks.index(chunk) == 0:
            hexValue = h.hexdigest()

print(hexValue)
