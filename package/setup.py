import os
from glob import glob
from setuptools import setup

setup(
    name="oop-book",
    version="1.3.2",
    description="Style and Imports for oop Book",
    author="Brandon Smith",
    author_email="brandon.smith@deakin.edu.au",
    url="https://dmol.pub",
    license="MIT",
    packages=["dmol"],
    install_requires=[
        "jupyter-book==0.13.1",
        "lxml_html_clean"
    ],
    test_suite="tests",
    long_description="""

""",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
