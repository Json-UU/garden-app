# Garden App

A small Python gardening advice app for the M07T02 Git Workflows practical.
It uses only the Python standard library; no installation or packages are needed.

## Run

```console
python garden_advice.py
```

Enter your local season (`spring`, `summer`, `autumn`, `winter`) and plant type
(`flower`, `vegetable`). Capitalisation and surrounding spaces are ignored.
Unsupported choices prompt again. Ctrl+C or end-of-input cancels the session.

For example, `winter` and `vegetable` produce:

```text
Protect your plants from frost with covers.
Keep an eye out for pests!
```

The program asks for the season directly, so it does not assume your hemisphere
or infer seasons from the current month. Advice is general and should be adapted
to local conditions and the particular plant.

## Code

- `SEASON_ADVICE` and `PLANT_ADVICE` store the supported choices and advice.
- `read_choice()` handles prompts and retries.
- `get_advice()` returns advice without printing or asking for input.
- `main()` connects input and output; the main guard keeps imports non-interactive.

## Check

```console
python -m unittest -v
```

Checks cover all eight season/plant combinations, normalisation, unsupported
choices, CLI retries, importing without prompts, and cancelled input.

## Git workflow

The supplied Python starter was uploaded first and then cloned locally.
Two separate feature branches and pull requests implement the improvements:

- [Issue #1](https://github.com/Json-UU/garden-app/issues/1): interactive input.
- [Issue #2](https://github.com/Json-UU/garden-app/issues/2): documented functions,
  dictionary-based advice and all four seasons.

Each pull request is checked and self-reviewed before merging into `main`.
The original starter remains available in Git history.
