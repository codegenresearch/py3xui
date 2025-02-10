"""
Provides a base model for handling JSON string fields.
"""

import json
from pydantic import BaseModel, model_validator


class JsonStringModel(BaseModel):
    """
    Base model for JSON string validation and conversion.
    """

    @model_validator(mode="before")
    def model_validate(cls, values):
        """
        Validate and convert JSON string to dictionary.
        """
        if isinstance(values, str):
            try:
                return json.loads(values)
            except json.JSONDecodeError:
                pass
        return values