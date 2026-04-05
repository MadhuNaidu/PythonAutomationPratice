"""
API: Application Programming Interface,
it will be useful to communicate with diff software componets
Soap vs Rest:
Soap:  Simple object access protocol, stateless or statefull
it will dealing with xml files, it will allow WSDL ( web service description language )
protocals: http, smtp, tcp, udp

Rest API: Representional state transfer
HTTP / HTTPS: - GET / POST / PATCH / PUT / DELETE
json/xml/html/text
stateless apis

auth: Oauth, Oauth2, Basic, JWT
API Endpoint:
Path params:
Query params:
Headers:
Payload:
Statu codes:


dict datatype:

1. Fetch all the user ids where price is greater than 600
2. Fetch all the user details where type is men
3. Fetch all the user details where category is dress


"""
import pytest

"""
Status codes: 
1xx: Information related
2xx: Successful status codes
    200: OK
    
3xx: Redirect status codes
4xx: Client error status codes
    400: Bad request
    401: Unauthorized
    403: Forbidden
    404: Not Found
5xx: Server error status codes

GET: It will retrive the data from the endpoint, 
once it is success we can see 200 status code

POST: We can use to create a new resource in the entity, we can send the payload
Once it is success we can see the 201 status code, created

PATCH: We can modify particular attribute and value ex: {'password': 'msn321'}
    we can modify existing resource by sending partial payload

PUT: It will replace existing resource by sending entire payload.
if resource is not there it will create new resource in the entity.

DELETE: Deletes existing resource 
"""
"""
authenication:Verifies user credentials / token it means you are the authencated user
401 unauthorized
authrozation: it will check the permissions, role based access controal (rbac), 403 - forbidden
"""

"""
Path Parameters vs Query Parameters:
path parameters we can use to create url, 
it of part url, to fetch particular record from the resource
Query params we can use after ? in url, to filter, sort or pagination we can use
"""
"""
Request Headers: We can use to send any api auth, content-type details

Payload: it will be used in post call to create the resource, in json data
"""

# by using requests module we can automate api

import requests

# print(dir(requests))

class TestProduct:

    def test_product_list(self):
        resp = requests.get("https://automationexercise.com/api/productsList")
        print(resp.status_code)
        assert resp.status_code == 200, "get api is failed"
        resp = resp.json()
        print(resp.keys())
        # print(resp["products"])
        product_list = []
        for product in resp["products"]:
            print(product["name"])
            product_list.append(product['name'])
        assert "Summer white Top" in product_list, "Item is not there in product list"

    @pytest.mark.post
    def test_search_product(self):
        # url, headers, data/payload
        payload = {'search_product': 'top'}
        resp = requests.post("https://automationexercise.com/api/searchProduct", data=payload)
        print(resp.status_code)
        resp = resp.json()
        for product in resp["products"]:
            print(product["category"]["category"])
            print(product["category"]["usertype"])