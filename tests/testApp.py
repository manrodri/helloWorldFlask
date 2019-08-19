import unittest
from app import routes
import microblog

class TestMicroblog(unittest.TestCase):
    def test_helloWorld(self):
        self.assertEquals(4, 4)
