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

## Testing

Run tests with `tox`:
```
tox -epy312
```

## Updating kubernetes-client version

1. Update `DEFAULT_BRANCH` in [`scripts/stubgen.py`](./scripts/stubgen.py)
2. Update [`requirements-test.txt`](./requirements-test.txt) version pin and `pip install` it.
3. Regenerate stubs and model dicts

## Generating stubs

Stubs are generated using [`stubgen`](https://mypy.readthedocs.io/en/stable/stubgen.html)

To regenerate stubs run:
```
python ./scripts/stubgen.py
```

## Generating model dicts

Do this:
```
python ./scripts/typeddictgen.py
```
