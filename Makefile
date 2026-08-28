.PHONY: init test coverage docs

init:
	uv sync --group test --group docs

test:
	uv run pytest tests

coverage:
	uv run coverage run -m pytest tests
	uv run coverage report -m

docs:
	cd docs && uv run --group docs make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"
