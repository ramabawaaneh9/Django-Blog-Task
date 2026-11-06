
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..ai_content.service.summarize import (
    summarize_post,
    PostNotFoundError,
)


@api_view(['POST'])
def summarize_post_view(request, post_id):

    try:
        result = summarize_post(post_id)

        return Response(
            result,
            status=status.HTTP_200_OK
        )

    except PostNotFoundError as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_404_NOT_FOUND
        )

    except ValueError as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )
