APC 524 - Homework 3

Start by creating your private repo
`https://github.com/APC524-F2024/ci-exercice-{NETID}`. Clone the present repo
and push it to your private repo.

In this repo is a basic project, with some code in `src/unc/__init__.py` and
some tests in `tests/`. The main code requires `typing_extensions` if running
on Python < 3.11, while the tests require `pytest` and `uncertainties`. The minimum
supported Python is 3.9.

Add the following files:

* `pyproject.toml`: Setup a basic project. Include at least:
    * A build backend. `hatchling` recommended, but any one should work.
    * A project table with at least name, version, requires-python, and dependencies. The only dependency is `typing_extesions; python_version<"3.11"`.
    * An project.optional-dependencies table with a `test` extra (dependencies listed above) and a `docs` extra, with `"sphinx"`, `"furo"`, and `"myst_parser"`.
* `.pre-commit-config.yaml`: Add at least the following checks:
    * Basic checks (pre-commit/pre-commit-hooks) with at least `trailing-whitespace`.
    * A formatter check (probably ruff-format)
    * Ruff with at least the default checks,  bugbear (B), isort (I),
      Ruff-specific (RUF), and PyUpgrade (UP). Use `extend-select` to ensure
      the default checks are present.
* `docs/conf.py`: The configuration file for Sphinx documentation. This should have:
    * `project`: the name of the project
    * `extensions`: This should have `myst_parser` and `sphinx.ext.autodoc`
    * `source_suffix`: This should have both `".rst"` and `".md"`
    * `html_theme`: This should be set to `"furo"`
* `noxfile.py`: Add at least the following sessions. Optionally, you can add a formatting session or anything else useful, but at least include:
    * `tests`: `nox -s tests` should run your tests. Use the `tests` extra defined above, do not list dependencies explicitly here.
    * `docs`: `nox -s docs` should build your documentation. You can have it also open a web browser if you like.
* `.github/workflow/ci.yml`: Add two jobs.
    * Format: this should run pre-commit. Manually implement, or use the pre-commit action, or nox. Doesn't matter how you do it, but it should show the diff on failure.
    * Tests: run your tests. Either through nox or by hand, but again, use the `tests` extra, don't list `pytest`, etc. Use `ubuntu-latests` and run both minimum and maximum supported Pythons (3.9 and 3.13), either with a matrix, or with nox, or both. Feel free to uv to install, either directly or through nox.
    * You do not need to build the docs in CI.

As you add these, verify it works at each step. There might be mistakes in the code that you will expose with these checks, fix them if needed and list each fix in `CHANGELOG.md`. You do not need to list automatic formatting changes, just bugfixes.

> [!tip]
>
> This is covered (including documentation setup) in the [Scientific-Python Development Guide](https://learn.scientific-python.org/development).

> [!tip]
>
> [`uv`](https://docs.astral.sh/uv) can help. Specifically, you can even get started with your `pyproject.toml` using `uv init --lib --name unc`!

