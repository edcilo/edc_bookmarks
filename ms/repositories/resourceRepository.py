from ms.models import Resource
from .repository import Repository


class ResourceRepository(Repository):
    def get_model(self):
        return Resource
