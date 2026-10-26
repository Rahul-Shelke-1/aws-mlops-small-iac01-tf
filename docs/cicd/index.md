# CI/CD Overview

## Overview

The Small MLOps Platform uses GitHub Actions to automate code quality checks, Python testing, infrastructure validation, documentation publishing, and release management.

The CI/CD strategy is designed to establish reliable validation and delivery practices before implementing the AWS infrastructure layers. Each workflow has a clearly defined responsibility, allowing changes to be validated independently and integrated through pull requests.

## Objectives

The CI/CD foundation aims to:

- Automate code quality and security checks.
- Validate Python code and tests across supported Python versions.
- Validate OpenTofu configurations before infrastructure deployment.
- Build and publish project documentation.
- Standardize release versioning and changelog generation.
- Establish a foundation for secure, controlled infrastructure delivery.

## Workflow Architecture

The CI/CD system is organized into four initial workflows.

| Workflow | Responsibility | Status |
|---|---|---|
| Python CI | Code quality, security checks, and automated tests | Implemented |
| OpenTofu CI | Infrastructure formatting, validation, linting, and security checks | Planned |
| Documentation Deployment | Documentation build validation and GitHub Pages publishing | Planned |
| Release Workflow | Automated release PRs, changelogs, and version management | Planned |
| Infrastructure CD | Controlled infrastructure planning, approval, and deployment | Future |

Workflow status should be updated as each implementation is completed and merged.

## Development and Integration Workflow

The repository follows a feature-branch workflow.

1. Create a feature branch from the latest `main`.
2. Implement a focused change.
3. Run relevant checks locally.
4. Open a pull request targeting `main`.
5. Review the changes and verify the required CI checks.
6. Merge the pull request after successful validation.

This approach keeps changes isolated, makes failures easier to diagnose, and provides a consistent review process.

## Continuous Integration

Continuous Integration (CI) validates changes before they are merged.

The initial CI capabilities include:

- Python formatting and linting.
- Static type checking.
- Python security scanning.
- Unit and integration testing.
- OpenTofu configuration validation.

Workflows are triggered by relevant repository changes and pull requests according to their configured branch and path filters.

## Continuous Delivery and Deployment

Documentation publishing and release automation are planned as separate workflows.

Infrastructure deployment will be implemented later, when the bootstrap layer and its validation strategy are ready.

The intended infrastructure delivery process will include:

- OpenTofu plan generation and review.
- Environment-specific configuration.
- Secure AWS authentication using GitHub Actions OIDC.
- Approval and protection rules for sensitive environments.
- Controlled application of infrastructure changes.

Infrastructure CD will not be enabled until the required infrastructure configuration, state management, permissions, and deployment safeguards are in place.

## Security Principles

The CI/CD implementation follows these principles:

- Use least-privilege GitHub Actions permissions.
- Avoid storing long-lived AWS credentials in repository secrets when OIDC federation is suitable.
- Keep secrets out of source code and workflow logs.
- Validate infrastructure changes before applying them.
- Require review and appropriate approvals for sensitive changes.
- Separate validation from deployment responsibilities.

## Related Documentation

- [Python CI](python-ci.md)
- [OpenTofu CI](opentofu-ci.md) — planned
- [Documentation Deployment](documentation-deployment.md) — planned
- [Release Workflow](release-workflow.md) — planned
- Infrastructure CD — documentation to be added as the deployment design matures.
