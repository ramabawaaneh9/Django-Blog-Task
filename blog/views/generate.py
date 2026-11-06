from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..ai_content.service import generate_post as service_generate_post


@api_view(['POST'])
def generate_post(request):
    title = request.data.get("title", "")
    tone = request.data.get("tone", None)

    try:
        result = service_generate_post(title, tone)
        return Response(result, status=status.HTTP_200_OK)

    except ValueError as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )