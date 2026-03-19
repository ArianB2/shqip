from fastapi import APIRouter, Query
from typing import Literal

router = APIRouter()

# ---------------------------------------------------------------------------
# Month 1: hardcoded mock data so the frontend has something real to display.
# Month 2: replace these with actual database queries via SQLAlchemy + RDS.
# ---------------------------------------------------------------------------

MOCK_LESSONS = [
    {
        "id": 1,
        "title": "Greetings",
        "title_sq": "Përshëndetje",
        "description": "Learn how to say hello and goodbye in Albanian",
        "level": "beginner",
        "available_dialects": ["gheg", "tosk"],
        "word_count": 8,
    },
    {
        "id": 2,
        "title": "Numbers 1–10",
        "title_sq": "Numrat 1–10",
        "description": "Count from one to ten in Albanian",
        "level": "beginner",
        "available_dialects": ["gheg", "tosk"],
        "word_count": 10,
    },
    {
        "id": 3,
        "title": "Colors",
        "title_sq": "Ngjyrat",
        "description": "Basic colors in Albanian",
        "level": "beginner",
        "available_dialects": ["gheg", "tosk"],
        "word_count": 7,
    },
    {
        "id": 4,
        "title": "Family Members",
        "title_sq": "Anëtarët e familjes",
        "description": "Words for family relationships",
        "level": "beginner",
        "available_dialects": ["gheg", "tosk"],
        "word_count": 10,
    },
]


@router.get("")
def get_all_lessons(
    dialect: Literal["gheg", "tosk"] = Query(
        default="tosk",
        description="Which dialect to filter lessons for"
    )
):
    """Return all available lessons for the selected dialect."""
    return {
        "dialect": dialect,
        "lessons": [
            lesson for lesson in MOCK_LESSONS
            if dialect in lesson["available_dialects"]
        ],
    }


@router.get("/{lesson_id}")
def get_lesson(
    lesson_id: int,
    dialect: Literal["gheg", "tosk"] = Query(default="tosk")
):
    """Return a single lesson by ID."""
    lesson = next((l for l in MOCK_LESSONS if l["id"] == lesson_id), None)
    if not lesson:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Lesson not found")
    return {"dialect": dialect, "lesson": lesson}
