from pydantic import BaseModel, RootModel
from typing import List, Dict, Any, Optional


class Flashcard(BaseModel):
    question: str
    answers: List[str]
    audio_url: Optional[str] = None
    tags: Dict[str, Any] = {}  # e.g., {"language": "Spanish", "book": "Book1", "chapter": 2}


class FlashcardList(RootModel[List[Flashcard]]):
    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]

    def append(self, flashcard: Flashcard):
        self.root.append(flashcard)

    def to_list(self):
        return [fc.dict() for fc in self.root]

    def filter_by_tags(self, tag_values: List[Dict[str, Any]]) -> 'FlashcardList':
        filtered = self.root
        for key, value in tag_values:
            filtered = [fc for fc in filtered if fc.tags.get(key) == value]
        return FlashcardList(filtered)
