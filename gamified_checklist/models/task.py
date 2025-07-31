"""
Task model for the Gamified Checklist app.
"""
from enum import Enum
from datetime import date
from typing import Optional, Dict, Any

class TaskType(Enum):
    """Enum for task types."""
    DAILY = "daily"
    QUEST = "quest"

class TaskDifficulty(Enum):
    """Enum for task difficulty levels."""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class Task:
    """
    Represents a task in the gamified checklist.
    
    Attributes:
        title: The task title
        description: Optional task description
        task_type: Whether it's a daily task or quest
        difficulty: Task difficulty level
        category: Task category name
        completed: Whether the task is completed
        xp_value: XP points earned for completing this task
        created_date: Date when task was created
        completed_date: Date when task was completed (if any)
    """
    
    # XP base values for different difficulties and types
    XP_BASE_VALUES = {
        TaskDifficulty.EASY: 10,
        TaskDifficulty.MEDIUM: 20,
        TaskDifficulty.HARD: 35,
    }
    
    TYPE_MULTIPLIERS = {
        TaskType.DAILY: 1.0,
        TaskType.QUEST: 2.0,  # Quests give double XP
    }
    
    def __init__(
        self,
        title: str,
        task_type: TaskType,
        difficulty: TaskDifficulty,
        category: str,
        description: str = "",
        completed: bool = False,
        xp_value: Optional[int] = None,
        created_date: Optional[date] = None,
        completed_date: Optional[date] = None
    ):
        self.title = title
        self.description = description
        self.task_type = task_type
        self.difficulty = difficulty
        self.category = category
        self.completed = completed
        self.created_date = created_date or date.today()
        self.completed_date = completed_date
        
        # Calculate XP value if not provided
        if xp_value is None:
            base_xp = self.XP_BASE_VALUES[difficulty]
            multiplier = self.TYPE_MULTIPLIERS[task_type]
            self.xp_value = int(base_xp * multiplier)
        else:
            self.xp_value = xp_value
    
    def mark_completed(self) -> None:
        """Mark the task as completed."""
        self.completed = True
        self.completed_date = date.today()
    
    def mark_uncompleted(self) -> None:
        """Mark the task as not completed."""
        self.completed = False
        self.completed_date = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary for JSON serialization."""
        return {
            "title": self.title,
            "description": self.description,
            "task_type": self.task_type.value,
            "difficulty": self.difficulty.value,
            "category": self.category,
            "completed": self.completed,
            "xp_value": self.xp_value,
            "created_date": self.created_date.isoformat(),
            "completed_date": self.completed_date.isoformat() if self.completed_date else None,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        """Create a task from dictionary data."""
        # Parse dates
        created_date = date.fromisoformat(data["created_date"]) if data["created_date"] else None
        completed_date = date.fromisoformat(data["completed_date"]) if data.get("completed_date") else None
        
        return cls(
            title=data["title"],
            description=data.get("description", ""),
            task_type=TaskType(data["task_type"]),
            difficulty=TaskDifficulty(data["difficulty"]),
            category=data["category"],
            completed=data.get("completed", False),
            xp_value=data.get("xp_value"),
            created_date=created_date,
            completed_date=completed_date,
        )
    
    def __repr__(self) -> str:
        """String representation of the task."""
        status = "✅" if self.completed else "⭕"
        return f"{status} {self.title} ({self.difficulty.value}, {self.xp_value} XP)"
