import json
from django.http import HttpResponse
from rest_framework.views import APIView

from logs.models import Entry
from logs.utils import Logger
logger = Logger()


class ReportingHandler(APIView):
    """ API for dumping json logs from Arbiter games' clients.
    """

    def post(self, request):
        data = request.DATA.get('data', None)
        try:
            Entry.objects.create(data=data)
            return HttpResponse(json.dumps({'success': True}), content_type="application/json")
        except Exception as err:
            logger.debug(err)
            return HttpResponse(json.dumps({'success': False}), content_type="application/json")
