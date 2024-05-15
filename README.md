# Assignment-Optimizer

## Overview

## Requirement
- Ubuntu 20.04 LTS
- Python 3.10

## Setup
```sh
python3 -m venv venv
. venv/bin/activate
pip3 install -e .
```

## Usage

### 1. Data Generation
```sh
cd src/data_generator
python3 main.py
```

### 2. Optimization
```sh
cd src/optimizer
python3 main.py
```

### 3. Vizualization
```sh
cd src/visualizer
python3 main.py
```