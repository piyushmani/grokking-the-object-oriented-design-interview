# main.py
import datetime

from models.account import Account
from models.member import Member
from models.admin import Admin
from models.moderator import Moderator
from models.badge import Badge
from models.tag import Tag
from models.notification import Notification
from models.photo import Photo
from models.bounty import Bounty
from models.question import Question
from models.comment import Comment
from models.answer import Answer
from enums.account_status import AccountStatus
from enums.question_status import QuestionStatus
from enums.question_closing_remark import QuestionClosingRemark


def main():
    # Creating accounts
    account1 = Account(
        id="1",
        password="password1",
        name="John Doe",
        email="john@example.com",
        address="123 Street",
        phone=1234567890,
        status=AccountStatus.ACTIVE,
        reputation=100
    )

    account2 = Account(
        id="2",
        password="password2",
        name="Jane Smith",
        email="jane@example.com",
        address="456 Avenue",
        phone=9876543210,
        status=AccountStatus.ACTIVE,
        reputation=200
    )

    # Resetting password
    account1.reset_password("new_password1")

    # Creating members
    member1 = Member(account=account1)
    member2 = Member(account=account2)

    # Creating admin and moderator
    admin = Admin(account=account1)
    moderator = Moderator(account=account2)

    # Creating badges
    badge1 = Badge(name="Gold Badge", description="Awarded for excellence")
    badge2 = Badge(name="Silver Badge", description="Awarded for good performance")

    member1.badges.append(badge1)
    member2.badges.append(badge2)

    # Creating and adding tags
    tag1 = Tag(name="Python", description="Questions related to Python")
    tag2 = Tag(name="OOP", description="Questions related to Object-Oriented Programming")

    member1.create_tag(tag1)
    member2.create_tag(tag2)

    # Creating notifications
    notification1 = Notification(notification_id=1, content="You have a new message")
    notification2 = Notification(notification_id=2, content="Your question has been answered")

    notification1.send_notification()
    notification2.send_notification()

    # Creating and deleting photos
    photo1 = Photo(photo_id=1, photo_path="/photos/photo1.jpg", creating_member=member1)
    photo2 = Photo(photo_id=2, photo_path="/photos/photo2.jpg", creating_member=member2)

    photo1.delete()
    photo2.delete()

    # Creating bounty
    bounty = Bounty(reputation=50, expiry=datetime.datetime.now() + datetime.timedelta(days=7))

    bounty.modify_reputation(100)

    # Creating questions
    question1 = Question(
        title="How to implement class diagrams?",
        description="Detailed question about class diagrams.",
        bounty=bounty,
        asking_member=member1
    )

    question2 = Question(
        title="What is polymorphism in OOP?",
        description="Explanation of polymorphism in object-oriented programming.",
        bounty=bounty,
        asking_member=member2
    )

    member1.create_question(question1)
    member2.create_question(question2)

    question1.add_bounty(bounty)
    question2.add_bounty(bounty)

    question1.add_comment(Comment(text="This is a comment.", member=member1))
    question2.add_comment(Comment(text="Another comment.", member=member2))

    moderator.close_question(question1, QuestionClosingRemark.DUPLICATE)
    question1.undelete()

    # Creating answers
    answer1 = Answer(answer_text="This is an answer to question 1", member=member1)
    answer2 = Answer(answer_text="This is an answer to question 2", member=member2)

    answer1.increment_vote_count()
    answer2.increment_vote_count()

    question1.answers.append(answer1)
    question2.answers.append(answer2)

    # Admin operations
    admin.block_member(member1)
    admin.unblock_member(member1)

    # Displaying information
    print(f"Member: {member1.get_email()}, Reputation: {member1.get_reputation()}")
    print(f"Member: {member2.get_email()}, Reputation: {member2.get_reputation()}")
    print(f"Question: {question1.title}, Status: {question1.status.name}, Bounty: {question1.bounty.reputation}")
    print(f"Question: {question2.title}, Status: {question2.status.name}, Bounty: {question2.bounty.reputation}")

    # Test searching for questions
    search_result = question1.search("class diagrams")
    if search_result:
        print(f"Search found: {search_result.title}")

if __name__ == "__main__":
    main()
