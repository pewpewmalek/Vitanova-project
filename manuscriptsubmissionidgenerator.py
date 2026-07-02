"""
Task 05: Manuscript Submission ID Generator

Objective:
Generate a unique manuscript submission ID.

Format:
VNIAS-YYYY-XXXX-UUID

Example:
VNIAS-2026-0042-a3f9
"""

import uuid

PROJECT_PREFIX = "VNIAS"


def generate_submission_id(year: int, sequence: int) -> str:
    """
    Generate a manuscript submission ID.

    Args:
        year (int): Submission year.
        sequence (int): Sequential submission number.

    Returns:
        str: Submission ID.
    """

    if year < 2000:
        raise ValueError("Invalid year.")

    if sequence <= 0:
        raise ValueError("Sequence must be greater than zero.")

    # First 4 hexadecimal characters from UUID4
    uuid_fragment = uuid.uuid4().hex[:4]

    # Pad sequence with leading zeros
    sequence_str = str(sequence).zfill(4)

    submission_id = (
        f"{PROJECT_PREFIX}-{year}-{sequence_str}-{uuid_fragment}"
    )

    return submission_id


def main():
    print("=" * 50)

    for number in range(1, 6):
        print(generate_submission_id(2026, number))

    print("=" * 50)


if __name__ == "__main__":
    main()