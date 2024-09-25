# This is an example settings file.
# To make changes, copy this into your user directory and remove the .example extension

settings():
    user.model_temperature = 0.2

    # Works with any API with the same schema as OpenAI's (i.e. Azure, llamafiles, etc.)
    # user.model_endpoint = "https://api.openai.com/v1/chat/completions"
    user.model_system_prompt = "You are an assistant helping a developer in an fMRI research lab to be more productive. Output just the response to the request and no additional content. Do not repeat or paraphrase the request. Do not summarize anything at the end or otherwise output any redundant info. If code is requested, do not generate any comments or markdown formatting such as backticks, unless explicitly requested to do so."

    # Change to 'gpt-4' or the model of your choice
    user.openai_model = "gpt-4o"

# Only uncomment the line below if you want experimental behavior to parse Talon files
# tag(): user.gpt_beta

# Use codeium instead of Github Copilot
# tag(): user.codeium
