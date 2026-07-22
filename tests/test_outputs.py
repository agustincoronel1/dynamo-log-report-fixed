import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def load_report() -> dict:
    assert REPORT_PATH.is_file(), "/app/report.json was not created"

    try:
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError("/app/report.json is not valid JSON") from exc

    assert isinstance(report, dict), "The report must be a JSON object"
    return report


def test_report_structure():
    """Success criterion 1: the report is valid JSON with exactly the required fields."""
    report = load_report()

    assert set(report.keys()) == {
        "total_requests",
        "unique_ips",
        "top_path",
    }


def test_total_requests():
    """Success criterion 2: total_requests matches the number of non-empty log entries."""
    report = load_report()

    assert report["total_requests"] == 6


def test_unique_ips():
    """Success criterion 3: unique_ips matches the number of distinct client IPs."""
    report = load_report()

    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion 4: top_path is the most frequently requested path."""
    report = load_report()

    assert report["top_path"] == "/index.html"