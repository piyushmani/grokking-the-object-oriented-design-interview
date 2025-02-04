from dataclasses import dataclass
from typing import Optional
from .user import User

@dataclass
class Admin(User):
    role: str = ""
    permissions: Optional[List[str]] = None

    def grant_permission(self, permission: str):
        if self.permissions is None:
            self.permissions = []
        self.permissions.append(permission)

    def revoke_permission(self, permission: str):
        if self.permissions and permission in self.permissions:
            self.permissions.remove(permission)
