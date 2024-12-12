import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


reqs = ["opencv-python~=4.10", "easyocr~=1.7"]

extras_require = {
    "test": ["pytest~=8.0", "pytest-cov~=6.0"],
    "hook": ["pre-commit~=4.0"],
    "lint": ["ruff~=0.2"],
    "docs": ["mkdocs-material~=9.0", "mkdocstrings[python]~=0.24", "mike~=2.0"],
}
extras_require["all"] = sum(extras_require.values(), [])
extras_require["dev"] = (
    extras_require["test"] + extras_require["hook"] + extras_require["lint"] + extras_require["docs"]
)

setuptools.setup(
    name="dofas",
    version="1.0.0.dev0",
    author="Nicolas REMOND",
    author_email="remondnicola@gmail.com",
    description="A scraper for Dofus Auction house",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/astariul/dofas",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    install_requires=reqs,
    extras_require=extras_require,
    entry_points={
        "console_scripts": [
            "dofas=dofas.cmd:cli",
        ],
    },
)
