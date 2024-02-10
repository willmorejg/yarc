import requests

class RequestsWrapper():
    """Wrapper for requests module
    """
    
    def __init__(self):
        """constructor
        """
        pass

    def process_response(self, response):
        """process response

        Args:
            response (requests.Response): response object
        """
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get(self, url: str, headers: dict, timeout: int):
        """get request

        Args:
            url (str): url for request
            headers (dict): headers for request
            timeout (int): time out setting for request
        """
        try:
            return requests.get(url, headers=headers, timeout=timeout)
        except requests.exceptions.RequestException as e:
            print(e)
            return None
    
    def post(self, url: str, headers: dict, timeout: int, *args, **kwargs):
        """post request

        Args:
            url (str): url for request
            headers (dict): headers for request
            timeout (int): time out setting for request
            data (dict): data to post
        """
        try:
            return requests.post(url, headers=headers, timeout=timeout, *args, **kwargs)
        except requests.exceptions.RequestException as e:
            print(e)
            return None
