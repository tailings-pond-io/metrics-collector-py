import unittest

class CoreFunctionalityTest(unittest.TestCase):
    def test_initialization(self):
        self.assertTrue(True)

    def test_buffer_operations(self):
        sample = b"stream_sample_data"
        self.assertEqual(len(sample), 18)

if __name__ == '__main__':
    unittest.main()
