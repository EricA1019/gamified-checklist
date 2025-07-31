"""
Tests for the User model.
"""
import pytest
from datetime import date
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from gamified_checklist.models.user import User

class TestUser:
    """Test cases for the User model."""
    
    def test_user_creation(self):
        """Test creating a new user."""
        user = User()
        
        assert user.total_xp == 0
        assert user.current_level == 1
        assert user.current_streak == 0
        assert user.longest_streak == 0
        assert user.last_activity_date is None
        
    def test_user_add_xp(self):
        """Test adding XP to user."""
        user = User()
        
        user.add_xp(25)
        
        assert user.total_xp == 25
        assert user.last_activity_date == date.today()
        
    def test_user_level_up(self):
        """Test user leveling up when reaching XP threshold."""
        user = User()
        
        # Add enough XP to reach level 2 (assuming 100 XP needed)
        user.add_xp(100)
        
        assert user.current_level == 2
        assert user.total_xp == 100
        
    def test_user_multiple_level_ups(self):
        """Test user leveling up multiple times."""
        user = User()
        
        # Add enough XP for multiple levels
        user.add_xp(350)  # Should reach level 3 or 4
        
        assert user.current_level > 2
        assert user.total_xp == 350
        
    def test_user_xp_for_next_level(self):
        """Test calculating XP needed for next level."""
        user = User()
        
        xp_needed = user.xp_for_next_level()
        assert xp_needed > 0
        
        # After adding some XP, should still need XP for next level
        user.add_xp(25)  # Still at level 1
        new_xp_needed = user.xp_for_next_level()
        assert new_xp_needed < xp_needed  # Should need less now
        assert new_xp_needed == 25  # Should need 25 more for level 2
        
    def test_user_update_streak_same_day(self):
        """Test updating streak on the same day (should not increase)."""
        user = User()
        user.update_streak()
        
        first_streak = user.current_streak
        user.update_streak()  # Same day
        
        assert user.current_streak == first_streak
        
    def test_user_update_streak_consecutive_days(self):
        """Test updating streak on consecutive days."""
        user = User()
        
        # Simulate yesterday's activity
        yesterday = date.today().replace(day=date.today().day - 1)
        user.last_activity_date = yesterday
        user.current_streak = 1
        
        # Update streak today
        user.update_streak()
        
        assert user.current_streak == 2
        assert user.last_activity_date == date.today()
        
    def test_user_streak_reset_after_gap(self):
        """Test streak resets after missing days."""
        user = User()
        
        # Simulate activity 3 days ago
        three_days_ago = date.today().replace(day=date.today().day - 3)
        user.last_activity_date = three_days_ago
        user.current_streak = 5
        user.longest_streak = 5
        
        # Update streak today (should reset)
        user.update_streak()
        
        assert user.current_streak == 1  # Reset to 1
        assert user.longest_streak == 5  # Longest streak preserved
        
    def test_user_to_dict(self):
        """Test converting user to dictionary."""
        user = User()
        user.add_xp(150)
        user.update_streak()  # This should set current_streak to 1
        
        user_dict = user.to_dict()
        
        assert user_dict["total_xp"] == 150
        assert user_dict["current_level"] >= 1
        assert user_dict["current_streak"] == 1
        assert user_dict["longest_streak"] >= 1
        assert "last_activity_date" in user_dict
        
    def test_user_from_dict(self):
        """Test creating user from dictionary."""
        user_data = {
            "total_xp": 250,
            "current_level": 3,
            "current_streak": 7,
            "longest_streak": 12,
            "last_activity_date": "2025-07-31"
        }
        
        user = User.from_dict(user_data)
        
        assert user.total_xp == 250
        assert user.current_level == 3
        assert user.current_streak == 7
        assert user.longest_streak == 12
