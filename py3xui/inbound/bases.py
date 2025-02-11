import json

from pydantic import BaseModel, model_validator


class JsonStringModel(BaseModel):
    """
    Base Pydantic model that validates and converts a JSON string to a dictionary.
    If the input is a JSON string, it attempts to parse it into a dictionary.
    If parsing fails, the original input is returned.
    """

    @model_validator(mode="before")
    def model_validate(cls, json_data):  # pylint: disable=no-self-argument, arguments-differ
        """
        Validates and converts the input JSON string to a dictionary.
        If parsing fails, the original input is returned.
        """
        if isinstance(json_data, str):
            try:
                return json.loads(json_data)
            except json.JSONDecodeError:
                pass
        return json_data