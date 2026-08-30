from typing import Optional

from pydantic import (
    BaseModel,
    Field
)


class PersonInformation(
    BaseModel
):
    """
    Schema for information extracted
    from unstructured text.
    """

    name: Optional[str] = Field(
        default=None,
        description=(
            "Full name of the person. "
            "Return null if not mentioned."
        )
    )


    age: Optional[int] = Field(
        default=None,
        ge=0,
        le=150,
        description=(
            "Age of the person. "
            "Return null if not mentioned."
        )
    )


    email: Optional[str] = Field(
        default=None,
        description=(
            "Email address of the person. "
            "Return null if not mentioned."
        )
    )


    phone: Optional[str] = Field(
        default=None,
        description=(
            "Phone number of the person. "
            "Return null if not mentioned."
        )
    )


    location: Optional[str] = Field(
        default=None,
        description=(
            "Current city, state, or country "
            "where the person lives. "
            "Return null if not mentioned."
        )
    )


    occupation: Optional[str] = Field(
        default=None,
        description=(
            "Current occupation, job role, "
            "or profession. "
            "Return null if not mentioned."
        )
    )


    skills: list[str] = Field(
        default_factory=list,
        description=(
            "List of technical, professional, "
            "or other relevant skills."
        )
    )


    education: list[str] = Field(
        default_factory=list,
        description=(
            "Educational qualifications, "
            "courses, degrees, or institutions."
        )
    )


    organizations: list[str] = Field(
        default_factory=list,
        description=(
            "Companies, universities, or "
            "organizations mentioned."
        )
    )


    important_dates: list[str] = Field(
        default_factory=list,
        description=(
            "Important dates mentioned in the text."
        )
    )


    summary: str = Field(
        description=(
            "A concise summary of the "
            "extracted information."
        ),
        min_length=1,
        max_length=500
    )