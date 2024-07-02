# models/admin.py
from models.member import Member
from models.account import AccountStatus

class Admin(Member):
    def block_member(self, member: Member):
        if member.account.status != AccountStatus.BLOCKED:
            member.account.status = AccountStatus.BLOCKED
            print(f"Member {member.account.name} is now blocked.")
        else:
            print(f"Member {member.account.name} is already blocked.")

    def unblock_member(self, member: Member):
        if member.account.status == AccountStatus.BLOCKED:
            member.account.status = AccountStatus.ACTIVE
            print(f"Member {member.account.name} is now unblocked.")
        else:
            print(f"Member {member.account.name} is not blocked.")
