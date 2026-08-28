# AGENTS.md

This file provides guidance to Claude Code, Codex, GitHub Copilot, and other coding agents
working in this repository.

## About This Project

`sweetrpg-client` (PyPI: `sweetrpg-client`, import name `sweetrpg_client`) is a JSON:API client
library used by other sweetrpg Python services to talk to the platform's REST APIs. Its type
registry (`sweetrpg_client/types/registry.py`) maps object type names to
`{endpoint_path, api_schema_class, object_class}`, backed by `sweetrpg-catalog-objects`'
schema/model classes (Volume, License, Person, Contribution, Publisher, Studio, System, Review) -
the Catalog domain, not Shelf or Library, despite the dependency having been misnamed
`sweetrpg-shelf-objects`/`sweetrpg-library-objects` for years (fixed in #103/#104).

## Committing Code

[Conventional Commits](https://www.conventionalcommits.org/): `<type>(<scope>): <description>`.

## Branches and Workflow

Git-flow (see `docs/git-flow.md` in `sweetrpg/platform`): `develop` is the integration branch,
`master` reflects the latest release. Feature/fix branches off `develop`, PR back into `develop`.

Releasing: dispatch the "Prepare Release" workflow - it computes the next version via
`git-cliff`, bumps `__version__` in `src/sweetrpg_client/__init__.py`, updates `CHANGELOG.md`,
and opens a `release/<version>` PR into `master`. Merging that PR tags the release, which
publishes to PyPI (`.github/workflows/prepare-release.yaml`/`release.yaml`/`tag-release.yaml`,
using the `sweetrpg/github-actions` reusable Python release workflow family). Previously this
repo had no real release workflow at all: a `relekang/python-semantic-release` step auto-tagged
every `develop` push directly, with no review step and no changelog - removed in favor of the
above.

## Running Checks Locally

Python 3.14, managed via [uv](https://docs.astral.sh/uv/), which is the required Python tool on
this platform (`pyproject.toml` + committed `uv.lock`; do not use `pip`/`tox`/`setup.py`
directly).

```bash
uv sync --group test   # create .venv and install deps
uv run pytest tests    # run tests
uv lock --upgrade      # update dependencies
```
