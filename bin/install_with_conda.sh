#!/bin/bash -e

read -p "Want to install conda env named 'aretfact-hackathon-03'? (y/n)" answer
if [ "$answer" = "y" ]; then
  echo "Installing conda env..."
  conda create -n aretfact-hackathon-03 python=3.10 -y
  source $(conda info --base)/etc/profile.d/conda.sh
  conda activate aretfact-hackathon-03
  echo "Installing requirements..."
  pip install -r requirements-developer.txt
  python3 -m ipykernel install --user --name=aretfact-hackathon-03
  conda install -c conda-forge --name aretfact-hackathon-03 notebook -y
  echo "Installing pre-commit..."
  make install_precommit
  echo "Installation complete!";
else
  echo "Installation of conda env aborted!";
fi
