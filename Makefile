.DEFAULT_GOAL := check

.PHONY: format lint check test all

format:
	uv run ruff check --fix .
	uv run ruff format .

lint:
	uv run ruff check .

check:
	uv run ruff check .
	uv run ruff format --check .

test:
	uv run python -m pytest

all:
	$(MAKE) format
	$(MAKE) check
	$(MAKE) test
