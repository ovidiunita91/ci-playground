# CI Playground (Python)

A tiny Python project for learning Continuous Integration with GitHub Actions.

## Run locally
    python -m venv .venv
    .venv\Scripts\activate          # Linux/macOS: source .venv/bin/activate
    pip install -e ".[dev]"
    ruff check .
    pytest --cov=calculator

## How the pipeline works
`.github/workflows/ci.yml` runs on every push to `main` and every pull request:
checkout -> install Python (3.11, 3.12, 3.13 in parallel, pip cached) -> install deps -> ruff lint -> pytest with coverage.

## Learning path
1. Push to GitHub and watch the Actions tab go green.
2. Break a test on a branch, open a PR, see it fail.
3. Add a lint error and see ruff fail the build.
4. Enforce coverage (`--cov-fail-under=90`).
5. Add type checking (mypy) as another step or job.
6. Require the CI check to pass via branch protection.
7. Add a build/release job that only runs on `main` (or on tags).
