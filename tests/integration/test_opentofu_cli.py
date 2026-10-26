import subprocess


def test_opentofu_cli_is_available() -> None:
    result = subprocess.run(
        ["tofu", "version"],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "OpenTofu" in result.stdout
