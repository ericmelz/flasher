import json
from pathlib import Path

import pytest
from src.models.flashcard import Flashcard
from src.data.flashcard_data import FlashcardData


@pytest.fixture
def sample_flashcards():
    return [
        {
            "question": "What is 2 + 2?",
            "answers": ["4", "four"],
            "tags": {"language": "English", "book": "Math"}
        },
        {
            "question": "What's the capital of France?",
            "answers": ["Paris"],
            "tags": {"language": "English", "book": "Geo"}
        }
    ]


def test_load_data_from_file(tmp_path, sample_flashcards):
    json_file = tmp_path / "flashcards.json"
    json_file.write_text(json.dumps(sample_flashcards), encoding="utf-8")

    db = FlashcardData(data_path=Path(json_file))
    assert len(db.get_all_flashcards().root) == 2
    assert db.get_all_flashcards()[0].question == "What is 2 + 2?"


def test_add_flashcard(tmp_path):
    json_file = tmp_path / "flashcards.json"
    db = FlashcardData(data_path=Path(json_file))
    new_fc = Flashcard(
        question="New Question?",
        answers=["A"],
        tags={"topic": "test"}
    )
    db.add_flashcard(new_fc)
    assert len(db.get_all_flashcards().root) == 1
    assert db.get_all_flashcards()[0].question == "New Question?"

    # File should now exist with new content
    loaded = json.loads(json_file.read_text())
    assert loaded[0]["question"] == "New Question?"


def test_get_random_flashcard(tmp_path, sample_flashcards):
    json_file = tmp_path / "flashcards.json"
    json_file.write_text(json.dumps(sample_flashcards), encoding="utf-8")

    db = FlashcardData(data_path=Path(json_file))
    fc = db.get_random_flashcard()

    assert FlashcardData
    assert fc.question in [item["question"] for item in sample_flashcards]
