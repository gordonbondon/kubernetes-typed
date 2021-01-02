# Contribution Guide

## Dev setup

Activate virtual env:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Then install the dev requirements:
```bash
pip install -r ./requirements-dev.txt
```


## Generating stubs

Stubs are generated using [`stubgen`](https://mypy.readthedocs.io/en/stable/stubgen.html)

To regenerate stubs run:
```
python ./scripts/stubgen.py
```
