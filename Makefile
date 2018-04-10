
test:
	pytest

dist:
	python setup.py sdist bdist_wheel upload

.PHONY: test dist