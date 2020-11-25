import ipdb

class ShopifyWebhookHandler():

    def __init__(self):
        pass

    def check_for_beetrack_tag(self, body):
        tags = body.get("tags")
        tags_lower = tags.lower()
        if "beetrack" in tags_lower:
            return True
        else:
            return False

    def check_for_fulfilled_order(self, body):
        fulfillment_status = body.get("fulfillment_status")
        if fulfillment_status == "fulfilled":
            return True
        else: 
            return False

    def get_shopify_costumer_info(self, body):
        # Manejar el error si es que la shipping_address no se encuentra en el webhook
        ipdb.set_trace()
        shopify_order_number = body.get("order_number")
        shipping_address = body.get("shipping_address")
        shopify_address = "{}, {}, {}, {}".format(
            shipping_address.get("address1"),
            shipping_address.get("city"),
            shipping_address.get("province"),
            shipping_address.get("country")
        )
        shopify_costumer_name = shipping_address.get("name")
        shopify_costumer_phone = shipping_address.get("phone")
        shoppify_costumer_email = shipping_address.get("email")
        id_order_shopify = body.get("id")
        id_fulfilled = body.get("fulfillments")[0].get("id")
        return shopify_order_number, shopify_costumer_name, shopify_address, shopify_costumer_phone, shoppify_costumer_email, id_order_shopify, id_fulfilled

    def get_shopify_items(self, body):
        items_array = []
        items = body.get("line_items")
        for item in items:
            new_item = {
                "code": item.get("id"),
                "description": item.get("title"),
                "quantity": item.get("quantity")
                }
            items_array.append(new_item)
        return items_array
        