import json

from pydantic import BaseModel, model_validator


class JsonStringModel(BaseModel):
    """
    Base model for parsing JSON strings into dictionaries.
    """

    @model_validator(mode="before")
    def model_validate(
        cls,
        values,
    ):  # pylint: disable=no-self-argument, arguments-differ
        """
        Validate and convert JSON string to dictionary.

        Args:
            values: The input data to be validated and converted.

        Returns:
            A dictionary if the input is a valid JSON string, otherwise the original input.
        """
        if isinstance(values, str):
            try:
                return json.loads(values)
            except json.JSONDecodeError:
                pass
        return values