class BasicBuilding(object):
    def __init__(self, floors=1, purpose="living", material="concrete", year_built=2000, is_finished=False):
        self.floors = floors
        self.purpose = purpose
        self.material = material
        self.year_built = year_built
        self.is_building_finished = is_finished

    def add_floors(self, quantity):
        self.floors += quantity

    def consider_as_finished(self, year_when_finished):
        self.year_built = year_when_finished
        self.is_building_finished = True

    @staticmethod
    def open_doors():
        print("Doors are opened")

    @staticmethod
    def close_doors():
        print("Doors are closed")
