import json

from pydantic import BaseModel, model_validator


class JsonStringModel(BaseModel):
    """
    Pydantic model that validates and converts a JSON string to a dictionary.
    If the input is a JSON string, it attempts to parse it into a dictionary.
    If parsing fails, the original input is returned.
    """

    @model_validator(mode="before")
    def model_validate(cls, values):  # pylint: disable=no-self-argument, arguments-differ
        """
        Validates and converts the input values. If the input is a JSON string, it attempts to parse it into a dictionary.
        If parsing fails, the original input is returned.
        """
        if isinstance(values, str):
            try:
                return json.loads(values)
            except json.JSONDecodeError:
                pass
        return values