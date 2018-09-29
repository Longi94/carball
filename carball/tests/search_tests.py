import unittest

import numpy as np

from carball.analysis.utils.similar_search import SimilarSearch
from ..analysis.utils.split_location import LocationSplitManager, STANDARD_MIN_VALUES, STANDARD_MAX_VALUES


class DBTest(unittest.TestCase):

    def setUp(self):
        self.split_manager = LocationSplitManager(3, np.array([7, 7, 5]), STANDARD_MIN_VALUES, STANDARD_MAX_VALUES)
        self.search_manager = SimilarSearch(self.split_manager)
        self.ball_position = np.array([0, 0, 0])
        self.cars = []

    def test_search(self):
        self.search_manager.create_hashes_from_positions()


if __name__ == '__main__':
    unittest.main()
