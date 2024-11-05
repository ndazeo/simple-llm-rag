#!/usr/bin/env python3
from model import model

if __name__ == "__main__":
    question = "what time is it?"
    print("Question: ", question)
    
    #before = time.time()
    message = model.invoke({"input": question})
    #after = time.time()
    #print("Time: ", after-before)
    print("Answer: ", message)