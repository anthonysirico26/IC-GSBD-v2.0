.PHONY: lint test train pipeline

lint:
	ruff check src/

test:
	pytest src/tests/

train:
	dvc repro train

pipeline: lint test train