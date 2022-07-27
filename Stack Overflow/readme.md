
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
from dataclasses import dataclass
```
