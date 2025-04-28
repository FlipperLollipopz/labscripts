# tweak_body.py
from mitmproxy import http

def response(flow: http.HTTPFlow):
    # solo per risposte testuali
    ct = flow.response.headers.get("Content-Type", "")
    if "text" in ct:
        flow.response.text = flow.response.text + "\n, You have been tricked!!!"
