import requests
import json
import time

# --- Configuration ---
GRAPHQL_URL = "http://localhost:8080/graphql"
REST_URL = "http://localhost:8080/api/users"


def tool_call_rest_delete(user_id):
    """Tool: Calls the Spring Boot REST API to delete the user if critical validation fails"""
    if user_id:
        try:
            response = requests.delete(f"{REST_URL}/{user_id}")
            if response.status_code == 204:
                print(f"✅ User with ID {user_id} deleted successfully.")
            else:
                print(f"❌ Failed to delete user with ID {user_id}. Status Code: {response.status_code}")
        except Exception as e:
            print(f"❌ Error during REST call: {str(e)}")


class UserAgentOrchestrator:
    def __init__(self, username, email, phone=None, address=None):
        self.data = {
            "username": username,
            "email": email,
            "phone": phone,
            "address": address
        }
        self.attempts = 0
        self.max_attempts = 3

    def tool_call_graphql(self):
        """Tool: Calls the Spring Boot GraphQL Mutation"""
        query = """
        mutation($u: String!, $e: String!, $p: String, $a: String) {
          createUserWithProfile(username: $u, email: $e, profile: {phoneNumber: $p, address: $a}) {
            id
            username
            profile {
              id
              phoneNumber
              address
            }
          }
        }
        """
        variables = {
            "u": self.data["username"],
            "e": self.data["email"],
            "p": self.data["phone"],
            "a": self.data["address"]
        }

        try:
            response = requests.post(GRAPHQL_URL, json={'query': query, 'variables': variables})
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def agent_corrector(self, missing_fields):
        """Agent B: Repairs specific missing fields identified by the Validator"""
        print(f"🤖 Agent B (Corrector): Fixing specific fields: {missing_fields}")

        if "phone" in missing_fields:
            self.data["phone"] = "999-000-111"
            print("   > Generated Phone Number.")

        if "address" in missing_fields:
            self.data["address"] = "Default AI Assigned Address, Bengaluru"
            print("   > Generated Address.")

        return True

    def run(self):
        """The Orchestrator Logic"""
        while self.attempts < self.max_attempts:
            self.attempts += 1
            print(f"\n--- Cycle {self.attempts} ---")
            print(f"🤖 Agent A (Creator): Sending request for {self.data['username']}...")

            result = self.tool_call_graphql()

            # Validation Logic
            if "error" in result:
                print(f"❌ Connection Error: {result['error']}")
                break

            user_data = result.get('data', {}).get('createUserWithProfile')

            # --- Deep Validation Logic ---
            missing_fields = []

            if not user_data:
                print("⚠️ Critical: No user data returned.")
                break

            profile = user_data.get('profile')
            id = user_data.get('id')

            if profile is None:
                print("⚠️ Validation: Profile object is completely missing.")
                missing_fields = ["phone", "address"]
            else:
                # Check specific fields within the profile
                if not profile.get('phoneNumber'):
                    print("⚠️ Validation: Phone Number is empty.")
                    missing_fields.append("phone")

                if not profile.get('address'):
                    print("⚠️ Validation: Address is empty.")
                    missing_fields.append("address")

            # --- Decision Point ---
            if not missing_fields:
                print("✅ Success! All fields (User + Profile + Detailed Info) are verified.")
                print(json.dumps(result, indent=2))
                return
            else:
                if id:
                    print(f"   > Deleting User ID {id}, created without profile.")
                    tool_call_rest_delete(id)
                # Trigger Agent B with only the missing fields
                self.agent_corrector(missing_fields)
                print("🔄 Re-routing to Agent A for retry...")
                time.sleep(1)

        print("🚫 Agent Orchestrator: Process terminated.")

# --- Execution ---
if __name__ == "__main__":
    # Test Case: Creating a user WITHOUT profile data
    # Agent B should catch this and fix it.
    print("🚀 Starting Multi-Agent Task: Create user 'Singh' with missing profile.")

    orchestrator = UserAgentOrchestrator(
        username="Singh",
        email="singh@example.com",
        phone=None,    # Missing!
        address=None   # Missing!
    )

    orchestrator.run()