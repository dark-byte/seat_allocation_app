class Classroom:
    def __init__(self, seats_per_bench=3, benches=16):
        self.benches = benches  # Default to 16 benches
        self.seats_per_bench = seats_per_bench  # Supports 2 or 3 seats per bench
        self.seating_arrangement = []  # Initialize seating_arrangement here

    def add_seating(self, arrangement):
        self.seating_arrangement.extend(arrangement)
