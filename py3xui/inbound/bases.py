import json

from pydantic import BaseModel, model_validator


class JsonStringModel(BaseModel):
    """
    Base model for Pydantic that validates and converts a JSON string to a dictionary.
    """

    @model_validator(mode="before")
    def model_validate(cls, values):  # pylint: disable=no-self-argument, arguments-differ
        """
        Validates and converts the input values from a JSON string to a dictionary if possible.
        """
        if isinstance(values, str):
            try:
                return json.loads(values)
            except json.JSONDecodeError:
                pass
        return values