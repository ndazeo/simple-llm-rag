from typing import Any, Dict, Optional, TypedDict
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import render_text_description

from .get_time import get_time
from .sum import sum

tools = [get_time, sum]
rendered_tools = render_text_description(tools)


class ToolCallRequest(TypedDict):
    """A typed dict that shows the inputs into the invoke_tool function."""

    action: str
    action_input: Dict[str, Any]


def invoke_tool(
    tool_call_request: ToolCallRequest, config: Optional[RunnableConfig] = None
):
    """A function that we can use the perform a tool invocation.

    Args:
        tool_call_request: a dict that contains the keys action and action_input.
            The action must match the name of a tool that exists.
            The action_input are the arguments to that tool.
        config: This is configuration information that LangChain uses that contains
            things like callbacks, metadata, etc.See LCEL documentation about RunnableConfig.

    Returns:
        output from the requested tool
    """
    tool_name_to_tool = {tool.name: tool for tool in tools}
    name = tool_call_request["action"]
    requested_tool = tool_name_to_tool[name]
    if "action_input" not in tool_call_request:
      tool_call_request["action_input"] = {}
    return requested_tool.invoke(tool_call_request["action_input"], config=config)