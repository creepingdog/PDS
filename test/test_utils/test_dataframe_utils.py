
import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
import lib.utils.dataframe_utils as dfu

class TestDataFrameUtils(unittest.TestCase):
    """
    Test the add function from the dataframe_utils library
    """

    def test_value_counts_by_columns(self):
        # """
        # Test that the addition of two integers returns the correct total
        # """

        df = pd.DataFrame([['F','Asian'],
                           ['F','Hispanic'],
                           ['M','Latino'],
                           ['F','Latino']], columns=['Sex','Race'])
        ret = dfu.value_counts_by_columns(df, ['Sex','Race'])
        # print(ret)
        idx = pd.MultiIndex.from_tuples([('Sex','F'),('Sex','M'),('Race','Asian'),('Race','Hispanic'),('Race','Latino')])

        target = pd.DataFrame([3,1,1,1,2],
                              index=idx,
                              columns=['Count',])

        # print(target)
        assert_frame_equal(ret, target)
#

if __name__ == '__main__':
    unittest.main()