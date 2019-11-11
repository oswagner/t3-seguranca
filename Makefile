.PHONY: .run .install

run:
	python3 hash_validation.py ./data/video05.mp4

install:
	pip3 install -r requirements.txt
