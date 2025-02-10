"""
Base class for models that have a JSON string as a field.
"""

import json

from pydantic import BaseModel, model_validator


class JsonStringModel(BaseModel):
    """
    Base model that can parse JSON strings.
    """

    @model_validator(mode="before")
    def model_validate(
        cls,
        values,  # pylint: disable=no-self-argument, arguments-differ
    ):
        """
        Validate and convert JSON string to dictionary if necessary.

        Returns:
            dict: A dictionary if the input is a valid JSON string, otherwise the original input.
        """
        if isinstance(values, str):
            try:
                return json.loads(values)
            except json.JSONDecodeError:
                pass
        return values