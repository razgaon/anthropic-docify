

# Partial Prompt Templates

Partial prompt formatting allows creating a new prompt template by passing a subset of required values to an existing template. This is useful when you want to reuse a template but don't have all the values available at once. 

LangChain supports two methods of partial formatting:

## Partial Formatting with String Values

Partial formatting with strings is useful when you receive some input values earlier in your program than others. For example, suppose you have a prompt template that requires two variables, `foo` and `baz`. If you get the `foo` value early on in the chain, but the `baz` value later, it can be annoying to wait until you have both variables in the same place to pass them to the prompt template. Instead, you can partial the prompt template with the `foo` value, and then pass the partialed prompt template along and just use that.

For example, consider a prompt template that requires `foo` and `baz`:

```python
prompt = PromptTemplate(template="{foo}{baz}", input_variables=["foo", "baz"])
```

If you receive `foo` first but `baz` later, you can create a partial template with just `foo`:

```python
partial_prompt = prompt.partial(foo="hello") 
```

Now `partial_prompt` just needs `baz` to be fully formatted.

You can also initialize a template with partial values:

```python
prompt = PromptTemplate(template="{foo}{baz}", input_variables=["baz"],  
                        partial_variables={"foo": "hello"})
```

## Partial Formatting with Functions  

The other common use is to partial with a function. The use case for this is when you have a variable you know that you always want to fetch in a common way. A prime example of this is with date or time. Imagine you have a prompt which you always want to have the current date. You can't hard code it in the prompt, and passing it along with the other input variables is a bit annoying. In this case, it's very handy to be able to partial the prompt with a function that always returns the current date.

Partial formatting with functions is useful when you want to dynamically generate a value each time the template is formatted. 

For example, to include the current date:

```python
from datetime import datetime

def get_date():
    return datetime.now().strftime("%m/%d/%Y")  

prompt = PromptTemplate(
    template="Today's date is {date}.",
    input_variables=["date"]   
)

partial_prompt = prompt.partial(date=get_date)
```

Now `get_date()` will be called each time `partial_prompt` is formatted. 

You can use functions that take arguments:

```python 
def get_ordinal(num):
    # returns 1st, 2nd etc
    ...
    
prompt = PromptTemplate(
    template="The {num} ordinal is {ordinal}.",
    input_variables=["num", "ordinal"]
)

partial_prompt = prompt.partial(ordinal=get_ordinal) 
```

And functions that return different types like lists:

```python
def get_list():
    return [1, 2, 3]
    
prompt = PromptTemplate(
    template="The list is {mylist}",
    input_variables=["mylist"]  
)

partial_prompt = prompt.partial(mylist=get_list)
```

## When to Use Each Method

- Use string partial formatting when you have some static values available earlier than others. This avoids having to pass them around.

- Use function partial formatting when you want to dynamically generate a value on every format call. This is useful for values that change like date/time. 

- If you have all values available at once, just initialize the template with `partial_variables` instead of using partial formatting.

Splitting the documentation into separate sections on strings and functions improves organization and discoverability.

