import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wicked_python-hotness",
    version="0.0.1",
    author="Graham Williasmon",
    author_email="author@example.com",
    description="A wicked new package that is the new hotness",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/00willo/circleci-tox-pyenv-sandbox",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
