"""
This module contains base classes for inbound models, including a model that validates and converts a JSON string into a dictionary.
"""

import json

from pydantic import BaseModel, model_validator


class JsonStringModel(BaseModel):
    """
    Base class for models that have a JSON string as a field.
    Validates and converts a JSON string into a dictionary.
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


I have revised the module-level docstring to reflect that it contains base classes for inbound models. The class docstring has been made more concise and specifies that it is a base class for models with a JSON string as a field. The method docstring has been simplified to focus on the core functionality. The code structure and formatting remain consistent with the provided code snippets.