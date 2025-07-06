"""
Pytest configuration and shared fixtures for the test suite.
"""
import pytest
from pathlib import Path
import sys

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))
