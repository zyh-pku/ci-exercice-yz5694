import nox


@nox.session
def tests(session):
    session.install(".[test]")
    session.run("pytest")


@nox.session
def docs(session: nox.Session) -> None:
    session.install(".[docs]")
    session.chdir("docs")
    session.run("sphinx-build", "-M", "html", ".", "build")
