from mkdocs_caseinsensitive_plugin.plugin import CaseInsensitiveFiles
import pathlib
import regex as re

pattern = CaseInsensitiveFiles.pattern


def open_file(name: str) -> str:
    return pathlib.Path(__file__).parent.joinpath("files", name).read_text()


def test_regex_basic():
    sample_markdown = open_file("test_regex_basic.md")
    found = re.findall(pattern, sample_markdown)
    assert len(found) == 1
    assert found[0][0] == "text"
    assert found[0][-1] == "./file.md"


def test_recursive_basic():
    sample_markdown = open_file("test_regex_recursive.md")
    found = re.findall(pattern, sample_markdown)
    assert len(found) == 1
    assert found[0][0] == "recursive text"
    assert found[0][-1] == "./recursive(recursive_link(wow)).md"
