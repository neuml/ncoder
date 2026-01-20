"""
NCoder module
"""

import os

from IPython.core.magic import Magics, magics_class, line_cell_magic
from IPython.display import clear_output

from openai import OpenAI


@magics_class
class NCoder(Magics):
    """
    Defines a magic function that calls a LLM API service and updates the current cell
    with the result.
    """

    def __init__(self, shell):
        # Call parent constructor
        super().__init__(shell)

        self.client = OpenAI(
            base_url=os.environ.get("OPENAI_BASE_URL", "http://localhost:8000/v1"),
            api_key=os.environ.get("OPENAI_API_KEY", "sk-ncoder")
        )

        self.prompt = (
            "{request}\n\n"
            "Just answer the request without any additional explanations around it. "
            "Don't wrap as Markdown, only write the code. Add comments to code as needed."
        )

    @line_cell_magic
    def ncoder(self, line, cell=None):
        """
        Main method that generates code.

        Args:
            line: input line
            cell: input cell, if any
        """

        request = line
        if cell:
            request += f"\n{cell}"

        # Run request
        response = self.client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": self.prompt.format(request=request),
            }],
            model=os.environ.get("API_MODEL", "ncoder"),
        )

        # Get code
        code = response.choices[0].message.content

        # Include the request in the input
        code = f"%%ncoder {line}\n\n{code}"

        # Add the code cell
        self.shell.set_next_input(code, replace=True)

        # Clear the debugging output
        clear_output()
