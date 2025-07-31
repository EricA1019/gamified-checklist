"""
JSON storage utility for persisting app data.
"""
import json
import os
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import date

from gamified_checklist.models.task import Task
from gamified_checklist.models.category import Category
from gamified_checklist.models.user import User
from gamified_checklist.utils.logger import log_info, log_error

class DataStorage:
    """
    Handles saving and loading application data to/from JSON files.
    """
    
    def __init__(self, data_dir: str = "data"):
        """
        Initialize storage with data directory.
        
        Args:
            data_dir: Directory to store data files
        """
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        self.user_file = self.data_dir / "user.json"
        self.tasks_file = self.data_dir / "tasks.json"
        self.categories_file = self.data_dir / "categories.json"
    
    def save_user(self, user: User) -> bool:
        """
        Save user data to JSON file.
        
        Args:
            user: User object to save
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(self.user_file, 'w') as f:
                json.dump(user.to_dict(), f, indent=2)
            log_info(f"User data saved to {self.user_file}", "Storage")
            return True
        except Exception as e:
            log_error(f"Failed to save user data: {e}", "Storage")
            return False
    
    def load_user(self) -> Optional[User]:
        """
        Load user data from JSON file.
        
        Returns:
            User object if successful, None otherwise
        """
        try:
            if not self.user_file.exists():
                log_info("No user data file found, creating new user", "Storage")
                return User()
            
            with open(self.user_file, 'r') as f:
                data = json.load(f)
            
            user = User.from_dict(data)
            log_info(f"User data loaded from {self.user_file}", "Storage")
            return user
        except Exception as e:
            log_error(f"Failed to load user data: {e}", "Storage")
            return User()  # Return new user on error
    
    def save_tasks(self, tasks: List[Task]) -> bool:
        """
        Save tasks list to JSON file.
        
        Args:
            tasks: List of Task objects to save
            
        Returns:
            True if successful, False otherwise
        """
        try:
            tasks_data = [task.to_dict() for task in tasks]
            with open(self.tasks_file, 'w') as f:
                json.dump(tasks_data, f, indent=2)
            log_info(f"Tasks data saved to {self.tasks_file} ({len(tasks)} tasks)", "Storage")
            return True
        except Exception as e:
            log_error(f"Failed to save tasks data: {e}", "Storage")
            return False
    
    def load_tasks(self) -> List[Task]:
        """
        Load tasks from JSON file.
        
        Returns:
            List of Task objects
        """
        try:
            if not self.tasks_file.exists():
                log_info("No tasks data file found, returning empty list", "Storage")
                return []
            
            with open(self.tasks_file, 'r') as f:
                data = json.load(f)
            
            tasks = [Task.from_dict(task_data) for task_data in data]
            log_info(f"Tasks data loaded from {self.tasks_file} ({len(tasks)} tasks)", "Storage")
            return tasks
        except Exception as e:
            log_error(f"Failed to load tasks data: {e}", "Storage")
            return []
    
    def save_categories(self, categories: List[Category]) -> bool:
        """
        Save categories list to JSON file.
        
        Args:
            categories: List of Category objects to save
            
        Returns:
            True if successful, False otherwise
        """
        try:
            categories_data = [category.to_dict() for category in categories]
            with open(self.categories_file, 'w') as f:
                json.dump(categories_data, f, indent=2)
            log_info(f"Categories data saved to {self.categories_file} ({len(categories)} categories)", "Storage")
            return True
        except Exception as e:
            log_error(f"Failed to save categories data: {e}", "Storage")
            return False
    
    def load_categories(self) -> List[Category]:
        """
        Load categories from JSON file.
        
        Returns:
            List of Category objects
        """
        try:
            if not self.categories_file.exists():
                # Return default categories if no file exists
                default_categories = self._get_default_categories()
                log_info("No categories data file found, using defaults", "Storage")
                return default_categories
            
            with open(self.categories_file, 'r') as f:
                data = json.load(f)
            
            categories = [Category.from_dict(cat_data) for cat_data in data]
            log_info(f"Categories data loaded from {self.categories_file} ({len(categories)} categories)", "Storage")
            return categories
        except Exception as e:
            log_error(f"Failed to load categories data: {e}", "Storage")
            return self._get_default_categories()
    
    def _get_default_categories(self) -> List[Category]:
        """Get default categories for new installations."""
        return [
            Category("work"),
            Category("personal"),
            Category("health"),
            Category("learning"),
            Category("finance"),
            Category("home"),
        ]
    
    def save_all(self, user: User, tasks: List[Task], categories: List[Category]) -> bool:
        """
        Save all data (user, tasks, categories) to their respective files.
        
        Args:
            user: User object
            tasks: List of tasks
            categories: List of categories
            
        Returns:
            True if all saves successful, False otherwise
        """
        user_saved = self.save_user(user)
        tasks_saved = self.save_tasks(tasks)
        categories_saved = self.save_categories(categories)
        
        return user_saved and tasks_saved and categories_saved
    
    def load_all(self) -> tuple[User, List[Task], List[Category]]:
        """
        Load all data from files.
        
        Returns:
            Tuple of (user, tasks, categories)
        """
        user = self.load_user() or User()  # Ensure we always return a User object
        tasks = self.load_tasks()
        categories = self.load_categories()
        
        return user, tasks, categories
    
    def backup_data(self) -> bool:
        """
        Create a backup of all data files with timestamp.
        
        Returns:
            True if backup successful, False otherwise
        """
        try:
            timestamp = date.today().isoformat()
            backup_dir = self.data_dir / f"backup_{timestamp}"
            backup_dir.mkdir(exist_ok=True)
            
            # Copy files to backup directory
            import shutil
            
            if self.user_file.exists():
                shutil.copy2(self.user_file, backup_dir / "user.json")
            if self.tasks_file.exists():
                shutil.copy2(self.tasks_file, backup_dir / "tasks.json")
            if self.categories_file.exists():
                shutil.copy2(self.categories_file, backup_dir / "categories.json")
            
            log_info(f"Data backed up to {backup_dir}", "Storage")
            return True
        except Exception as e:
            log_error(f"Failed to backup data: {e}", "Storage")
            return False
