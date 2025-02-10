"""
Provides a Pydantic model for validating JSON string fields.
"""

from pydantic import BaseModel, model_validator
import json

class JsonStringModel(BaseModel):
    """
    Base Pydantic model for validating and parsing JSON string fields.
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