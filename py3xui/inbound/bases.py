import json

from pydantic import BaseModel, model_validator

class JsonStringModel(BaseModel):
    """
    A Pydantic model that validates and converts a JSON string into a dictionary.
    """

    @model_validator(mode="before")
    def model_validate(
        cls,
        values,
    ):  # pylint: disable=no-self-argument, arguments-differ
        """
        Validates and converts a JSON string into a dictionary.

        :param values: The input values to be validated and converted.
        :return: A dictionary if the input was a valid JSON string, otherwise the original values.
        """
        if isinstance(values, str):
            try:
                return json.loads(values)
            except json.JSONDecodeError:
                pass
        return values