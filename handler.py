from pkg.shopify_to_beetrack import ShopifyToBeetrack
from pkg.beetrack_to_shopify import BeetrackToShopify
import datetime
import json, requests
import ipdb

evento = {
  "method": "POST",
  "path": "/",
  "query": {},
  "headers": {
    "x-forwarded-for": "52.12.104.177",
    "x-forwarded-proto": "https",
    "x-forwarded-port": "443",
    "host": "f737d42c3038cdd800bb1b6fd7e18d7f.m.pipedream.net",
    "x-amzn-trace-id": "Root=1-5fbe9f22-663e4708521447397fbd576e",
    "content-length": "842",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "user-agent": "rest-client/2.0.2 (linux-gnu x86_64) ruby/2.4.5p335",
    "content-type": "application/json",
    "user_uuid": "0dd84b3c-7de0-4cdd-9109-48c330a9ffcd",
    "x-newrelic-id": "UwQBWVVaGwQGXFFaBgU=",
    "x-newrelic-transaction": "PxQFUFIACQoJAVYEA1ACU1cDFB8EBw8RVU4aUAkMVwMKXFxWV1VSV1EFBUNKQQ9RVlZUAFZSFTs="
  },
  "bodyRaw": "{\"resource\":\"dispatch\",\"event\":\"update\",\"account_name\":\"Test Interno (Agustin Di Prospero)\",\"account_id\":2575,\"guide\":\"1002\",\"identifier\":\"1002\",\"route_id\":null,\"dispatch_id\":180901960,\"truck_identifier\":null,\"status\":2,\"substatus\":null,\"substatus_code\":null,\"estimated_at\":null,\"contact_identifier\":null,\"contact_phone\":\"56482486\",\"contact_name\":\"Agustin Di Prospero\",\"contact_email\":null,\"contact_address\":\"Las Pircas, Santiago, Santiago, Chile\",\"tags\":[{\"name\":\"id_fulfilled\",\"value\":\"2882125496518\"},{\"name\":\"id_order_shopify\",\"value\":\"3076447011014\"}],\"is_pickup\":false,\"is_trunk\":false,\"locked\":false,\"items\":[{\"id\":288939481,\"name\":\"Banana\",\"description\":\"Banana\",\"quantity\":2,\"original_quantity\":2,\"delivered_quantity\":2,\"code\":\"8893307093190\",\"extras\":[]}],\"groups\":[],\"arrived_at\":\"2020-11-25 15:13:48-0300\",\"evaluation_answers\":[]}",
  "body": {
    "resource": "dispatch",
    "event": "update",
    "account_name": "Test Interno (Agustin Di Prospero)",
    "account_id": 2575,
    "guide": "1002",
    "identifier": "1002",
    "dispatch_id": 180901960,
    "status": 1,
    "contact_phone": "56482486",
    "contact_name": "Agustin Di Prospero",
    "contact_address": "Las Pircas, Santiago, Santiago, Chile",
    "tags": [
      {
        "name": "id_fulfilled",
        "value": "2882125496518"
      },
      {
        "name": "id_order_shopify",
        "value": "3076447011014"
      }
    ],
    "is_pickup": False,
    "is_trunk": False,
    "locked": False,
    "items": [
      {
        "id": 288939481,
        "name": "Banana",
        "description": "Banana",
        "quantity": 2,
        "original_quantity": 2,
        "delivered_quantity": 2,
        "code": "8893307093190",
        "extras": []
      }
    ],
    "groups": [],
    "arrived_at": "2020-11-25 15:13:48-0300",
    "evaluation_answers": []
  }
}

def integrate(event):
  domain = event.get("headers").get("x-shopify-shop-domain")
  user_uuid = event.get("headers").get("user_uuid")
  body = event.get("body") # Solo para ambiente de prueba

  if domain:
    #prueba push
    
    shopify_fulfilled_and_paid = ShopifyToBeetrack(body).check_for_fulfilled_and_paid_order()
    beetrack_tagged = ShopifyToBeetrack(body).check_for_beetrack_tag()

    if shopify_fulfilled_and_paid == True and beetrack_tagged == True:
        beetrack_credentials = requests.get("http://localhost:5000/shopify_credentials/" + str(domain)).json()
        creating_shopify_dispatch = ShopifyToBeetrack(body).create_shopify_dispatch(beetrack_credentials)
        print("Response guide creation: ",creating_shopify_dispatch) # Reparar print.

  elif user_uuid:
    resource = body.get("resource")
    event = body.get("event")
    if resource == "dispatch" and event == "update":
        beetrack_to_shopify = BeetrackToShopify(body).send_to_shopify(user_uuid)
        print(beetrack_to_shopify)

  else:
    print("Webhook doesn't belong")



integrate(evento)