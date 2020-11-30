import requests, json
from pkg.beetrack import BeetrackApiHandler
from flask_sqlalchemy import SQLAlchemy
from models.shopify import ShopifyCredentialsModel
import ipdb

class ShopifyToBeetrack():

    def __init__(self, body):
        self.body = body

    def create_shopify_dispatch(self, beetrack_credentials):
        beetrack_api_key = beetrack_credentials["api_key"]
        payload = self.create_dispatch_payload()
        create = BeetrackApiHandler(beetrack_api_key).create_dispatch(payload)

        return create

    def create_dispatch_payload(self):
        costumer_info = self.get_shopify_costumer_info()
        ipdb.set_trace()
        new_dispatch = {
                "identifier": costumer_info[0],
                "contact_name": costumer_info[1],
                "contact_address": costumer_info[2],
                "contact_phone": costumer_info[3],
                "contact_email": costumer_info[4],
                "items": self.get_shopify_items(),
                "tags": [
                    {"name" :"id_order_shopify",
                    "value": costumer_info[5]}, 
                    {"name": "id_fulfilled",
                    "value": costumer_info[6]}
                    ]
                }
        return new_dispatch


    def check_for_beetrack_tag(self):
        tags = self.body.get("tags")
        tags_lower = tags.lower()
        if "beetrack" in tags_lower:
            return True
        else:
            return False

    def check_for_fulfilled_and_paid_order(self):
        financial_status = self.body.get("financial_status")
        fulfillment_status = self.body.get("fulfillment_status")
        if fulfillment_status == "fulfilled" and financial_status == "paid":
            return True
        else: 
            return False

    def get_shopify_costumer_info(self):
        # Manejar el error si es que la shipping_address no se encuentra en el webhook
        shopify_order_number = self.body.get("order_number")
        shipping_address = self.body.get("shipping_address")
        shopify_costumer_address = "{}, {}, {}, {}".format(
            shipping_address.get("address1"),
            shipping_address.get("city"),
            shipping_address.get("province"),
            shipping_address.get("country")
        )
        shopify_costumer_name = shipping_address.get("name")
        shopify_costumer_phone = shipping_address.get("phone")
        shoppify_costumer_email = shipping_address.get("email")
        id_order_shopify = self.body.get("id")
        id_fulfilled = self.body.get("fulfillments")[0].get("id")
        return shopify_order_number, shopify_costumer_name, shopify_costumer_address, shopify_costumer_phone, shoppify_costumer_email, id_order_shopify, id_fulfilled

    def get_shopify_items(self):
        items_array = []
        items = self.body.get("line_items")
        for item in items:
            new_item = {
                "code": item.get("id"),
                "description": item.get("title"),
                "quantity": item.get("quantity")
                }
            items_array.append(new_item)
        return items_array