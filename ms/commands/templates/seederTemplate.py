from faker import Faker
from flask_seeder import Seeder, generator


class <CLASSNAME>(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 10

    def run(self):
        fake = Faker()
