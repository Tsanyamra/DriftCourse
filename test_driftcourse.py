# test_driftcourse.py
"""
Tests for DriftCourse module.
"""

import unittest
from driftcourse import DriftCourse

class TestDriftCourse(unittest.TestCase):
    """Test cases for DriftCourse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DriftCourse()
        self.assertIsInstance(instance, DriftCourse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DriftCourse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
