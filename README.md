<h1 align="center">dofas</h1>
<p align="center">
A scraper for Dofus Auction house
</p>

<p align="center">
    <a href="https://github.com/astariul/dofas/releases"><img src="https://img.shields.io/github/release/astariul/dofas.svg" alt="GitHub release" /></a>
    <a href="https://github.com/astariul/dofas/actions/workflows/pytest.yaml"><img src="https://github.com/astariul/dofas/actions/workflows/pytest.yaml/badge.svg" alt="Test status" /></a>
    <a href="https://github.com/astariul/dofas/actions/workflows/lint.yaml"><img src="https://github.com/astariul/dofas/actions/workflows/lint.yaml/badge.svg" alt="Lint status" /></a>
    <img src="https://gist.githubusercontent.com/astariul/9fa9f960c5aabc529ec2cfa3e8f52553/raw/coverage.svg" alt="Coverage status" />
    <a href="https://astariul.github.io/dofas"><img src="https://img.shields.io/website?down_message=failing&label=docs&up_color=green&up_message=passing&url=https%3A%2F%2Fastariul.github.io%2Fdofas" alt="Docs" /></a>
    <br>
    <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json" alt="ruff" /></a>
    <a href="https://github.com/pre-commit/pre-commit"><img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="pre-commit"></a>
    <a href="https://github.com/astariul/dofas/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="licence" /></a>
</p>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#install">Install</a> •
  <a href="#usage">Usage</a> •
  <a href="#contribute">Contribute</a>
  <br>
  <a href="https://astariul.github.io/dofas/" target="_blank">Documentation</a>
</p>


<h2 align="center">Description</h2>

**`dofas`** stands for **Dof**us **A**uction house **S**craper.

TODO


<h2 align="center">Install</h2>

You can install it locally by first cloning the repository :

```
git clone https://github.com/astariul/dofas.git
cd dofas
pip install -e .
```

<h2 align="center">Usage</h2>

TODO


<h2 align="center">Contribute</h2>

To contribute, install the package locally, create your own branch, add your code (and tests, and documentation), and open a PR !

### Pre-commit hooks

Pre-commit hooks are set to check the code added whenever you commit something.

> [!NOTE]  
> If you never ran the hooks before, install it with :
> ```bash
> pip install -e .[hook]
> pre-commit install
> ```

Then you can just try to commit your code. If your code does not meet the quality required by linters, it will not be committed. You can just fix your code and try to commit again !

> [!TIP]
> You can manually run the pre-commit hooks with :
> ```bash
> pre-commit run --all-files
> ```

### Tests

When you contribute, you need to make sure all the unit-tests pass. You should also add tests if necessary !

> [!NOTE]  
> Install the testing dependencies with :
> ```bash
> pip install -e .[test]
> ```

You can run the tests with :

```bash
pytest
```

---

Tests are not included in the pre-commit hooks, because running the tests might be slow, and for the sake of developpers we want the pre-commit hooks to be fast !

### Documentation

The documentation should be kept up-to-date. You can visualize the documentation locally by running :

```bash
mkdocs serve
```

> [!NOTE]  
> Before running this, you need to install the documentation dependencies :
> ```bash
> pip install -e .[docs]
> ```
