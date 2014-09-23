import json
from django.http import HttpResponse
from rest_framework.views import APIView


class ReportingHandler(APIView):
    """ API for dumping json logs from Arbiter games' clients.
    """

    def post(self, request):
        response = {'test': 'tesing value'}
        return HttpResponse(json.dumps(response), content_type="application/json")
