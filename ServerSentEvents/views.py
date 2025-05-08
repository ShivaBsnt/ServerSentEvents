import time

from django.http import StreamingHttpResponse
from django.shortcuts import render


def sse_view(request):
    def event_stream():
        while True:
            time.sleep(1)
            message = f"data: Server time is {time.strftime('%H:%M:%S')}\n\n"
            yield message
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


def index(request):
    return render(request, 'index.html')