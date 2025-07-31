"""
Tests for the Task model.
"""
import pytest
from datetime import datetime, date
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from gamified_checklist.models.task import Task, TaskType, TaskDifficulty

class TestTask:
    """Test cases for the Task model."""
    
    def test_task_creation_basic(self):
        """Test creating a basic task with minimal parameters."""
        task = Task(
            title="Test Task",
            task_type=TaskType.DAILY,
            difficulty=TaskDifficulty.EASY,
            category="work"
        )
        
        assert task.title == "Test Task"
        assert task.task_type == TaskType.DAILY
        assert task.difficulty == TaskDifficulty.EASY
        assert task.category == "work"
        assert task.completed is False
        assert task.xp_value > 0  # Should calculate XP based on difficulty
        assert task.created_date == date.today()
        
    def test_task_creation_with_description(self):
        """Test creating a task with description."""
        task = Task(
            title="Complex Task",
            description="This is a detailed description",
            task_type=TaskType.QUEST,
            difficulty=TaskDifficulty.HARD,
            category="personal"
        )
        
        assert task.description == "This is a detailed description"
        assert task.task_type == TaskType.QUEST
        assert task.difficulty == TaskDifficulty.HARD
        
    def test_task_xp_calculation(self):
        """Test that XP is calculated correctly based on difficulty and type."""
        easy_daily = Task("Easy Daily", TaskType.DAILY, TaskDifficulty.EASY, "test")
        medium_daily = Task("Medium Daily", TaskType.DAILY, TaskDifficulty.MEDIUM, "test")
        hard_daily = Task("Hard Daily", TaskType.DAILY, TaskDifficulty.HARD, "test")
        
        easy_quest = Task("Easy Quest", TaskType.QUEST, TaskDifficulty.EASY, "test")
        
        # Quest tasks should give more XP than daily tasks
        assert easy_quest.xp_value > easy_daily.xp_value
        
        # Harder tasks should give more XP
        assert medium_daily.xp_value > easy_daily.xp_value
        assert hard_daily.xp_value > medium_daily.xp_value
        
    def test_task_completion(self):
        """Test task completion functionality."""
        task = Task("Test Task", TaskType.DAILY, TaskDifficulty.EASY, "test")
        
        assert task.completed is False
        assert task.completed_date is None
        
        # Complete the task
        task.mark_completed()
        
        assert task.completed is True
        assert task.completed_date == date.today()
        
    def test_task_uncomplete(self):
        """Test uncompleting a task."""
        task = Task("Test Task", TaskType.DAILY, TaskDifficulty.EASY, "test")
        task.mark_completed()
        
        assert task.completed is True
        
        task.mark_uncompleted()
        
        assert task.completed is False
        assert task.completed_date is None
        
    def test_task_to_dict(self):
        """Test converting task to dictionary for JSON serialization."""
        task = Task(
            title="Test Task",
            description="Test description",
            task_type=TaskType.QUEST,
            difficulty=TaskDifficulty.MEDIUM,
            category="work"
        )
        
        task_dict = task.to_dict()
        
        assert task_dict["title"] == "Test Task"
        assert task_dict["description"] == "Test description"
        assert task_dict["task_type"] == "quest"
        assert task_dict["difficulty"] == "medium"
        assert task_dict["category"] == "work"
        assert task_dict["completed"] is False
        assert "xp_value" in task_dict
        assert "created_date" in task_dict
        
    def test_task_from_dict(self):
        """Test creating task from dictionary."""
        task_data = {
            "title": "Restored Task",
            "description": "From dict",
            "task_type": "daily",
            "difficulty": "hard",
            "category": "personal",
            "completed": True,
            "xp_value": 50,
            "created_date": "2025-07-31",
            "completed_date": "2025-07-31"
        }
        
        task = Task.from_dict(task_data)
        
        assert task.title == "Restored Task"
        assert task.description == "From dict"
        assert task.task_type == TaskType.DAILY
        assert task.difficulty == TaskDifficulty.HARD
        assert task.category == "personal"
        assert task.completed is True
        assert task.xp_value == 50
