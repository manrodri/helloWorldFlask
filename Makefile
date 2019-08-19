.PHONY: default install test

default: test

install:
	pipenv install --dev --skip-lock

test:
	python src/run_test.py test_document.py tests  

