"""
Base classes for inbound models with JSON string fields.
"""

import json
from pydantic import BaseModel, model_validator


class JsonStringModel(BaseModel):
    """
    Base class for models that include a JSON string field.
    Validates and converts JSON strings to dictionaries.
    """

    @model_validator(mode="before")
    def model_validate(
        cls,
        values,
    ):  # pylint: disable=no-self-argument, arguments-differ
        """
        Validate and convert JSON string to dictionary.
        If the input is a JSON string, it attempts to parse it.
        If parsing fails, it returns the original value.
        """
        if isinstance(values, str):
            try:
                return json.loads(values)
            except json.JSONDecodeError:
                pass
        return values