import json
import random
from pathlib import Path
from models.flashcard import Flashcard, FlashcardList


class FlashcardData:
    def __init__(self, data_path: Path = Path(__file__).parent.parent.parent / "data" / "flashcards.json"):
        self.data_path = data_path
        self.flashcards = self._load_data()

    def _load_data(self) -> FlashcardList:
        if not self.data_path.exists():
            return FlashcardList([])
        with self.data_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return FlashcardList([Flashcard(**fc) for fc in data])

    def _save_data(self):
        with self.data_path.open("w", encoding="utf-8") as f:
            json.dump(self.flashcards.to_list(), f, indent=2)

    def get_random_flashcard(self, tags=None) -> Flashcard:
        if tags is None:
            tags = {}
        return random.choice(self.flashcards.filter_by_tags(tags))

    def get_all_flashcards(self) -> FlashcardList:
        return self.flashcards

    def add_flashcard(self, flashcard: Flashcard):
        self.flashcards.append(flashcard)
        self._save_data()
