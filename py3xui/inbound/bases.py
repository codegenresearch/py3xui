"""
Provides base classes for inbound models that include JSON string fields.
"""

from pydantic import BaseModel, model_validator
import json

class JsonStringModel(BaseModel):
    """
    Base class for models that have a JSON string as a field.
    This class ensures that JSON strings are properly validated and converted to dictionaries.
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