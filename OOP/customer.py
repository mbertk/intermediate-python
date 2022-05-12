class Customer:
    def __init__(self, first_name, second_name, tier=("free", 0)):
        self.first_name = first_name
        self.second_name = second_name
        self.name = first_name + " " + second_name
        self.tier = tier

    def can_access(self, item):
        if item["tier"] == "premium" and self.tier[0] == "free":
            return False
        else:
            return True

    def bill_for(self, time):
        total = time * self.tier[1]
        print(f"{total} ({time} months at {self.tier[1]}$/mo)")

    @classmethod
    def premium(cls, first_name, second_name):
        return cls(first_name, second_name, tier=("premium", 10))


if __name__ == '__main__':
    # This won't run until you implement the `Customer` class!

    marco = Customer('Marco', 'Polo')  # Defaults to the free tier
    print(marco.name)  # Marco Polo
    print(marco.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(marco.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # False

    victoria = Customer.premium("Alexandrina",
                                "Victoria")  # Build a customer around the ('premium', 10$/mo) streaming plan.
    print(victoria.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(victoria.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # True
    print(victoria.bill_for(5))  # => 50 (5 months at 10$/mo)
    print(victoria.name)  # Alexandrina Victoria