from ms.models import Workspace
from ms.repositories import SectionRepository
from .repository import Repository


class WorkspaceRepository(Repository):
    def __init__(self) -> None:
        super().__init__()
        self.sectionRepo = SectionRepository()

    def get_model(self):
        return Workspace

    def add_section(self, id, data, fail=True):
        workspace = self.find(id, fail=fail)
        data['workspace_id'] = workspace.id
        self.sectionRepo.add(data)
        return workspace
