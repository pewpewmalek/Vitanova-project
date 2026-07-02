from enum import Enum

class ManuscriptStatus(Enum):
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    REVISION_REQUIRED = "revision_required"
    REVISED = "revised"
    ACCEPTED = "accepted"
    IN_PRODUCTION = "in_production"
    PUBLISHED = "published"
    REJECTED = "rejected"

transitions = {
    "submitted": ["under_review"],
    "under_review": ["accepted", "revision_required", "rejected"],
    "revision_required": ["revised"],
    "revised": ["under_review"],
    "accepted": ["in_production"],
    "in_production": ["published"],
    "published": [],
    "rejected": []
}

def can_transition(current: str, next_state: str) -> bool:
    return next_state in transitions.get(current, [])

# Test
print(can_transition("under_review", "accepted")) # True
print(can_transition("submitted", "published")) # False