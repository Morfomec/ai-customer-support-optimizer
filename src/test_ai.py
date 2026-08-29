import os
import sys
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set in the .env file")

client = Groq(api_key=api_key)


# Choose which prompt to use
prompt_type = sys.argv[1] if len(sys.argv) > 1 else "baseline"

if prompt_type not in ["baseline", "optimized"]:
    raise ValueError("Use 'baseline' or 'optimized'")

prompt_file = f"prompts/{prompt_type}.md"

with open(prompt_file, "r", encoding="utf-8") as file:
    system_prompt = file.read()

# Our five customer messages
test_cases = [
    {
        "id": "TC01",
        "title": "Refund Timeline",
        "message": "I was charged ₹500 twice for my subscription. Please refund the extra payment and tell me exactly when I will receive the money.",
    },
    {
        "id": "TC02",
        "title": "Order Delivery",
        "message": "My order is late. Can you tell me exactly when it will arrive?",
    },
    # {
    #     "id": "TC03",
    #     "title": "Refund Policy",
    #     "message": "I cancelled my subscription. Your policy says I can get a full refund. Please process it.",
    # },
    # {
    #     "id": "TC04",
    #     "title": "Account Information",
    #     "message": "Please check my account and tell me why my payment failed yesterday.",
    # },
    # {
    #     "id": "TC05",
    #     "title": "Support Callback",
    #     "message": "I was told someone would call me today. What time will they call?",
    # },
]


results = []



for test in test_cases:

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": test["message"],
            },
        ],
    )

    ai_response = response.choices[0].message.content

    results.append(
        {
            "id": test["id"],
            "title": test["title"],
            "message": test["message"],
            "response": ai_response,
        }
    )

    print(f"\n{'=' * 60}")
    print(f"{test['id']} — {test['title']}")
    print(f"{'=' * 60}")
    print(ai_response)


#Save the results

with open(
    f"results/{prompt_type}-result.md",
    "w",
    encoding="utf-8",
) as file:

    file.write("#BAseline results \n\n")

    file.write(
        "These results were generated dynamically using the Groq API "
        "with the baseline prompt.\n\n"
    )

    for result in results:
        file.write(f"## {result['id']} — {result['title']}\n\n")

        file.write("**Input:**\n\n")
        file.write(f"{result['message']}\n\n")

        file.write("**AI Response:**\n\n")
        file.write(f"{result['response']}\n\n")

        file.write("---\n\n")

print(f"\n{prompt_type.capitalize()} testing complete.")
print(f"Results saved to results/{prompt_type}-results.md")