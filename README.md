# A simple example of an LLM that calls external tools

This example chains any LLM to a tool caller. This works by asking the LLM to
not to answer the question but to provide a JSON with the tool that can obtain
the anwser.

## Prequisites

This application needs python3, pip, and the following packages:

1. langchain:

`pip install langchain_community`

2. llama-cpp-python (can be replaced with any other llm)

On CPU:
`pip install llama-cpp-python`

With CUDA support:
`CMAKE_ARGS="-DGGML_CUDA=on" FORCE_CMAKE=1 pip install llama-cpp-python`

## Run

To run the application, just run main.py:

`python3 main.py`

## Next steps

 * Implement a fallback for unknown questions:
    * Tell the LLM to use action: unknown
    * Create a "unknown" tool that returns the same query to give a nice answer in the future
 * "Beautify" answers:
    * Extend the prompt to give a "human" like answer
    * Chain the output appended to the conversation to the LLM again to generate
 * Statefull interaction
    * Add memory to the agent to remember previous interactions
    * This would mean we can follow up questions
 * Implement UI
    * Allow user inputs
    * Show a chat-like application
