import unittest

import pandas as pd

from src.utils import count_unique_values


class TestHelpers(unittest.TestCase):
    def test_count_unique_values(self):
        input_df = pd.DataFrame([
            {"properties.zipcodes": "21211"},
            {"properties.zipcodes": "21211"},
            {"properties.zipcodes": "21212"}
        ])

        expected_output_df = pd.DataFrame([
            {"properties.zipcodes": "21211", "Counts": 2},
            {"properties.zipcodes": "21212", "Counts": 1},
        ])

        # Call the function under test
        output_df = count_unique_values(input_df, "properties.zipcodes")

        # Assert that the output matches the expected output
        pd.testing.assert_frame_equal(expected_output_df, output_df)


if __name__ == '__main__':
    unittest.main()
