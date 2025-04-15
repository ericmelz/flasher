import pytest
from models.flashcard import Flashcard, FlashcardList


@pytest.fixture
def sample_flashcards():
    return FlashcardList(__root__=[
        Flashcard(
            question="What is 2 + 3?",
            answers=["5", "five", "cinco"],
            tags={"language": "English", "book": "Math 101", "chapter": 1}
        ),
        Flashcard(
            question="¿Cómo se dice 'hello' en español?",
            answers=["hola"],
            tags={"language": "Spanish", "book": "SpanishBasics", "chapter": 1}
        ),
        Flashcard(
            question="What's the capital of France?",
            answers=["Paris"],
            tags={"language": "English", "book": "Geography", "chapter": 2}
        )
    ])


def test_flashcard_creation():
    fc = Flashcard(question="Test?", answers=["yes"], tags={"topic": "test"})
    assert fc.question == "Test?"
    assert fc.answers == ["yes"]
    assert fc.tags["topic"] == "test"
