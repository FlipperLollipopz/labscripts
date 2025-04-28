from mitmproxy import http

def response(flow: http.HTTPFlow):
    ct = flow.response.headers.get("Content-Type", "")
    if "text" in ct:
        flow.response.text = flow.response.text + ", You have been tricked!!!"
