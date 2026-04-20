import datetime
from pathlib import Path
import sys
from server.config.database import database_config as db_config

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

OUTPUT_FILE = Path(__file__).with_name("database_input_dict_schema.py")


def generate_type_name(table_name: str) -> str:
    return "".join(word.capitalize() for word in table_name.split("_"))


def type_to_source(value_type) -> str:
    if isinstance(value_type, tuple):
        return " | ".join(type_to_source(each_type) for each_type in value_type)
    if value_type is datetime.date:
        return "datetime.date"
    return value_type.__name__


def build_file_contents() -> str:
    lines = [
        '"""Generated from database_config.REQUIRED_DATABASE_TABLES_FIELDS."""',
        "",
        "import datetime",
        "from typing import TypedDict",
        "\n",
    ]

    for table_name, schema in db_config.REQUIRED_DATABASE_TABLES_FIELDS.items():
        lines.append(f"class {generate_type_name(table_name)}Schema(TypedDict):")
        for key, value_type in schema.items():
            lines.append(f"    {key}: {type_to_source(value_type)}")
        lines.append("\n")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    OUTPUT_FILE.write_text(build_file_contents(), encoding="utf-8")


if __name__ == "__main__":
    main()
