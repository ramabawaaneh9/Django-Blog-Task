
from ...models import Post
from ..claint  import ContentClient


class PostNotFoundError(ValueError):
    pass


def _build_summary_prompt(content):
    return (
        "Summarize the following blog post clearly "
        "in no more than 500 characters. "
        "Keep only the most important ideas.\n\n"
        f"Blog post:\n{content}"
    )


def summarize_post(post_id):

    # 1. Validate the post ID
    if (
        not isinstance(post_id, int)
        or isinstance(post_id, bool)
        or post_id <= 0
    ):
        raise ValueError(
            "Post ID must be a positive integer."
        )

    # 2. Retrieve the post
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise PostNotFoundError("Post not found.")

    # 3. Validate content
    content = (post.content or "").strip()

    if not content:
        raise ValueError(
            "Post content cannot be empty."
        )

    # 4. Build prompt
    prompt = _build_summary_prompt(content)

    # 5. Call the shared client
    client = ContentClient()
    summary = client.generate(prompt)

    # 6. Clean the AI response
    summary = (summary or "").strip()

    if not summary:
        raise ValueError(
            "AI returned an empty summary."
        )

    # 7. Enforce character limit
    summary = summary[:500]

    # 8. Return Python dictionary
    return {
        "post_id": post.pk,
        "title": post.title,
        "summary": summary,
        "length": len(summary)
    }
