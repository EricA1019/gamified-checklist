"""
Category model for organizing tasks.
"""
from typing import Dict, Any, Optional

class Category:
    """
    Represents a task category with display properties.
    
    Attributes:
        name: Unique category identifier (lowercase)
        display_name: Human-readable category name
        emoji: Emoji icon for the category
        color: Hex color code for the category
    """
    
    # Default values for common categories
    DEFAULT_CATEGORIES = {
        "work": {"display_name": "Work", "emoji": "💼", "color": "#3498db"},
        "personal": {"display_name": "Personal", "emoji": "📝", "color": "#95a5a6"},
        "health": {"display_name": "Health", "emoji": "🏃‍♂️", "color": "#e74c3c"},
        "learning": {"display_name": "Learning", "emoji": "📚", "color": "#9b59b6"},
        "finance": {"display_name": "Finance", "emoji": "💰", "color": "#f39c12"},
        "home": {"display_name": "Home", "emoji": "🏠", "color": "#27ae60"},
        "social": {"display_name": "Social", "emoji": "👥", "color": "#e67e22"},
        "hobby": {"display_name": "Hobby", "emoji": "🎨", "color": "#f1c40f"},
    }
    
    def __init__(
        self,
        name: str,
        display_name: Optional[str] = None,
        emoji: Optional[str] = None,
        color: Optional[str] = None
    ):
        self.name = name.lower()
        
        # Use defaults if category exists in defaults, otherwise use provided values or fallbacks
        defaults = self.DEFAULT_CATEGORIES.get(self.name, {})
        
        self.display_name = display_name or defaults.get("display_name", name.capitalize())
        self.emoji = emoji or defaults.get("emoji", "📝")
        self.color = color or defaults.get("color", "#95a5a6")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert category to dictionary for JSON serialization."""
        return {
            "name": self.name,
            "display_name": self.display_name,
            "emoji": self.emoji,
            "color": self.color,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Category":
        """Create a category from dictionary data."""
        return cls(
            name=data["name"],
            display_name=data.get("display_name"),
            emoji=data.get("emoji"),
            color=data.get("color"),
        )
    
    def __eq__(self, other) -> bool:
        """Categories are equal if they have the same name."""
        if not isinstance(other, Category):
            return False
        return self.name == other.name
    
    def __hash__(self) -> int:
        """Hash based on category name."""
        return hash(self.name)
    
    def __repr__(self) -> str:
        """String representation of the category."""
        return f"{self.emoji} {self.display_name}"
