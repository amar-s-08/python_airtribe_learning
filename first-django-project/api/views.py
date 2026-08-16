from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

@api_view(["GET"])
def hello(request):
    return Response({
        "message":"Hello from Airtribe"
    })

@api_view(["GET"])
def add_two_numbers(request):
    try:
        a = int(request.query_params.get("a"))
        b = int(request.query_params.get("b"))
    except (TypeError, ValueError):
        return Response(
            {"error": "Both 'a' and 'b' must be valid numbers."},
            status=HTTP_400_BAD_REQUEST,
        )
    return Response({"sum": a + b}, status=HTTP_200_OK)