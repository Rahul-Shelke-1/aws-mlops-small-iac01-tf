# Getting Started

This guide explains how to configure the local development environment for the AWS Small MLOps Platform.

## Prerequisites

Install the following tools:

- Git
- Python version supported by `pyproject.toml`
- [uv](https://docs.astral.sh/uv/)
- [OpenTofu CLI](https://opentofu.org/docs/intro/install/)
- [pre-commit](https://pre-commit.com/) — installed through the project environment

Verify the installations:

```bash
python --version
uv --version
tofu version
git --version
```

## Clone the Repository

```bash
git clone https://github.com/Rahul-Shelke-1/aws-mlops-small-iac01-tf.git
cd aws-mlops-small-iac01-tf
```

## Set Up the Python Environment

Install the project dependencies and create the virtual environment:

```bash
uv sync
```

This installs dependencies declared in `pyproject.toml` and uses `uv.lock` to reproduce the resolved environment.

If development dependencies are configured in a separate dependency group, install them using the appropriate command, such as:

```bash
uv sync --group dev
```

Activate the environment if you prefer working inside it interactively:

```bash
source .venv/bin/activate
```

Alternatively, execute project commands using `uv run` without activating the environment.

Verify the development tools:

```bash
uv run pre-commit --version
uv run pytest --version
```

## Configure Pre-commit

Install the repository's Git hooks:

```bash
uv run pre-commit install
```

Run all configured hooks against the repository:

```bash
uv run pre-commit run --all-files
```

Resolve any reported issues before committing changes.

If secret detection is configured to use `.secrets.baseline`, initialize the baseline when it does not already exist:

```bash
uv run detect-secrets scan > .secrets.baseline
```

Review the baseline carefully before committing it. Never treat actual credentials as acceptable findings.

## OpenTofu Development

OpenTofu is used to manage the platform's infrastructure as code.

Verify the installation:

```bash
tofu version
```

Format OpenTofu configuration files:

```bash
tofu fmt -recursive
```

Check formatting without modifying files:

```bash
tofu fmt -check -recursive
```

Before validating a particular infrastructure root module, change into its directory and initialize it:

```bash
cd path/to/infrastructure/root
tofu init
tofu validate
```

Replace the example directory with the actual infrastructure root module.

Run `tofu plan` only when you are ready to evaluate the proposed infrastructure changes. AWS credentials and appropriate permissions may be required, depending on the providers and data sources configured.

Do not run `tofu apply` against a shared or production environment without following the project's deployment and approval procedures.

## Run Tests

The project uses pytest for Python tests and OpenTofu for infrastructure management.

### Run the Complete Test Suite

```bash
uv run pytest
```

### Run Unit Tests

```bash
uv run pytest tests/unit/
```

Unit tests should validate Python logic and project configuration without provisioning infrastructure.

### Run Integration Tests

```bash
uv run pytest tests/integration/
```

The initial integration test verifies that the OpenTofu CLI is installed and executable.

Future integration tests may validate Terraform-compatible infrastructure configurations using `tftest` or OpenTofu's native testing capabilities.

### Run OpenTofu Formatting Checks

```bash
tofu fmt -check -recursive
```

### Run Pre-commit Checks

```bash
uv run pre-commit run --all-files
```

Integration tests that interact with AWS or provision infrastructure may require credentials, permissions, initialized modules, and isolated test resources. Do not run infrastructure tests against production environments without explicit safeguards.

## Development Workflow

1. Create a focused feature or chore branch.
2. Implement the change and add relevant tests.
3. Run pre-commit hooks and the applicable test suite locally.
4. Commit changes using Conventional Commits.
5. Open a pull request and ensure the required checks pass.
6. Merge the pull request after review and required checks succeed.

## Next Steps

Future development will introduce OpenTofu CI, Python-based infrastructure testing, documentation preview and deployment, and automated releases.
