class Flight:
    def _init_(self, origin, destination, duration):

        self.origin = origin
        self.destination=destination
        self.duration=duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight duration: {self.duration}")

def main():
    f=Flight(origin="New York", destination="Paris", duration=540)

    f.duration+=10

    print(f.origin)
    print(f.destination)
    print(f.duration)

