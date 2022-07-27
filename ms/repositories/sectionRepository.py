from ms.models import Section
from ms.repositories import ResourceRepository
from .repository import Repository


class SectionRepository(Repository):
    def __init__(self):
        super().__init__()
        self.resourceRepo = ResourceRepository()

    def get_model(self):
        return Section

    def add_resource(self, id, data, fail=True):
        section = self.find(id, fail=fail)
        data['section_id'] = section.id
        self.resourceRepo.add(data)
        return section
