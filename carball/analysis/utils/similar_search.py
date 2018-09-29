import numpy as np
from carball.analysis.utils.split_location import LocationSplitManager


class SimilarSearch:

    def __init__(self, location_split_managner: LocationSplitManager):
        self.location_split_manager = location_split_managner

    def compare_cars(self, car1, car2):
        if car1.team != car2.team:
            return car2.is_orange - car1.is_orange
        if car1.pos_x != car2.pos_x:
            return car2.pos_x - car1.pos_x
        if car1.pos_y != car2.pos_y:
            return car2.pos_y - car1.pos_y
        if car1.pos_z != car2.pos_z:
            return car2.pos_z - car1.pos_z
        return 0

    def create_layers_from_positions(self, ball, car_positions):
        """
        Creates the hash of the position that can be used for searching.
        :param ball: has a field called: position
        :param car_positions: has a fields called: team, position
        :return: A list of hashes equal to the number of layers
        """
        # sort the list so that the hash is consistent
        car_positions.sort(cmp=lambda car1, car2: SimilarSearch.compare_cars(car1, car2))
        total_list = [ball] + car_positions
        layer_list = [[], [], []]
        for i in range(len(total_list)):
            position = np.array([total_list[i].pos_x, total_list[i].pos_y, total_list[i].pos_z])
            layers = self.location_split_manager.create_boxes(position)
            for j in range(len(layers)):
                layer_list[j].append(layers[j])
            return layer_list

    def create_hashes_from_positions(self, ball, car_positions):
        """
        Creates the hash of the position that can be used for searching.
        :param ball: has a field called: position
        :param car_positions: has a fields called: team, position
        :return: A list of hashes equal to the number of layers
        """
        # sort the list so that the hash is consistent
        car_positions.sort(cmp=lambda car1, car2: SimilarSearch.compare_cars(car1, car2))
        total_list = [ball] + car_positions
        layer_list = [[], [], []]
        hashes = []
        for i in range(len(total_list)):
            position = np.array([total_list[i].pos_x, total_list[i].pos_y, total_list[i].pos_z])
            layers = self.location_split_manager.create_boxes(position)
            for j in range(len(layers)):
                layer_list[j].append(layers[j])
        for i in range(len(layer_list)):
            hashes.append(hash(tuple(layer_list[i])))
