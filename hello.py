from litellm import completion
from config import PROVIDER_MODEL as MODEL

resp = completion(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are concise."},
        {"role": "user", "content": "Say Hello"}
    ],
    max_tokens=1000,
)
print("REPLY:", resp.choices[0].message["content"])
print("USAGE:", getattr(resp, "usage", {}))