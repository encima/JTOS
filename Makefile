export PYTHONPATH=$(PWD)


.PHONY: all
all:
	build
	check
	upload

.PHONY: build
build:
	python setup.py sdist bdist_wheel

.PHONY: check
check:
	twine check dist/*

.PHONY: stop
stop:
	-rm -rf /dist

.PHONY: upload
upload:
	twine upload dist/*
