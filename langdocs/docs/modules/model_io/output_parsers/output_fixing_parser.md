

# Auto-fixing Parser

The auto-fixing parser is an output parser that can automatically fix errors in language model outputs before parsing. This allows robustly handling potentially malformed outputs.

## Overview

The auto-fixing parser wraps another output parser. If the first parser fails due to incorrectly formatted output from the language model, the auto-fixing parser will call out to another language model to try to fix the errors.

This allows parsing outputs from language models even when they may be malformed. The auto-fixing parser passes the misformatted output and prompt instructions to a second "fixer" language model, asking it to fix any errors so the output can be parsed correctly.

## Usage

The auto-fixing parser is useful when you want to parse structured outputs from language models, but the outputs may sometimes be malformed.

For example, say you want to parse output into a Pydantic model. The Pydantic parser would fail if the output is not valid JSON. 

The auto-fixing parser handles this by taking the Pydantic parser, and another language model as a "fixer" model. If parsing fails with the Pydantic parser, it sends the invalid output to the fixer language model to correct errors. Once fixed, it passes the output back to the Pydantic parser.

Here is an example:

```python
from langchain.output_parsers import PydanticOutputParser, OutputFixingParser  
from langchain.chat_models import ChatOpenAI

# Pydantic parser  
pydantic_parser = PydanticOutputParser(MyPydanticModel)

# Auto-fixing parser with ChatOpenAI as fixer model
fixing_parser = OutputFixingParser.from_llm(
  parser=pydantic_parser,  
  llm=ChatOpenAI()  
)

# If output is invalid, fixing_parser will call ChatOpenAI to fix it
structured_output = fixing_parser.parse(invalid_json_string)
```

The auto-fixing parser allows robustly parsing structured outputs from language models, by automatically handling any malformed outputs before parsing.

