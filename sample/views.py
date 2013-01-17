

import logging
from django.views.generic import View
from django import http


logger = logging.getLogger('Index')
class Index(View):

    def get(self, request, *args, **kwargs):

        logger.error('Some crazy error', exc_info=True, extra={'request': request})

        raise Exception("oops2")

        return http.HttpResponse("hi")
