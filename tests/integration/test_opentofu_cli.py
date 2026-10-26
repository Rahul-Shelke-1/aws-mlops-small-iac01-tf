import subprocess  # nosec B404


def test_opentofu_cli_is_available() -> None:
    result = subprocess.run(  # nosec B603, B607
        ["tofu", "version"],
        check=True,
        capture_output=True,
        text=True,
    )  # B603

    assert "OpenTofu" in result.stdout  # nosec B101
