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
    install_requires=Path("requirements.txt").read_text().split(),
    author_email="tony.fast@gmail.com",
    description="Pre commit hooks for jupyter notebooks.",
    entry_points={"console_scripts": ["prenotebook=prenotebook:main"],},
)

if __name__ == "__main__":
    setuptools.setup(**setup_args)
