"""
User model for tracking progress, levels, and streaks.
"""
from datetime import date, timedelta
from typing import Dict, Any, Optional
import math

class User:
    """
    Represents a user with their progress and statistics.
    
    Attributes:
        total_xp: Total experience points earned
        current_level: Current user level
        current_streak: Current consecutive days streak
        longest_streak: Longest streak ever achieved
        last_activity_date: Date of last task completion
    """
    
    def __init__(
        self,
        total_xp: int = 0,
        current_level: int = 1,
        current_streak: int = 0,
        longest_streak: int = 0,
        last_activity_date: Optional[date] = None
    ):
        self.total_xp = total_xp
        self.current_streak = current_streak
        self.longest_streak = longest_streak
        self.last_activity_date = last_activity_date
        
        # Only auto-calculate level if not provided explicitly
        if current_level == 1 and total_xp > 0:
            self.current_level = self._calculate_level(total_xp)
        else:
            self.current_level = current_level
    
    def add_xp(self, xp_amount: int) -> None:
        """
        Add XP to the user and update level if necessary.
        
        Args:
            xp_amount: Amount of XP to add
        """
        self.total_xp += xp_amount
        self.last_activity_date = date.today()
        self._update_level()
    
    def _update_level(self) -> None:
        """Update the user's level based on total XP."""
        new_level = self._calculate_level(self.total_xp)
        self.current_level = new_level
    
    def _calculate_level(self, total_xp: int) -> int:
        """
        Calculate level based on total XP using exponential curve.
        
        Formula: Level = floor(sqrt(total_xp / 50)) + 1
        This means:
        - Level 1: 0-49 XP
        - Level 2: 50-199 XP  
        - Level 3: 200-449 XP
        - Level 4: 450-799 XP
        - etc.
        """
        if total_xp < 0:
            return 1
        return math.floor(math.sqrt(total_xp / 50)) + 1
    
    def _xp_required_for_level(self, level: int) -> int:
        """Calculate total XP required to reach a specific level."""
        if level <= 1:
            return 0
        return ((level - 1) ** 2) * 50
    
    def xp_for_next_level(self) -> int:
        """Calculate XP needed to reach the next level."""
        next_level_xp = self._xp_required_for_level(self.current_level + 1)
        return next_level_xp - self.total_xp
    
    def update_streak(self) -> None:
        """
        Update the user's streak based on activity.
        
        Rules:
        - If no previous activity, start streak at 1
        - If last activity was yesterday, increment streak
        - If last activity was today and streak is 0, set to 1
        - If last activity was today and streak > 0, no change
        - If last activity was 2+ days ago, reset streak to 1
        """
        today = date.today()
        
        if self.last_activity_date is None:
            # First activity ever
            self.current_streak = 1
            self.last_activity_date = today
        elif self.last_activity_date == today:
            # Already active today
            if self.current_streak == 0:
                # First activity today
                self.current_streak = 1
            # Otherwise no change to streak count
        elif self.last_activity_date == today - timedelta(days=1):
            # Activity yesterday, increment streak
            self.current_streak += 1
            self.last_activity_date = today
        else:
            # Gap in activity, reset streak
            self.current_streak = 1
            self.last_activity_date = today
        
        # Update longest streak if current is higher
        if self.current_streak > self.longest_streak:
            self.longest_streak = self.current_streak
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert user to dictionary for JSON serialization."""
        return {
            "total_xp": self.total_xp,
            "current_level": self.current_level,
            "current_streak": self.current_streak,
            "longest_streak": self.longest_streak,
            "last_activity_date": self.last_activity_date.isoformat() if self.last_activity_date else None,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "User":
        """Create a user from dictionary data."""
        last_activity_date = None
        if data.get("last_activity_date"):
            last_activity_date = date.fromisoformat(data["last_activity_date"])
        
        # Use provided level directly, don't recalculate
        return cls(
            total_xp=data.get("total_xp", 0),
            current_level=data.get("current_level", 1),
            current_streak=data.get("current_streak", 0),
            longest_streak=data.get("longest_streak", 0),
            last_activity_date=last_activity_date,
        )
    
    def __repr__(self) -> str:
        """String representation of the user."""
        return f"Level {self.current_level} ({self.total_xp} XP, {self.current_streak} day streak)"
