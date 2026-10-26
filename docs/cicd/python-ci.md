# Python CI

## Overview

Python CI automates code quality checks, security scanning, and automated testing for the Small MLOps Platform.

The workflow is implemented using GitHub Actions and uses `uv` for Python installation and dependency management.

**Workflow file:** `.github/workflows/python-ci.yml`

## Objectives

- Enforce consistent Python code formatting.
- Detect common code-quality issues.
- Perform static type checking.
- Scan Python code for common security issues.
- Execute unit and integration tests.
- Validate compatibility across supported Python versions.

## Workflow Triggers

The workflow supports the following triggers:

| Trigger | Behavior |
|---|---|
| Push to `main` | Runs when configured path filters match |
| Push to `feat/**` | Runs when configured path filters match |
| Push to `fix/**` | Runs when configured path filters match |
| Pull request targeting `main` | Runs when configured path filters match |
| Manual dispatch | Allows manual execution |

The workflow uses path filters to avoid running for changes unrelated to Python CI.

The configured paths are:

- `tests/**`
- `pyproject.toml`
- `uv.lock`
- `.pre-commit-config.yaml`
- `.github/workflows/python-ci.yml`

These paths must remain synchronized with the actual workflow configuration.

## Code Quality and Security

The quality job runs on Ubuntu using Python 3.11.

### Formatting

Ruff checks whether Python files follow the configured formatting rules.

```bash
uv run ruff format --check .
```

The check reports formatting differences without modifying files.

### Linting

Ruff detects common programming errors and code-quality issues.

```bash
uv run ruff check .
```

### Static Type Checking

mypy checks type annotations and reports potential type inconsistencies.

```bash
uv run mypy tests/
```

### Security Scanning

Bandit scans Python code for common security issues.

```bash
uv run bandit -r tests/
```

These commands target the test directory. Tool rules and exclusions can be managed through the project's configuration where applicable.

## Automated Testing

The test job runs after the quality job succeeds.

### Python Version Matrix

Tests execute against the supported Python versions:

- Python 3.11
- Python 3.12
- Python 3.13

The matrix helps identify compatibility issues across supported interpreter versions.

### Unit Tests

Unit tests validate individual functions, classes, and components.

**Test directory:** `tests/unit/`

```bash
uv run pytest tests/unit
```

### Integration Tests

Integration tests validate interactions between components and their dependencies.

**Test directory:** `tests/integration/`

```bash
uv run pytest tests/integration
```

Integration tests that require external services or cloud resources must use explicitly configured test fixtures, local services, or dedicated test environments.

## Dependency Management

The workflow uses `uv` to install Python and synchronize project dependencies.

The following files define the project's dependency configuration:

- `pyproject.toml`
- `uv.lock`

Development dependencies must include the tools required by the workflow, including Ruff, mypy, Bandit, and pytest.

The lockfile should be committed and kept synchronized with dependency changes.

## Local Validation

Before opening a pull request, run the relevant checks locally.

```bash
uv run ruff format --check tests/
uv run ruff check tests/
uv run mypy tests/
uv run bandit -r tests/
uv run pytest tests/unit
uv run pytest tests/integration
```

To correct formatting issues locally, run:

```bash
uv run ruff format tests/
```

Resolve reported issues before pushing changes.

## Failure Handling

If a workflow fails:

1. Open the failed GitHub Actions run.
2. Identify the failed job and step.
3. Reproduce the failure locally when possible.
4. Correct the underlying issue.
5. Run the relevant checks again.
6. Push the fix and verify the updated workflow run.

Pull requests should be merged only after the required checks pass and the changes have been reviewed.

## Future Improvements

Potential extensions to Python CI include:

- Uploading test results and coverage reports.
- Enforcing a minimum test coverage threshold.
- Publishing machine-readable test reports.
- Adding dependency vulnerability scanning.
- Integrating CI checks with branch protection rules.

These improvements should be introduced when they provide clear value to the project.
