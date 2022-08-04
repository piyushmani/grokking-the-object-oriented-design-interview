
## Stack Overflow


**Table of Contents**

- [System Requirements](#system-requirements)
- [Use case diagram](#use-case-diagram)
- [Class diagram](#class-diagram)
- [Activity diagrams](#activity-diagrams)
- [Code](#code)

### System Requirements
- Any non-member (guest) can search and view questions. However, to add or upvote a question, they have to become a member.
- Members should be able to post new questions.
- Members should be able to add an answer to an open question.
- Members can add comments to any question or answer.
- A member can upvote a question, answer or comment.
- Members can flag a question, answer or comment, for serious problems or moderator attention.
- Any member can add a bounty to their question to draw attention.
- Members will earn badges for being helpful.
- Members can vote to close a question; Moderators can close or reopen any question.
- Members can add tags to their questions. A tag is a word or phrase that describes the topic of the question.
- Members can vote to delete extremely off-topic or very low-quality questions.
- Moderators can close a question or undelete an already deleted question.
- The system should also be able to identify most frequently used tags in the questions.

### Class diagram
------------
```mermaid
%%{init: { "theme": "neutral"} }%%
classDiagram
    direction RL
    class Answer{
        answerText: string
        accepted: bool
        voteCount: int
        flagCount: int
        create: datetime
        increamentFlagCount()
    }
    class Question{
        title: string
        description: string
        viewCount: int
        voteCount: int
        creationTime: datetime
        update Time: datetime
        status: QuestionStatus
        closingRemark: QuestionClosingRemark
        close()
        undelete()
    }
    class Comment{
        text: string
        creation: datetime
        flagCount: int
        voteCount: int
        incrementVoteCount()
    }
    class Bounty{
        reputation: int
        expiry: dateTime
        modifyReputation()
    }
    class Photo{
        photold: int
        photoPath: string
        creationDate: dateTime
        delete()
    }
    class Notification{
        notificationld: int
        createdOn: date
        content: string
        sendNotification()
    }
    class Account{
        id: string
        password: string
        status: AccountStatus
        name: string
        email: string
        phone: string
        reputation: int
        resetPassword()
    }
    class Tag{
        name: string
        description: string
        dailyAskedFrequency: int
        weeklyAskedFrequency: int
    }
    class Member{
        getReputation()
        getEmail()
        createQuestion()
    }
    class Admin{
        blockMember()
        unblockMember()
    }
    class Moderator{
        closeQuestion()
        undeleteQuestion()
    }
    class Badge{
        name:  string
        description: string
    }
    class Guest {
        registerAccount()
    }
    class search{
        <<interface>>
    }

    Question "1" *-- "*" Answer
    Question "0..1" *-- "*" Comment
    Answer "0..1" *-- "*" Comment
    Question "1" *-- "*" Photo
    Answer "1" *-- "*" Photo
    Question "1" *-- "0..1" Bounty
    Question "*" -- "*" Tag
    Member "1" -- "1" Account
    Member --> Question : ask/close/mark favorite
    Member --> Comment : add/flags
    Member --> Answer : add/flags/create
    Member --> Tag : create
    Member --> Badge : collect
    Admin --|> Member : Extends
    Moderator --|> Member : Extends
    Notification --> Member : for
    Member ..> search : uses
    Guest ..> search : uses
    Question ..|> search 

```

------------
#### Activity diagram Post a new question

```mermaid

%%{init: { "theme": "forest","flowchart": {"nodeSpacing":10, "rankSpacing":20,"curve": "basic","useMaxWidth":true}} }%%
flowchart TD
    A[Start]
    B(Member clicks on the 'Ask Question' button)
    C(Member enters the Title and the Body of the question) 
    D{{Add tag to the question ??}}
    E{{Validate question ?}}
    F{{Does tag exist ?}} 
    G{{Has enougn reputation ?}}
    H(Create tag)
    I{{Tag created successfully? ??}}
    J(Show error to the user)
    K(Save and post the question)
    Z(End)

    A -->B-->C-->D 
    D -->|Yes| F
    D -->|No tags| E
    E --> |validation passed| K
    E --> |validation failed| C
    F --> |Yes| E
    F --> |No | G
    G --> |Yes| H --> I
    G --> |No| J
    I --> |Yes| E
    I --> |No| J
    K-->Z
    J-->Z    
    classDef se fill:#FDFCFC, color:#283747,stroke:#6F6A68,stroke-width:2px
    classDef normal fill:#FDFCFC, color:#283747,stroke:#6F6A68,stroke-width:1px
    classDef question fill:#FDFCFC, color:#283747,stroke:#283747,stroke-width:1.5px,stroke-dasharray:3
    classDef success fill:#FDFCFC, color:#73C6B6,stroke:#283747
    classDef error fill:#FDFCFC, color:#EC7063 ,stroke:#283747
    
    class A,Z se
    class B,C,H,K normal
    class D,F,G,I,E question
    class J error
    class K success
    linkStyle 0,1,2,3,4,5,7,8,9,10,12,14,15 stroke:#6F6A68,stroke-width:1.2px,color:#6F6A68
    linkStyle 6,13,11 stroke:#F3A8A0,stroke-width:1.1px,color:#973126
    
 ```
 
 ### Code
------------
 
 > ***Note => In below code the database implementation and payment implementation are skiped.***
 
 ###### Enums and Constants
 
 ```python
from enum import Enum

class QuestionStatus(Enum):
    OPEN, CLOSED, ON_HOLD, DELETED = 1, 2, 3, 4

class QuestionClosingRemark(Enum):
    DUPLICATE, OFF_TOPIC, TOO_BROAD, NOT_CONSTRUCTIVE, NOT_A_REAL_QUESTION, PRIMARILY_OPINION_BASED = 1, 2, 3, 4, 5, 6

class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5
```

 ###### Account, Member, Admin, and Moderator
 
 ```python
from dataclasses import dataclass

@dataclass
class Account:
    id: str 
    password: str
    name: str 
    email: str
    address: str 
    phone: int
    status : AccountStatus
    reputation : int = 0

    def reset_password(self):
        None

@dataclass
class Member:
    account : Account
    badges : list

    def get_reputation(self):
        return self.__account.get_reputation()

    def get_email(self):
        return self.__account.get_email()

    def create_question(self, question):
        None

    def create_tag(self, tag):
        None

class Admin(Member):
    def block_member(self, member):
        None

    def unblock_member(self, member):
        None

class Moderator(Member):
    def close_question(self, question):
        None

    def undelete_question(self, question):
        None
```

 ###### Badge, Tag, and Notification
 
 ```python
from dataclasses import dataclass,field
import datetime
from abc import ABC, abstractmethod

@dataclass
class Badge:
    name : str
    description : str

@dataclass
class Tag:
    name : str
    description : str
    daily_asked_frequency : int = 0
    weekly_asked_frequency : int = 0

@dataclass
class Notification:
    notification_id : int 
    content : str
    created_on: datetime.datetime = datetime.datetime.now()
 
    def send_notification(self):
        None     
```

 ###### Photo and Bounty
 
 ```python
from dataclasses import dataclass,field
import datetime
from abc import ABC, abstractmethod

@dataclass
class Photo:
    photo_id: int
    photo_path: int
    creating_member = Member
    created_on: datetime.datetime = datetime.datetime.now() 

    def delete(self):
        None
        
@dataclass
class Bounty:
    reputation : int
    expiry: datetime.datetime

    def modify_reputation(self, reputation):
        None
```


 ###### Question, Comment and Answer
 
 ```python
from dataclasses import dataclass,field
import datetime
from abc import ABC, abstractmethod


class Search(ABC):
  def search(self, query):
    None

@dataclass
class Question(Search):
    title: str
    description: str
    bounty: Bounty
    asking_member : Member
    view_count : int = 0
    vote_count : int = 0
    creation_time: datetime.datetime = datetime.datetime.now()
    update_time: datetime.datetime = datetime.datetime.now()
    status: QuestionStatus = QuestionStatus.OPEN
    closing_remark: QuestionClosingRemark = QuestionClosingRemark.DUPLICATE
    photos: list = field(default_factory=list)
    comments: list = field(default_factory=list)
    answers: list = field(default_factory=list)

    def close(self):
        None

    def undelete(self):
        None

    def add_comment(self, comment):
        None

    def add_bounty(self, bounty):
        None

    def search(self, query):
        # return all questions containing the string query in their title or description.
        None

@dataclass
class Comment:
    text: str
    member = Member
    flag_count: int = 0
    vote_count: int = 0
    creation_time:datetime.datetime = datetime.datetime.now()

    def increment_vote_count(self):
        None

@dataclass
class Answer:
    answer_text:str
    member: Member
    accepted: bool = False
    vote_count:int  = 0
    flag_count:int  = 0
    creation_time:datetime.datetime = datetime.datetime.now()
    photos: list = field(default_factory=list)

    def increment_vote_count(self):
        None

```
