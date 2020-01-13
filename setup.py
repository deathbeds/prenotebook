import json
from pathlib import Path
import setuptools

name = "prenotebook"

__version__ = "0.1.0"

setup_args = dict(
    name=name,
    version="0.1.0",
    author="deathbeds",
    packages=setuptools.find_packages(),
    install_requires="importnb black isort nbconvert pydantic IPython".split(),
    author_email="tony.fast@gmail.com",
    description="Import Jupyter (ne IPython) notebooks into tests and scripts.",
)

if __name__ == "__main__":
    setuptools.setup(**setup_args)
