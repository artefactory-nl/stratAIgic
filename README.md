<div align="center">

# aretfact-hackathon-03

[![CI status](https://github.com/artefactory-nl/aretfact-hackathon-03/actions/workflows/ci.yaml/badge.svg)](https://github.com/artefactory-nl/aretfact-hackathon-03/actions/workflows/ci.yaml?query=branch%3Amain)
[![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue.svg)]()

[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-informational?logo=pre-commit&logoColor=white)](https://github.com/artefactory-nl/aretfact-hackathon-03/blob/main/.pre-commit-config.yaml)
</div>

Repo for team Dalai LLaMA

## Installation

To install the required packages in a virtual environment, run the following command:

```bash
make install
```

TODO: Choose between conda and venv if necessary or let the Makefile as is and copy/paste the [MORE INFO installation section](MORE_INFO.md#eased-installation) to explain how to choose between conda and venv.

A complete list of available commands can be found using the following command:

```bash
make help
```

## Usage

Launch app by using the command:

```bash
streamlit run streamlit3.py
```

In order for the LLM calls to work, you must include an OpenAI API Key in a `credentials.json` file, stored in the folder `secrets` at the root of the project.

## Repository Structure

```
.
├── .github    <- GitHub Actions workflows and PR template
├── bin        <- Bash files
├── config     <- Configuration files
├── docs       <- Documentation files (mkdocs)
├── lib        <- Python modules
├── notebooks  <- Jupyter notebooks
├── secrets    <- Secret files (ignored by git)
└── tests      <- Unit tests
```
