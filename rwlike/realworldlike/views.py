import json
from django import http
from django.utils import simplejson as json
from django.views.generic.detail import BaseDetailView
from django.views.generic import CreateView

from realworldlike.models import PrintRun, Spot
from realworldlike.forms import PrintRunForm, SpotForm



class PrintRunCreateView(CreateView):
    form_class = PrintRunForm
    model = PrintRun


class PrintRunJSONView(BaseDetailView):
    model = PrintRun

    def render_to_response(self, context):
        print_run = self.object
        poster_ids = list(print_run.poster_set.all().values_list('pk', flat=True))
        if not poster_ids:
            raise http.Http404
        payload = {
            'qr': {
                'left': print_run.design.qr_left,
                'top': print_run.design.qr_top,
                'size': print_run.design.qr_size,
            },
            'campaign': {
                'number': print_run.design.campaign.number,
                'keyword': print_run.design.campaign.keyword,
            },
            'poster_ids': poster_ids,
        }
        return self.get_json_response(self.convert_payload_to_json(payload))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_payload_to_json(self, payload):
        "Convert the payload dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(payload)

class SpotCreateView(CreateView):
    form_class=SpotForm
    model = Spot
