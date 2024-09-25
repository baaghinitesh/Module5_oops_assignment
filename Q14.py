# 14. Write a class method that keeps track of the number of instances created from a class.

class InstanceCounter:
    instance_count = 0  # Class variable to keep track of the number of instances

    def __init__(self):
        InstanceCounter.instance_count += 1  # Increment the count when an instance is created

    @classmethod
    def get_instance_count(cls):
        return cls.instance_count  # Class method to access the instance count

# Example usage
if __name__ == "__main__":
    obj1 = InstanceCounter()
    obj2 = InstanceCounter()
    obj3 = InstanceCounter()

    print(f"Number of instances created: {InstanceCounter.get_instance_count()}")
