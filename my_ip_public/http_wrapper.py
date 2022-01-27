from http import client

def fetch(hostname, http_path):
    try:
        connection = client.HTTPSConnection(hostname, timeout=5)
    except Exception as connect_error:
        return False, 'could not connect to {}:{}'.format(hostname, connect_error)

    try:
        connection.request('GET', http_path)
        response = connection.getresponse()
    except Exception as get_response_error:
        return False, 'could get response from {}{}:{}'.format(hostname, http_path, get_response_error)

    http_status_code = response.status
    contents = response.read()
    if http_status_code is 200:
        return True, contents
    reason = 'got status code {}'.format(http_status_code)
    if len(contents) > 0:
        reason += ' and response {!r}'.format(contents)
    return False, reason
