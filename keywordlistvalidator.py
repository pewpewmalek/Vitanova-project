"""
Task 04: Keyword List Validator

Objective:
Validate manuscript keywords according to journal rules.

Rules:
- 4 to 6 keywords
- Remove extra spaces
- Convert to lowercase
- Remove duplicates
"""

MIN_KEYWORDS = 4
MAX_KEYWORDS = 6


def validate_keywords(keywords: list[str]) -> dict:
    """
    Validate manuscript keywords.

    Args:
        keywords (list[str]): List of keywords.

    Returns:
        dict: Validation result.
    """

    if not isinstance(keywords, list):
        raise TypeError("Keywords must be a list.")

    cleaned_keywords = []

    for keyword in keywords:

        if not isinstance(keyword, str):
            continue

        keyword = keyword.strip().lower()

        if keyword and keyword not in cleaned_keywords:
            cleaned_keywords.append(keyword)

    result = {
        "valid": False,
        "keywords": cleaned_keywords,
        "errors": []
    }

    count = len(cleaned_keywords)

    if count < MIN_KEYWORDS:
        result["errors"].append(
            f"At least {MIN_KEYWORDS} keywords are required."
        )

    if count > MAX_KEYWORDS:
        result["errors"].append(
            f"No more than {MAX_KEYWORDS} keywords are allowed."
        )

    result["valid"] = len(result["errors"]) == 0

    return result


def main():

    test_cases = [

        [
            "AI",
            "Machine Learning",
            " Agriculture ",
            "Deep Learning",
            "AI",
            "Data Science",
        ],

        [
            "Python",
            "AI",
        ],

        [
            "AI",
            "ML",
            "Data",
            "Cloud",
            "IoT",
            "Security",
            "Networks",
        ],

        [
            " NLP ",
            "Artificial Intelligence",
            "Machine Learning",
            "Computer Vision",
        ],
    ]

    print("=" * 60)

    for index, keywords in enumerate(test_cases, start=1):

        print(f"Test Case {index}")

        result = validate_keywords(keywords)

        print("Valid    :", result["valid"])
        print("Keywords :", result["keywords"])

        if result["errors"]:
            print("Errors:")
            for error in result["errors"]:
                print("-", error)

        print("-" * 60)


if __name__ == "__main__":
    main()