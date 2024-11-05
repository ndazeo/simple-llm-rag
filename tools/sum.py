from langchain.tools import tool


@tool
def sum(a: int, b: int):
  """Adds two numbers"""
  return a + b