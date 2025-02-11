import json

from pydantic import BaseModel, model_validator


class JsonStringModel(BaseModel):
    """
    A Pydantic model that validates and converts a JSON string to a dictionary.
    """

    @model_validator(mode="before")
    def model_validate(
        cls,
        values,
    ):  # pylint: disable=no-self-argument, arguments-differ
        """
        Validates and converts the input values. If the input is a JSON string, it attempts to parse it into a dictionary.
        If parsing fails, it returns the original values.

        :param values: The input values to be validated and converted.
        :return: A dictionary if the input was a valid JSON string, otherwise the original values.
        """
        if isinstance(values, str):
            try:
                return json.loads(values)
            except json.JSONDecodeError:
                pass
        return values