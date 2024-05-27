# Student guide for Object-Oriented Development

&copy; Brandon Smith

## Build Book Locally

To build the book locally you need to install [Jupyter Book](https://jupyterbook.org/en/stable/intro.html):

```bash
python -m pip install -U jupyter-book
# conda install -c conda-forge jupyter-book
```

With [Jupyter Book](https://jupyterbook.org/en/stable/intro.html) installed you can build the book locally as follows:

```bash
# From the root directory of the repository
jupyter-book build .
```

The HTML of the book are located in the `_build/html` directory. Open the `index.html` file to land on the home page of the book.

## Developing

This repo uses pre-commit, so after cloning run `pip install -r dev-requirements.txt` and `pre-commit install` prior to committing.
If you have already committed, but your PR is failing because of a pre-commit error, run `pre-commit run --all`
