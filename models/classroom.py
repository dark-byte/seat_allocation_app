
class Classroom:
    def __init__(self, benches, seats_per_bench, departments):
        self.benches = benches
        self.seats_per_bench = seats_per_bench
        self.departments = departments  # List of two departments

    def get_total_seats(self):
        return self.benches * self.seats_per_bench
