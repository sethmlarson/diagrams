import os
from pathlib import Path

import nox

BASE_DIR = Path(__file__).parent.absolute()
DIAGRAMS_DIR = BASE_DIR / "diagrams"
TOOLS_DIR = BASE_DIR / "tools"

PYTHON_CODE = (
    str(TOOLS_DIR),
    "noxfile.py",
)


@nox.session
def format(session):
    session.install("black", "isort")
    session.run("isort", "--profile=black", *PYTHON_CODE)
    session.run("black", *PYTHON_CODE)

    svg_formatter = str(TOOLS_DIR / "svg-formatter.py")
    for root, _, filenames in os.walk(DIAGRAMS_DIR):
        for filename in sorted(filenames):
            if not filename.endswith(".svg"):
                continue
            session.run("python", svg_formatter, os.path.join(root, filename))
