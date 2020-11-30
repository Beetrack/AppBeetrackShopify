import datetime
from models.beetrack import BeetrackCredentialsModel
from pkg.commons import fetch_tag
from pkg.beetrack import BeetrackApiHandler
from pkg.shopify import ShopifyApiHandler
import ipdb

class BeetrackToShopify():

    def __init__(self, body):
        self.body = body
        self.status = body.get("status")
        self.order_id = fetch_tag(self.body.get('tags'), "id_order_shopify")
        self.fulfillment_id = fetch_tag(self.body.get('tags'), "id_fulfilled")

    def send_to_shopify(self, account_uuid):
        order_payload = self.homologate_status(account_uuid)
        send_note = ShopifyApiHandler().create_note_order(self.order_id, order_payload)
        return send_note

    def homologate_status(self, account_uuid):
        arrived_at = self.get_time()
        if self.status == 1:
            status = "confirmed"
            get_fulfillment_payload = self.ship_fulfillment_payload(account_uuid)
            send_fulfillmanet = ShopifyApiHandler().create_fulfillment(self.order_id, self.fulfillment_id, get_fulfillment_payload)
            print({"Fulfillment Update Response": send_fulfillmanet})
        elif self.status == 2:
            status = "delivered"
        elif self.status == 3:
            status = "not delivered"
        elif self.status == 4:
            status = "partially delivered"
        get_order_payload = self.note_order_payload(status, arrived_at)
        return get_order_payload

    def get_time(self):
        time_now = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        arrived_at = self.body.get("arrived_at", time_now)
        return arrived_at

    def note_order_payload(self, status, arrived_at):
        payload = {
            "order": {
                "id": int(self.order_id),
                "note": "Beetrack Info: Dispatch {}".format(status),
                "tags": status,
                "note_attributes": [
                    {
                        "name": "Shipping Status",
                        "value": status
                    },
                                {
                        "name": "Event Time",
                        "value": arrived_at
                    }
                ]
            }
        }
        print(payload)
        return payload

    def ship_fulfillment_payload (self, account_uuid):
        identifier = self.body.get("identifier")
        beetrack_credential_obj = BeetrackCredentialsModel.find_by_uuid(account_uuid) # revisar
        api_key = beetrack_credential_obj.get("api_ke")
        get_dispatch = BeetrackApiHandler(api_key).get_dispatch(identifier)
        beecode = get_dispatch.get("response").get("beecode")
        payload = {
            "fulfillment": {
                "id": self.fulfillment_id,
                "tracking_number": "https://app.beetrack.com/track/{}".format(beecode),
                "tracking_url": "https://app.beetrack.com/track/{}".format(beecode),
                "shipment_status": self.status,
                "notify_customer": "true",
                "tracking_company": "Beetrack"
            }
        }
        print(payload)
        return payload