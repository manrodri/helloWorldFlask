.PHONY: default install test

default: test

install:
	pip3 install -r requirements.txt

test:
	python run_test.py

