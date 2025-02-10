"""
Module for handling JSON string validation in Pydantic models.
"""

from pydantic import BaseModel, model_validator
import json

class JsonStringModel(BaseModel):
    """
    Pydantic model that validates and parses JSON strings.
    """

    @model_validator(mode="before")
    def model_validate(
        cls,
        values,
    ):  # pylint: disable=no-self-argument, arguments-differ
        """
        Validate and convert JSON string to dictionary.
        """
        if isinstance(values, str):
            try:
                return json.loads(values)
            except json.JSONDecodeError:
                pass
        return values