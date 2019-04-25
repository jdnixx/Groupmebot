

def parse_response_from_json(r):
    response = ''
    try:
        response = r.json()['response']
    except Exception as ex:
        response = str(ex)
    return response
