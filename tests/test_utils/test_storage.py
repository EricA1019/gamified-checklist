"""
Tests for the storage utility.
"""
import pytest
import tempfile
import shutil
from pathlib import Path
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from gamified_checklist.utils.storage import DataStorage
from gamified_checklist.models.task import Task, TaskType, TaskDifficulty
from gamified_checklist.models.category import Category
from gamified_checklist.models.user import User

class TestDataStorage:
    """Test cases for the DataStorage utility."""
    
    def setup_method(self):
        """Set up test environment with temporary directory."""
        self.temp_dir = tempfile.mkdtemp()
        self.storage = DataStorage(self.temp_dir)
    
    def teardown_method(self):
        """Clean up temporary directory."""
        shutil.rmtree(self.temp_dir)
    
    def test_user_save_and_load(self):
        """Test saving and loading user data."""
        # Create a user with some data
        user = User(total_xp=150, current_level=2, current_streak=5)
        
        # Save user
        success = self.storage.save_user(user)
        assert success is True
        
        # Load user
        loaded_user = self.storage.load_user()
        assert loaded_user is not None
        assert loaded_user.total_xp == 150
        assert loaded_user.current_level == 2
        assert loaded_user.current_streak == 5
    
    def test_user_load_no_file(self):
        """Test loading user when no file exists."""
        loaded_user = self.storage.load_user()
        assert loaded_user is not None
        assert loaded_user.total_xp == 0
        assert loaded_user.current_level == 1
        assert loaded_user.current_streak == 0
    
    def test_tasks_save_and_load(self):
        """Test saving and loading tasks."""
        # Create some tasks
        tasks = [
            Task("Task 1", TaskType.DAILY, TaskDifficulty.EASY, "work"),
            Task("Task 2", TaskType.QUEST, TaskDifficulty.HARD, "personal"),
        ]
        tasks[0].mark_completed()
        
        # Save tasks
        success = self.storage.save_tasks(tasks)
        assert success is True
        
        # Load tasks
        loaded_tasks = self.storage.load_tasks()
        assert len(loaded_tasks) == 2
        assert loaded_tasks[0].title == "Task 1"
        assert loaded_tasks[0].completed is True
        assert loaded_tasks[1].title == "Task 2"
        assert loaded_tasks[1].completed is False
    
    def test_tasks_load_no_file(self):
        """Test loading tasks when no file exists."""
        loaded_tasks = self.storage.load_tasks()
        assert loaded_tasks == []
    
    def test_categories_save_and_load(self):
        """Test saving and loading categories."""
        # Create some categories
        categories = [
            Category("work", "Work Tasks", "💼", "#3498db"),
            Category("custom", "Custom Category", "🎯", "#e74c3c"),
        ]
        
        # Save categories
        success = self.storage.save_categories(categories)
        assert success is True
        
        # Load categories
        loaded_categories = self.storage.load_categories()
        assert len(loaded_categories) == 2
        assert loaded_categories[0].name == "work"
        assert loaded_categories[0].display_name == "Work Tasks"
        assert loaded_categories[1].name == "custom"
        assert loaded_categories[1].emoji == "🎯"
    
    def test_categories_load_no_file(self):
        """Test loading categories when no file exists (should return defaults)."""
        loaded_categories = self.storage.load_categories()
        assert len(loaded_categories) > 0  # Should have default categories
        category_names = [cat.name for cat in loaded_categories]
        assert "work" in category_names
        assert "personal" in category_names
    
    def test_save_all(self):
        """Test saving all data at once."""
        user = User(total_xp=100)
        tasks = [Task("Test Task", TaskType.DAILY, TaskDifficulty.MEDIUM, "work")]
        categories = [Category("work")]
        
        success = self.storage.save_all(user, tasks, categories)
        assert success is True
        
        # Verify files exist
        assert self.storage.user_file.exists()
        assert self.storage.tasks_file.exists()
        assert self.storage.categories_file.exists()
    
    def test_load_all(self):
        """Test loading all data at once."""
        # First save some data
        user = User(total_xp=200)
        tasks = [Task("Test Task", TaskType.QUEST, TaskDifficulty.HARD, "personal")]
        categories = [Category("personal")]
        
        self.storage.save_all(user, tasks, categories)
        
        # Load all data
        loaded_user, loaded_tasks, loaded_categories = self.storage.load_all()
        
        assert loaded_user.total_xp == 200
        assert len(loaded_tasks) == 1
        assert loaded_tasks[0].title == "Test Task"
        assert len(loaded_categories) >= 1  # At least the one we saved
    
    def test_backup_data(self):
        """Test creating data backup."""
        # Save some data first
        user = User(total_xp=50)
        self.storage.save_user(user)
        
        # Create backup
        success = self.storage.backup_data()
        assert success is True
        
        # Check that backup directory was created
        backup_dirs = [d for d in Path(self.temp_dir).iterdir() if d.is_dir() and d.name.startswith("backup_")]
        assert len(backup_dirs) > 0
