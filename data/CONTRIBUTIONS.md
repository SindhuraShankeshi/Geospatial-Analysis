# Contributing

Thanks for your interest in contributing! This file explains how to contribute in a way that keeps the repository organized and easy to review.

## Where to start
- Look at open issues or open a new issue to discuss new features or bugs.
- If you'd like to add a dataset or update a notebook, open an issue first to avoid duplicated effort.

## Branching & commits
- Create a descriptive branch from `main` (or `master`) for your work:
  - feature/add-sample-data
  - fix/sf-crime-notebook
- Keep commits small and focused. Use clear commit messages, e.g.:
  - "Add scripts/generate_maps.py to reproduce example maps"
  - "Fix: detect latitude/longitude columns in SF script"

## Code style & format
- Use Python 3.8+ syntax.
- Follow common Python style (PEP8). We recommend running black or flake8 if you add more script files.
- Keep notebooks runnable and avoid committing very large raw data files.

## Notebooks and scripts
- Notebooks live in `notebooks/` and should be runnable end-to-end. If a notebook depends on a dataset, indicate how to download or provide a small sample in `data/sample/`.
- Scripts that reproduce notebook results (like `scripts/generate_maps.py`) should be idempotent and accept file paths as arguments.

## Data handling
- Do NOT commit large raw data or sensitive data. Add download instructions or scripts that fetch the data into `data/`.
- Add a small sample dataset (a few rows) under `data/sample/` if you want others to run the notebooks quickly.

## Running tests / checks
- There are no automated tests yet. If you add functionality, please include tests or a simple checklist in your PR description explaining how reviewers can validate the change.

## Pull requests
- Open a PR from your branch to `main`.
- Include a summary of changes, why they are needed, and any manual steps to validate.
- If your PR changes data processing or visualization results, include sample output images in `images/` (small PNGs) or link to generated HTML in a GitHub Pages preview.

## License & copyright
- Ensure any added datasets have compatible licensing and include attribution in the `README.md` or a new `DATA_LICENSES.md`.

## Review checklist (for PRs)
- [ ] Branch created from main
- [ ] Description explains the why
- [ ] Notebooks/scripts run end-to-end with provided instructions
- [ ] No large binary data committed
- [ ] Appropriate attribution for external data sources

## Contact / help
If you need help or want to discuss a larger change, open an issue and tag @SindhuraShankeshi (or leave a comment on this repo). Thank you!
