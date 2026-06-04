import json
import os

from google import genai
from google.genai import types

SYSTEM_INSTRUCTION = """You are a brand extraction assistant analyzing AI-generated text responses.

Given a text and a monitored brand name, you must:
1. Determine if the monitored brand is mentioned in the text — including sub-brands and product lines that clearly belong to it (e.g. "Nubank Ultravioleta" counts as a mention of "Nubank")
2. Extract all OTHER company and brand names mentioned in the text

Brand extraction rules:
- Extract company/brand names only — not product lines, model descriptors, or feature names
- From "New Balance Fresh Foam X 1080 v14" extract "New Balance", not "Fresh Foam"
- From "Asics Gel-Excite 10" extract "Asics", not "Gel-Excite"
- From "Mizuno Wave Rider 29" extract "Mizuno", not "Wave Rider"
- From "BTG Pactual Black" extract "BTG Pactual", not "Black"
- Do NOT include the monitored brand or any of its sub-brands/variants in other_brands
- Use the most canonical form of each brand name (e.g. "Banco Inter" → "Inter")

Return ONLY a valid JSON object with this exact structure:
{
  "own_brand_mentioned": <boolean>,
  "other_brands": [<string>, ...]
}"""


def analyze(texto: str, marca_monitorada: str) -> dict:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY not set. Copy .env.example to .env and add your key."
        )

    client = genai.Client(api_key=api_key)
    prompt = f"Monitored brand: {marca_monitorada}\n\nText:\n{texto}"

    last_error = None
    for attempt in range(2):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                response_mime_type="application/json",
            ),
        )
        try:
            result = json.loads(response.text)
            if "own_brand_mentioned" not in result or "other_brands" not in result:
                raise ValueError(f"Missing fields in response: {result}")
            return result
        except (json.JSONDecodeError, ValueError) as e:
            last_error = e

    raise RuntimeError(f"Failed to parse LLM response after 2 attempts: {last_error}")
