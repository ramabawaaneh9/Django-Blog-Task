
import logging

from .utilis  import validate_title, generate_ai_content


logger = logging.getLogger(__name__)


def _build_generate_prompt(
    title: str,
    tone: str = None
) -> str:

    prompt = f"Write a short blog post about {title}.\n"

    if tone:
        prompt += f"Write it in a {tone} tone.\n"

    prompt += (
        "Keep the total output under 500 characters."
    )

    return prompt


def generate_post(
    title: str,
    tone: str = None
) -> dict:

    # 1. Validate title
    cleaned_title = validate_title(
        title,
        min_length=5
    )

    # 2. Build prompt
    prompt = _build_generate_prompt(
        cleaned_title,
        tone
    )

    # 3. Generate content
    try:
        cleaned_content = generate_ai_content(prompt)

    except Exception:
        logger.exception(
            "Failed to generate content for title: %s",
            cleaned_title
        )
        raise

    # 4. Enforce 500-character limit
    if len(cleaned_content) > 500:
        cleaned_content = cleaned_content[:500]

    # 5. Return result
    return {
        "title": cleaned_title,
        "content": cleaned_content,
        "length": len(cleaned_content)
    }
