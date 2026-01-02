import ollama

# --------------------------------------------------------------------------------------------------------#
# ------------------------------------------Main Program Logic--------------------------------------------#
# --------------------------------------------------------------------------------------------------------#

model = "qwen2.5:7b"

def user_prompt_stream(prompt):
    messages = [
        {"role": "system", "content": "You are my personal assistant"},
        {"role": "user", "content": prompt},]
    for chunk in ollama.chat(model=model, messages=messages, stream=True):
        # chunk["message"]["content"] is the newest partial text
        yield chunk["message"]["content"]