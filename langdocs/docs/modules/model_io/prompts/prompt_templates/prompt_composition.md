

# Prompt Composition and Templates

## Introduction

Prompt composition and templates are key concepts in LangChain for constructing flexible, reusable prompts to feed to language models. This guide provides an overview of these concepts, best practices, and examples.

## Prompt Composition with PipelinePromptTemplate

The `PipelinePromptTemplate` class allows composing multiple prompt templates together to build complex prompts. This is useful when you want to reuse parts of prompts or implement conditional logic/branching. 

A `PipelinePromptTemplate` consists of:

- **Final prompt**: The final composed prompt template returned.
- **Pipeline prompts**: A list of tuples with a name and prompt template. Each template is formatted and passed to future templates as a variable.

For example:

```python
intro_template = "My name is {name}."
intro_prompt = PromptTemplate.from_template(intro_template)

question_template = "Now you ask me a question: {question}"
question_prompt = PromptTemplate.from_template(question_template)

pipeline_prompts = [
   ("introduction", intro_prompt),
   ("question", question_prompt)
]

final_template = """
{introduction}
{question}
""" 

pipeline_prompt = PipelinePromptTemplate(
   final_prompt=final_prompt,
   pipeline_prompts=pipeline_prompts
)
```

This chains an introduction and a question prompt.

## Prompt Templates

A `PromptTemplate` represents a single parametrized prompt text. You can create one from a template string:

```python
template = "Tell me a {adjective} joke about {content}."
prompt = PromptTemplate.from_template(template) 
```

Or by specifying input variables explicitly:

```python 
prompt = PromptTemplate(
   input_variables=["adjective", "content"],
   template="Tell me a {adjective} joke about {content}."
)
```

You can then format the template to generate prompts.

## Best Practices

- Use `PipelinePromptTemplate` to compose complex prompts from reusable parts 
- Use `PromptTemplate` for single parametrized prompts
- Structure code into pipeline definition and final template definition sections

## Conclusion

In summary, `PipelinePromptTemplate` allows prompt composition while `PromptTemplate` represents single prompts. Use these tools to build modular, reusable prompts for language models.

