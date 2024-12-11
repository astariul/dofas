# Dofas

## Introduction

Welcome to the documentation of the `dofas` package.

`dofas` (**Dof**us **A**uction house **S**craper) is a scraper for Dofus Auction house.

## Installation

### Local

You can also clone the repository locally and install it manually :

```bash
git clone https://github.com/astariul/dofas.git
cd dofas
pip install -e .
```

### Extra dependencies

You can also install extras dependencies, for example :

```bash
pip install -e .[docs]
```

Will install necessary dependencies for building the docs.

!!! hint
    If you installed the package directly from github, run :
    ```bash
    pip install "dofas[docs] @ git+https://github.com/astariul/dofas.git"
    ```

---

List of extra dependencies :

* **`test`** : Dependencies for running unit-tests.
* **`hook`** : Dependencies for running pre-commit hooks.
* **`lint`** : Dependencies for running linters and formatters.
* **`docs`** : Dependencies for building the documentation.
* **`dev`** : `test` + `hook` + `lint` + `docs`.
* **`all`** : All extra dependencies.

## Contribute

To contribute, install the package locally (see [Installation](#local)), create your own branch, add your code (and tests, and documentation), and open a PR !

### Pre-commit hooks

Pre-commit hooks are set to check the code added whenever you commit something.

!!! info
    If you never ran the hooks before, install it with :
    ```bash
    pip install -e .[hook]
    pre-commit install
    ```

When you try to commit your code, hooks are automatically run, and if your code does not meet the quality required by linters, it will not be committed. You then have to fix your code and try to commit again !

!!! tip
    You can manually run the pre-commit hooks with :
    ```bash
    pre-commit run --all-files
    ```

### Unit-tests

When you contribute, you need to make sure all the unit-tests pass. You should also add tests if necessary !

!!! info
    Install the testing dependencies with :
    ```bash
    pip install -e .[test]
    ```

You can run the tests with :

```bash
pytest
```

---

!!! info
    Tests are not included in the pre-commit hooks, because running the tests might be slow, and for the sake of developpers we want the pre-commit hooks to be fast !

### Documentation

When you contribute, make sure to keep the documentation up-to-date.

You can visualize the documentation locally by running :

```bash
mkdocs serve
```

!!! info
    Before running this, you need to install the documentation dependencies :
    ```bash
    pip install -e .[docs]
    ```
