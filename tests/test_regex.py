from mkdocs_caseinsensitive_plugin.plugin import CaseInsensitiveFiles
import pathlib
import re

pattern = CaseInsensitiveFiles.pattern


def open_file(name: str) -> str:
    return pathlib.Path(__file__).parent.joinpath(name).read_text()


def test_regex():
    sample_markdown = open_file("sample.md")
    found = re.findall(pattern, sample_markdown)
    assert len(found) == 1
    assert found[0] == ("text", "./file.md")
