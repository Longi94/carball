class SimilarSearch:

    @staticmethod
    def compare_cars(car1, car2):
        if car1.team != car2.team:
            return car2.team - car1.team
        if car1.position.x != car2.position.x:
            return car2.position.x - car1.position.x
        if car1.position.y != car2.position.y:
            return car2.position.y - car1.position.y
        if car1.position.z != car2.position.z:
            return car2.position.z - car1.position.z
        return 0

    @staticmethod
    def create_layers_from_positions(ball, car_positions):
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
            position = [total_list[i].position.x, total_list[i].position.y, total_list[i].position.z]
            layers = SimilarSearch.create_layers_from_point(position)
            for j in range(len(layers)):
                layer_list[j].append(layers[j])
            return layer_list

    @staticmethod
    def create_hashes_from_positions(ball, car_positions):
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
            position = [total_list[i].position.x, total_list[i].position.y, total_list[i].position.z]
            layers = SimilarSearch.create_layers_from_point(position)
            for j in range(len(layers)):
                layer_list[j].append(layers[j])
        for i in range(len(layer_list)):
            hashes.append(hash(tuple(layer_list[i])))
