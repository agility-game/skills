from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ROOT / "tests" / "required-files.txt"


def test_required_files_exist():
    missing = []
    for line in REQUIRED.read_text().splitlines():
        if line.strip() and not (ROOT / line.strip()).exists():
            missing.append(line.strip())
    assert not missing, f"Missing required files: {missing}"


def test_skill_file_contains_skill_name():
    content = (ROOT / "SKILL.md").read_text()
    assert "code-smell-detective" in content
    assert "Code Smell Detective" in content
