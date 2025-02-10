import json

from pydantic import BaseModel, model_validator

class JsonStringModel(BaseModel):
    """
    Base class for Pydantic models that handle a JSON string as a field.
    This model attempts to parse the input into a dictionary if it is a valid JSON string.
    """

    @model_validator(mode="before")
    def model_validate(
        cls,
        values,
    ):  # pylint: disable=no-self-argument, arguments-differ
        """
        Validates and converts the input values. If the input is a JSON string, it attempts to parse it into a dictionary.
        """
        if isinstance(values, str):
            try:
                return json.loads(values)
            except json.JSONDecodeError:
                pass
        return values