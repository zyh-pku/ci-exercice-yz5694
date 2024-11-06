import nox

@nox.session
def tests(session):
    session.install(".[test]")
    session.run("pytest")

@nox.session
def docs(session):
    session.install(".[docs]")
    session.run("sphinx-build", "docs", "docs/_build")
