import requests
from langchain_core.tools import tool

@tool
def create_user_api(username: str, email: str, phone_number: str = None, address: str = None):
    """
    Call this tool to create a new user and their profile in the system.
    If phone or address are missing, the system might create a null profile.
    """
    url = "http://localhost:8080/graphql"
    query = """
    mutation($u: String!, $e: String!, $p: String, $a: String) {
      createUserWithProfile(username: $u, email: $e, profile: {phoneNumber: $p, address: $a}) {
        id
        username
        profile { phoneNumber address }
      }
    }
    """
    variables = {"u": username, "e": email, "p": phone_number, "a": address}
    try:
        response = requests.post(url, json={'query': query, 'variables': variables})
        return response.json()
    except Exception as e:
        return f"Error connecting to backend: {str(e)}"

from langchain_groq import ChatGroq

groq_api_key = "<groq_api_key>"
llm = ChatGroq(api_key=groq_api_key, model="llama-3.1-8b-instant", temperature=0)
# Bind the tool to the LLM
tools = [create_user_api]
llm_with_tools = llm.bind_tools(tools)



from langchain_core.messages import HumanMessage, ToolMessage

def run_agentic_workflow(user_prompt):
    messages = [HumanMessage(content=user_prompt)]

    # 1. AI decides to call the tool
    ai_msg = llm_with_tools.invoke(messages)
    messages.append(ai_msg)

    for tool_call in ai_msg.tool_calls:
        # Execute the actual function
        result = create_user_api.invoke(tool_call["args"])
        print(f"🛠️ API Result: {result}")

        # Check if profile is missing in the result
        user_info = result.get('data', {}).get('createUserWithProfile', {})

        if user_info and user_info.get('profile').get('phoneNumber') is None or user_info.get('profile').get('address') is None:
            print("⚠️ Profile data is missing! Asking AI to correct...")

            # 2. Add the 'failure' to memory and let AI reason
            messages.append(ToolMessage(tool_call_id=tool_call["id"], content=str(result)))
            messages.append(HumanMessage(content="The profile was created as null. Please generate a dummy phoneNumber and address and try again."))

            # AI now reasons: "Oh, it's null. I should provide a phone number."
            final_response = llm_with_tools.invoke(messages)
            print(f"🧠 AI Correction Thought: {final_response.tool_calls[0]['args']}")

            # Execute the corrected call
            corrected_result = create_user_api.invoke(final_response.tool_calls[0]["args"])
            print(f"✅ Final Result: {corrected_result}")

run_agentic_workflow("Create a user for AI with email ai@example.com")