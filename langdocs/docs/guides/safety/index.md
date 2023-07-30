

Preventing Harmful Language Model Outputs
=========================================

Using large language models comes with the risk that they may generate harmful, dangerous, or unethical text. Mitigating these risks is an active area of research and a key priority for developing safe AI systems. LangChain provides built-in tools to help make language models safer, but carefully evaluating outputs and tuning safety systems is critical.

Introduction
------------
Language models have shown impressive capabilities, but also have concerning failures like generating racist, violent, or otherwise unethical text. Developers using LangChain need to be aware of these risks and incorporate tools to detect and handle unsafe outputs. This page overviews LangChain's safety capabilities and best practices for evaluation.

Moderation Chains
-----------------
Moderation chains like OpenAIModerationChain explicitly check if text contains harmful content using services like OpenAI's moderation API. They can be appended to language model chains using SequentialChain to sanitize outputs:

```python
from langchain.chains import SequentialChain, LLMChain, OpenAIModerationChain

mod_chain = OpenAIModerationChain()
llm_chain = LLMChain(...)

chain = SequentialChain(chains=[llm_chain, mod_chain]) 
```

Moderation chains allow flexibly handling unsafe outputs by returning a string, throwing an error, etc. They provide a first line of defense against dangerous content.

Constitutional Chains
---------------------
Constitutional chains like ConstitutionalChain prompt the model with principles to guide its behavior. For example:

```python 
from langchain.chains.constitutional_ai import ConstitutionalChain

principles = ConstitutionalChain.get_principles(["illegal"])
chain = ConstitutionalChain(llm=..., principles=principles)
```

This critiques and updates responses that violate the principles, filtering unethical outputs. Constitutional chains have built-in principles like avoiding illegal content. The UnifiedObjectives can also correct ethical issues.

Evaluation Best Practices
-------------------------
Moderation and constitutional chains help mitigate risks, but evaluating outputs and tuning safety tools is critical. Best practices include:

- Spot checking samples of model outputs for safety issues 
- Using a diverse evaluation set covering different demographics
- Tuning tools like moderation thresholds and principles 
- Monitoring outputs when deployed in applications
- Having human oversight for policy violations

Careful evaluation and iteration helps build robust safety practices when working with language models. Constitutional and moderation chains provide helpful mechanisms, but responsible oversight is essential.

Conclusion
----------
LangChain provides helpful built-in tools for mitigating risks from language models. However, developing truly safe systems requires extensive evaluation and tuning. We encourage users to carefully assess outputs and incorporate human oversight when possible. There are still open challenges, but progress is being made toward reliable and ethical AI.

