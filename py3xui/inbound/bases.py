import json

from pydantic import BaseModel, model_validator


class JsonStringModel(BaseModel):
    """
    Base Pydantic model for handling JSON string fields.
    Ensures that any string input is parsed into a dictionary if it is valid JSON.
    If the input is not valid JSON, it returns the original input.
    """

    @model_validator(mode="before")
    def model_validate(
        cls,
        values,
    ):  # pylint: disable=no-self-argument, arguments-differ
        """
        Validates and converts a JSON string into a dictionary.
        Returns the original input if the string is not valid JSON.
        """
        if isinstance(values, str):
            try:
                return json.loads(values)
            except json.JSONDecodeError:
                pass
        return values