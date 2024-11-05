from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import LlamaCpp
from tools import tools, rendered_tools, invoke_tool

## Local LLM
llm_model = "llama-2-7b-ft-instruct-es.Q3_K_S.gguf"

def load_model():
    llm = LlamaCpp(
        model_path=llm_model,
        n_gpu_layers=-1,
        n_batch=512,
        verbose=False,
    )
    return llm

llm = load_model()


system_prompt = f"""\
Answer the following questions as best you can. You have access to the following tools:

{tools}

The way you use the tools is by specifying a json blob named $JSON_BLOB.

Specifically, this json should have a `action` key (with the name of the tool to use) and a `action_input` key (with the input to the tool going here).

The only values that should be in the "action" field are: {[t.name for t in tools]}

The $JSON_BLOB variable should only contain a SINGLE action, do NOT return a list of multiple actions. 

Here is an example of a valid $JSON_BLOB:

```

{{{{

  "action": $TOOL_NAME,

  "action_input": $INPUT

}}}}

```

Example:
Question: what is 2 + 2?
Callback: {{{{ "action": "sum", "action_input": {{{{ "a": 2, "b": 2 }}}} }}}}
END.
"""

prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt), ("user", "Question: {input} \n Callback: ")]
)


model = prompt | llm.bind(stop=['END.']) | JsonOutputParser() | invoke_tool