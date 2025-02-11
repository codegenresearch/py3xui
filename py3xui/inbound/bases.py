import json

from pydantic import BaseModel, model_validator


class JsonStringModel(BaseModel):
    """
    A base model for Pydantic that validates and converts a JSON string into a dictionary.
    """

    @model_validator(mode="before")
    def model_validate(
        cls,
        values,
    ):  # pylint: disable=no-self-argument, arguments-differ
        """
        Validates and converts the input values.

        If the input is a JSON string, it attempts to parse it into a dictionary.
        If parsing fails, the original input is returned.

        Args:
            values: The input data to be validated and converted.

        Returns:
            A dictionary if the input was a JSON string and was successfully parsed,
            otherwise the original input values.
        """
        if isinstance(values, str):
            try:
                return json.loads(values)
            except json.JSONDecodeError:
                pass
        return values