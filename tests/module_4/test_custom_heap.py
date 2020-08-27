import pytest

from src.module_4.custom_heap import Heap


@pytest.mark.parametrize(
    "commands,expected",
    [
        (
            """
        Insert 200
        Insert 10
        ExtractMax
        Insert 5
        Insert 500
        ExtractMax
        """,
            [200, 500],
        ),
        (
            """
        Insert 200
        Insert 10
        Insert 5
        Insert 500
        ExtractMax
        ExtractMax
        ExtractMax
        ExtractMax
        """,
            [500, 200, 10, 5],
        ),
    ],
)
def test_initial_example(commands, expected):
    heap = Heap()
    output = []

    for command in commands.strip().split("\n"):
        command = command.strip()
        if command.startswith("Insert"):
            _, value = command.split()
            heap.insert(int(value))
        elif command.startswith("Extract"):
            output.append(heap.extract_max())
        else:
            raise ValueError(f"unknown command {command}")

    assert output == expected
