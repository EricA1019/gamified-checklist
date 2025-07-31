"""
Tests for the Category model.
"""
import pytest
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from gamified_checklist.models.category import Category

class TestCategory:
    """Test cases for the Category model."""
    
    def test_category_creation(self):
        """Test creating a category."""
        category = Category(
            name="work",
            display_name="Work Tasks",
            emoji="💼",
            color="#3498db"
        )
        
        assert category.name == "work"
        assert category.display_name == "Work Tasks"
        assert category.emoji == "💼"
        assert category.color == "#3498db"
        
    def test_category_creation_minimal(self):
        """Test creating a category with minimal parameters."""
        category = Category(name="personal")
        
        assert category.name == "personal"
        assert category.display_name == "Personal"  # Should auto-capitalize
        assert category.emoji == "📝"  # Default emoji
        assert category.color == "#95a5a6"  # Default color
        
    def test_category_to_dict(self):
        """Test converting category to dictionary."""
        category = Category(
            name="health",
            display_name="Health & Fitness",
            emoji="🏃‍♂️",
            color="#e74c3c"
        )
        
        category_dict = category.to_dict()
        
        assert category_dict["name"] == "health"
        assert category_dict["display_name"] == "Health & Fitness"
        assert category_dict["emoji"] == "🏃‍♂️"
        assert category_dict["color"] == "#e74c3c"
        
    def test_category_from_dict(self):
        """Test creating category from dictionary."""
        category_data = {
            "name": "learning",
            "display_name": "Learning & Education",
            "emoji": "📚",
            "color": "#9b59b6"
        }
        
        category = Category.from_dict(category_data)
        
        assert category.name == "learning"
        assert category.display_name == "Learning & Education"
        assert category.emoji == "📚"
        assert category.color == "#9b59b6"
        
    def test_category_equality(self):
        """Test category equality comparison."""
        category1 = Category("work", "Work", "💼")
        category2 = Category("work", "Work Tasks", "💼")  # Different display name
        category3 = Category("personal", "Personal", "📝")
        
        # Categories with same name should be equal
        assert category1 == category2
        assert category1 != category3
