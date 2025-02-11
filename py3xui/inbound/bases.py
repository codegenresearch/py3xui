import json

from pydantic import BaseModel, model_validator


class JsonStringModel(BaseModel):
    """
    Base model for Pydantic that validates and converts a JSON string into a dictionary.
    """

    @model_validator(mode="before")
    def model_validate(
        cls,
        values,
    ):  # pylint: disable=no-self-argument, arguments-differ
        """
        Validates and converts a JSON string into a dictionary.
        If parsing fails, the original input is returned.
        """
        if isinstance(values, str):
            try:
                return json.loads(values)
            except json.JSONDecodeError:
                pass
        return values