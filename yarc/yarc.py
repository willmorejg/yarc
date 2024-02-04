"""Main Module"""
from typing import Protocol
from abc import ABC
import requests
import json

class YarcEndpointInterface(Protocol):
    """Yet Another REST Client Endpoint Interface

    Args:
        Protocol (_type_): _description_
    """
class YarcEndpoint(ABC, YarcEndpointInterface):
    """Yet Another REST Client Endpoint
    
    Abstract Class for REST Client Endpoints

    Args:
        ABC (_type_): _description_
        YarcEndpointInterface (_type_): _description_
    """
    __headers = {'content-type': 'application/json', 'accept': 'application/json'}
    """default JSON headers
    """
    __timeout = 10
    """default time out setting
    """
    
    def __init__(self, base_url: str, path: str, headers: dict = __headers, timeout: int = __timeout):
        """constructor

        Args:
            base_url (str): base URL for the endpoint (e.g. http://localhost:8080)
            path (str): path for the endpoint (e.g. /api/v1)
            headers (dict, optional): headers used in call to endpoint. Defaults to __headers.
            timeout (int, optional): time out setting for endpoint. Defaults to __timeout.
        """
        self.base_url = base_url
        self.path = path
        self.headers = headers
        self.timeout = timeout
class YarcEndpointFactory():
    """Yet Another REST Client Endpoint Factory
    """

    def __init__(self):
        """constructor
        """
        self.__endpoints = {}
    
    def add_endpoint(self, name: str, endpoint: YarcEndpoint):
        """add an endpoint to the factory

        Args:
            name (str): name of the endpoint
            endpoint (YarcEndpoint): endpoint object
        """
        self.__endpoints[name] = endpoint
    
    def process(self, name:str, *args, **kwargs):
        """process (call) an endpoint using the name assigned to the endpoint

        Args:
            name (str): endpoint name to process
        """
        do = f"{name}"
        if name in self.__endpoints and hasattr(self.__endpoints[do], do) and callable(func := getattr(self.__endpoints[do], do)):
            return func(*args, **kwargs)
        
        print(f"Name '{do}' not found or not callable.")
        return None

class ExampleEndpoint(YarcEndpoint):
    """Example endpoint for Yarc

    Args:
        YarcEndpoint (YarcEndpoint): abstract class for REST client endpoints
    """
    def get_contacts(self, *args, **kwargs):
        """get contacts from endpoint
        """
        response = requests.get(f"{self.base_url}{self.path}", headers=self.headers, timeout=self.timeout)
        return response.json()

    def post_contacts(self, values_dict: dict, *args, **kwargs):
        """post (save) contact to endpoint
        """
        print(values_dict)
        response = requests.post(f"{self.base_url}{self.path}", headers=self.headers, timeout=self.timeout, data=json.dumps(values_dict))
        return response.json()

if __name__ == '__main__':
    yarc_factory = YarcEndpointFactory()
    
    yarc = ExampleEndpoint('http://localhost:9987', '/api/contacts')
    yarc_factory.add_endpoint('get_contacts', yarc)
    yarc_factory.add_endpoint('post_contacts', yarc)

    names = yarc_factory.process('get_contacts')
    print(names[0])

    values_dict={'givenName': 'Edgardo', 'middleName': 'Sonya', 'surname': 'Zemlak'}
    names = yarc_factory.process('post_contacts', values_dict=values_dict)
    print(names)
    