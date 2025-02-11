import json

from pydantic import BaseModel, model_validator


class JsonStringModel(BaseModel):
    """
    A Pydantic model that validates and converts a JSON string into a dictionary.
    This model ensures that any string input is parsed into a dictionary if it is a valid JSON.
    If the input is not a valid JSON string, it returns the original input.
    """

    @model_validator(mode="before")
    def model_validate(
        cls,
        values,
    ):  # pylint: disable=no-self-argument, arguments-differ
        """
        Validates and converts a JSON string into a dictionary.
        If the input is a valid JSON string, it returns the parsed dictionary.
        If the input is not a valid JSON string, it returns the original input.
        """
        if isinstance(values, str):
            try:
                return json.loads(values)
            except json.JSONDecodeError:
                pass
        return values