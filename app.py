import os
import litellm
from litellm import completion
from halo import Halo
import dotenv

dotenv.load_dotenv()

## set ENV variables
# os.environ["OPENAI_API_KEY"] = "your-openai-key"
# os.environ["ANTHROPIC_API_KEY"] = "your-openai-key"

# Initialize spinner to show while waiting for response
def custom_callback(
    kwargs,                 # kwargs to completion
    completion_response,    # response from completion
    start_time, end_time    # start/end time
):
    # Your custom code here
    print("LITELLM: in custom callback function")
    # print("kwargs", kwargs)
    print("completion_response", completion_response)
    print("start_time", start_time)
    print("end_time", end_time)

# set callbacks
litellm.success_callback = [custom_callback]

spinner = Halo(text='Loading...', spinner='dots')
spinner.start()

messages = [
    {"role": "user", "content": "What is yoru name?"},
    {"role": "system", "content": "You are an AI assistant tasked to provide short answers with simple language."}
    ]

# call llm
response = completion(
    model="claude-3-opus-20240229", 
    messages=messages,
    temperature=0.5)

# Stop the spinner after getting response
spinner.stop()

# print(response)
print(f"{response.choices[0].message.role}: {response.choices[0].message.content}")