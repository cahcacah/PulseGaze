# test_pulsegaze.py
"""
Tests for PulseGaze module.
"""

import unittest
from pulsegaze import PulseGaze

class TestPulseGaze(unittest.TestCase):
    """Test cases for PulseGaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PulseGaze()
        self.assertIsInstance(instance, PulseGaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PulseGaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
