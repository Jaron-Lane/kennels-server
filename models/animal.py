class Animal():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, breed, status, pos5, customer_id):
        self.id = id
        self.name = name
        self.breed = breed
        self.status = status
        self.location_id = pos5
        self.customer_id = customer_id
        self.location = None