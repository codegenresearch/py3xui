import json

from pydantic import BaseModel, model_validator

class JsonStringModel(BaseModel):
    """\n    A Pydantic model that validates and processes input to ensure it is a valid JSON string.\n    If the input is a string, it attempts to parse it as JSON.\n    If parsing fails, the original input is returned.\n    """

    @model_validator(mode="before")
    def model_validate(
        cls,
        values,
    ):  # pylint: disable=no-self-argument, arguments-differ
        """\n        Validates and processes the input values.\n\n        :param values: The input values to be validated and processed.\n        :return: The parsed JSON if the input is a valid JSON string, otherwise the original input.\n        """
        if isinstance(values, str):
            try:
                return json.loads(values)
            except json.JSONDecodeError:
                pass
        return values