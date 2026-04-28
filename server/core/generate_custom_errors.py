from pathlib import Path
import sys
from server.core.error_codes_and_exceptions import ERRORS

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

OUTPUT_FILE = Path(__file__).with_name("custom_errors.py")


def build_file_contents() -> str:
    lines = []

    for parent_error, children_errors in ERRORS.items():
        lines.append(f"class {parent_error}(Exception):\n"
                     f"    pass\n\n")
        for error in children_errors:
            lines.append(f"class {error}({parent_error}):\n"
                         f"    pass\n\n")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    OUTPUT_FILE.write_text(build_file_contents(), encoding="utf-8")


if __name__ == "__main__":
    main()
