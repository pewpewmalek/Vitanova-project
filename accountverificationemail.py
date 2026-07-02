"""
Task 03: Account Verification Email

Objective:
Generate an account verification email.
"""

from email.message import EmailMessage


def create_verification_email(
    recipient: str,
    username: str,
    verification_link: str,
) -> EmailMessage:
    """
    Create account verification email.

    Args:
        recipient (str): Recipient email.
        username (str): User name.
        verification_link (str): Verification URL.

    Returns:
        EmailMessage: Ready email object.
    """

    message = EmailMessage()

    message["Subject"] = "Verify Your VNIAS Account"
    message["From"] = "no-reply@vnias.org"
    message["To"] = recipient

    message.set_content(
        f"""
Hello {username},

Welcome to VNIAS!

Please verify your account by clicking the link below:

{verification_link}

If you did not create this account, please ignore this email.

Regards,
VNIAS Team
"""
    )

    return message


def main():

    email = create_verification_email(
        recipient="ahmed@example.com",
        username="Ahmed Ali",
        verification_link=(
            "https://vnias.org/verify?token=abc123"
        ),
    )

    print("=" * 60)
    print(email)
    print("=" * 60)


if __name__ == "__main__":
    main()