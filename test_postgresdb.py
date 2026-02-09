# test_postgresdb.py
"""
Tests for PostgresDb module.
"""

import unittest
from postgresdb import PostgresDb

class TestPostgresDb(unittest.TestCase):
    """Test cases for PostgresDb class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PostgresDb()
        self.assertIsInstance(instance, PostgresDb)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PostgresDb()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
