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
    "x-forwarded-for": "104.196.146.40",
    "x-forwarded-proto": "https",
    "x-forwarded-port": "443",
    "host": "c3173cae7300aa5864da751d2ce20d1d.m.pipedream.net",
    "x-amzn-trace-id": "Root=1-5fbc10e7-3f5f6d9717d5ea651c771323",
    "content-length": "6710",
    "user-agent": "Shopify-Captain-Hook",
    "accept": "*/*",
    "accept-encoding": "gzip;q=1.0,deflate;q=0.6,identity;q=0.3",
    "content-type": "application/json",
    "x-shopify-api-version": "2020-10",
    "x-shopify-hmac-sha256": "ASXd30XBXjfje3skWzkFmtU7v/w1at6OVc2UqaNOjrE=",
    "x-shopify-order-id": "3076878401734",
    "x-shopify-shop-domain": "test-beetrack-shop.myshopify.com",
    "x-shopify-test": "False",
    "x-shopify-topic": "orders/fulfilled"
  },
  "bodyRaw": "{\"id\":3076878401734,\"email\":\"email@email.com\",\"closed_at\":\"2020-11-23T14:43:20-05:00\",\"created_at\":\"2020-11-23T14:41:57-05:00\",\"updated_at\":\"2020-11-23T14:43:20-05:00\",\"number\":3,\"note\":\"\",\"token\":\"e3608a44212442b64b4a7478254be7ed\",\"gateway\":\"manual\",\"test\":False,\"total_price\":\"2380\",\"subtotal_price\":\"2000\",\"total_weight\":200,\"total_tax\":\"380\",\"taxes_included\":False,\"currency\":\"CLP\",\"financial_status\":\"paid\",\"confirmed\":True,\"total_discounts\":\"0\",\"total_line_items_price\":\"2000\",\"cart_token\":null,\"buyer_accepts_marketing\":False,\"name\":\"#1003\",\"referring_site\":null,\"landing_site\":null,\"cancelled_at\":null,\"cancel_reason\":null,\"total_price_usd\":\"3.11\",\"checkout_token\":null,\"reference\":null,\"user_id\":67468394694,\"location_id\":null,\"source_identifier\":null,\"source_url\":null,\"processed_at\":\"2020-11-23T14:41:57-05:00\",\"device_id\":null,\"phone\":null,\"customer_locale\":\"en\",\"app_id\":1354745,\"browser_ip\":null,\"landing_site_ref\":null,\"order_number\":1003,\"discount_applications\":[],\"discount_codes\":[],\"note_attributes\":[],\"payment_gateway_names\":[\"manual\"],\"processing_method\":\"manual\",\"checkout_id\":null,\"source_name\":\"shopify_draft_order\",\"fulfillment_status\":\"fulfilled\",\"tax_lines\":[{\"price\":\"380\",\"rate\":0.19,\"title\":\"VAT\",\"price_set\":{\"shop_money\":{\"amount\":\"380\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"380\",\"currency_code\":\"CLP\"}}}],\"tags\":\"Beetrack\",\"contact_email\":\"email@email.com\",\"order_status_url\":\"https:\\/\\/test-beetrack-shop.myshopify.com\\/51526041798\\/orders\\/e3608a44212442b64b4a7478254be7ed\\/authenticate?key=7fabfa242f85ea1281b5c415aab97367\",\"presentment_currency\":\"CLP\",\"total_line_items_price_set\":{\"shop_money\":{\"amount\":\"2000\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"2000\",\"currency_code\":\"CLP\"}},\"total_discounts_set\":{\"shop_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"}},\"total_shipping_price_set\":{\"shop_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"}},\"subtotal_price_set\":{\"shop_money\":{\"amount\":\"2000\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"2000\",\"currency_code\":\"CLP\"}},\"total_price_set\":{\"shop_money\":{\"amount\":\"2380\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"2380\",\"currency_code\":\"CLP\"}},\"total_tax_set\":{\"shop_money\":{\"amount\":\"380\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"380\",\"currency_code\":\"CLP\"}},\"line_items\":[{\"id\":8894418354374,\"variant_id\":37639502069958,\"title\":\"Banana\",\"quantity\":1,\"sku\":\"02\",\"variant_title\":null,\"vendor\":\"Test Beetrack Shop\",\"fulfillment_service\":\"manual\",\"product_id\":6104659034310,\"requires_shipping\":True,\"taxable\":True,\"gift_card\":False,\"name\":\"Banana\",\"variant_inventory_management\":\"shopify\",\"properties\":[],\"product_exists\":True,\"fulfillable_quantity\":0,\"grams\":200,\"price\":\"2000\",\"total_discount\":\"0\",\"fulfillment_status\":\"fulfilled\",\"price_set\":{\"shop_money\":{\"amount\":\"2000\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"2000\",\"currency_code\":\"CLP\"}},\"total_discount_set\":{\"shop_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"}},\"discount_allocations\":[],\"duties\":[],\"admin_graphql_api_id\":\"gid:\\/\\/shopify\\/LineItem\\/8894418354374\",\"tax_lines\":[{\"title\":\"VAT\",\"price\":\"380\",\"rate\":0.19,\"price_set\":{\"shop_money\":{\"amount\":\"380\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"380\",\"currency_code\":\"CLP\"}}}]}],\"fulfillments\":[{\"id\":2882652963014,\"order_id\":3076878401734,\"status\":\"success\",\"created_at\":\"2020-11-23T14:43:19-05:00\",\"service\":\"manual\",\"updated_at\":\"2020-11-23T14:43:19-05:00\",\"tracking_company\":null,\"shipment_status\":null,\"location_id\":57954697414,\"line_items\":[{\"id\":8894418354374,\"variant_id\":37639502069958,\"title\":\"Banana\",\"quantity\":1,\"sku\":\"02\",\"variant_title\":null,\"vendor\":\"Test Beetrack Shop\",\"fulfillment_service\":\"manual\",\"product_id\":6104659034310,\"requires_shipping\":True,\"taxable\":True,\"gift_card\":False,\"name\":\"Banana\",\"variant_inventory_management\":\"shopify\",\"properties\":[],\"product_exists\":True,\"fulfillable_quantity\":0,\"grams\":200,\"price\":\"2000\",\"total_discount\":\"0\",\"fulfillment_status\":\"fulfilled\",\"price_set\":{\"shop_money\":{\"amount\":\"2000\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"2000\",\"currency_code\":\"CLP\"}},\"total_discount_set\":{\"shop_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"}},\"discount_allocations\":[],\"duties\":[],\"admin_graphql_api_id\":\"gid:\\/\\/shopify\\/LineItem\\/8894418354374\",\"tax_lines\":[{\"title\":\"VAT\",\"price\":\"380\",\"rate\":0.19,\"price_set\":{\"shop_money\":{\"amount\":\"380\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"380\",\"currency_code\":\"CLP\"}}}]}],\"tracking_number\":null,\"tracking_numbers\":[],\"tracking_url\":null,\"tracking_urls\":[],\"receipt\":{},\"name\":\"#1003.1\",\"admin_graphql_api_id\":\"gid:\\/\\/shopify\\/Fulfillment\\/2882652963014\"}],\"refunds\":[],\"total_tip_received\":\"0.0\",\"original_total_duties_set\":null,\"current_total_duties_set\":null,\"admin_graphql_api_id\":\"gid:\\/\\/shopify\\/Order\\/3076878401734\",\"shipping_lines\":[],\"billing_address\":{\"first_name\":\"Agustin\",\"address1\":\"Las Pircas\",\"phone\":\"56482486\",\"city\":\"Santiago\",\"zip\":\"7690000\",\"province\":\"Santiago\",\"country\":\"Chile\",\"last_name\":\"Di Prospero\",\"address2\":\"01\",\"company\":\"Beetrack\",\"latitude\":null,\"longitude\":null,\"name\":\"Agustin Di Prospero\",\"country_code\":\"CL\",\"province_code\":\"RM\"},\"shipping_address\":{\"first_name\":\"Agustin\",\"address1\":\"Las Pircas\",\"phone\":\"56482486\",\"city\":\"Santiago\",\"zip\":\"7690000\",\"province\":\"Santiago\",\"country\":\"Chile\",\"last_name\":\"Di Prospero\",\"address2\":\"01\",\"company\":\"Beetrack\",\"latitude\":null,\"longitude\":null,\"name\":\"Agustin Di Prospero\",\"country_code\":\"CL\",\"province_code\":\"RM\"},\"customer\":{\"id\":4464336437446,\"email\":\"email@email.com\",\"accepts_marketing\":False,\"created_at\":\"2020-11-23T11:07:48-05:00\",\"updated_at\":\"2020-11-23T14:41:57-05:00\",\"first_name\":\"Agustin\",\"last_name\":\"Di Prospero\",\"orders_count\":2,\"state\":\"disabled\",\"total_spent\":\"7140.00\",\"last_order_id\":3076878401734,\"note\":null,\"verified_email\":True,\"multipass_identifier\":null,\"tax_exempt\":False,\"phone\":null,\"tags\":\"\",\"last_order_name\":\"#1003\",\"currency\":\"CLP\",\"accepts_marketing_updated_at\":\"2020-11-23T11:07:48-05:00\",\"marketing_opt_in_level\":null,\"admin_graphql_api_id\":\"gid:\\/\\/shopify\\/Customer\\/4464336437446\",\"default_address\":{\"id\":5467322843334,\"customer_id\":4464336437446,\"first_name\":\"Agustin\",\"last_name\":\"Di Prospero\",\"company\":\"Beetrack\",\"address1\":\"Las Pircas\",\"address2\":\"01\",\"city\":\"Santiago\",\"province\":\"Santiago\",\"country\":\"Chile\",\"zip\":\"7690000\",\"phone\":\"56482486\",\"name\":\"Agustin Di Prospero\",\"province_code\":\"RM\",\"country_code\":\"CL\",\"country_name\":\"Chile\",\"default\":True}}}",
  "body": {
    "id": 3076878401734,
    "email": "email@email.com",
    "closed_at": "2020-11-23T14:43:20-05:00",
    "created_at": "2020-11-23T14:41:57-05:00",
    "updated_at": "2020-11-23T14:43:20-05:00",
    "number": 3,
    "note": "",
    "token": "e3608a44212442b64b4a7478254be7ed",
    "gateway": "manual",
    "test": False,
    "total_price": "2380",
    "subtotal_price": "2000",
    "total_weight": 200,
    "total_tax": "380",
    "taxes_included": False,
    "currency": "CLP",
    "financial_status": "paid",
    "confirmed": True,
    "total_discounts": "0",
    "total_line_items_price": "2000",
    "buyer_accepts_marketing": False,
    "name": "#1003",
    "total_price_usd": "3.11",
    "user_id": 67468394694,
    "processed_at": "2020-11-23T14:41:57-05:00",
    "customer_locale": "en",
    "app_id": 1354745,
    "order_number": 1003,
    "discount_applications": [],
    "discount_codes": [],
    "note_attributes": [],
    "payment_gateway_names": [
      "manual"
    ],
    "processing_method": "manual",
    "source_name": "shopify_draft_order",
    "fulfillment_status": "fulfilled",
    "tax_lines": [
      {
        "price": "380",
        "rate": 0.19,
        "title": "VAT",
        "price_set": {
          "shop_money": {
            "amount": "380",
            "currency_code": "CLP"
          },
          "presentment_money": {
            "amount": "380",
            "currency_code": "CLP"
          }
        }
      }
    ],
    "tags": "Beetrack",
    "contact_email": "email@email.com",
    "order_status_url": "https://test-beetrack-shop.myshopify.com/51526041798/orders/e3608a44212442b64b4a7478254be7ed/authenticate?key=7fabfa242f85ea1281b5c415aab97367",
    "presentment_currency": "CLP",
    "total_line_items_price_set": {
      "shop_money": {
        "amount": "2000",
        "currency_code": "CLP"
      },
      "presentment_money": {
        "amount": "2000",
        "currency_code": "CLP"
      }
    },
    "total_discounts_set": {
      "shop_money": {
        "amount": "0",
        "currency_code": "CLP"
      },
      "presentment_money": {
        "amount": "0",
        "currency_code": "CLP"
      }
    },
    "total_shipping_price_set": {
      "shop_money": {
        "amount": "0",
        "currency_code": "CLP"
      },
      "presentment_money": {
        "amount": "0",
        "currency_code": "CLP"
      }
    },
    "subtotal_price_set": {
      "shop_money": {
        "amount": "2000",
        "currency_code": "CLP"
      },
      "presentment_money": {
        "amount": "2000",
        "currency_code": "CLP"
      }
    },
    "total_price_set": {
      "shop_money": {
        "amount": "2380",
        "currency_code": "CLP"
      },
      "presentment_money": {
        "amount": "2380",
        "currency_code": "CLP"
      }
    },
    "total_tax_set": {
      "shop_money": {
        "amount": "380",
        "currency_code": "CLP"
      },
      "presentment_money": {
        "amount": "380",
        "currency_code": "CLP"
      }
    },
    "line_items": [
      {
        "id": 8894418354374,
        "variant_id": 37639502069958,
        "title": "Banana",
        "quantity": 1,
        "sku": "02",
        "vendor": "Test Beetrack Shop",
        "fulfillment_service": "manual",
        "product_id": 6104659034310,
        "requires_shipping": True,
        "taxable": True,
        "gift_card": False,
        "name": "Banana",
        "variant_inventory_management": "shopify",
        "properties": [],
        "product_exists": True,
        "fulfillable_quantity": 0,
        "grams": 200,
        "price": "2000",
        "total_discount": "0",
        "fulfillment_status": "fulfilled",
        "price_set": {
          "shop_money": {
            "amount": "2000",
            "currency_code": "CLP"
          },
          "presentment_money": {
            "amount": "2000",
            "currency_code": "CLP"
          }
        },
        "total_discount_set": {
          "shop_money": {
            "amount": "0",
            "currency_code": "CLP"
          },
          "presentment_money": {
            "amount": "0",
            "currency_code": "CLP"
          }
        },
        "discount_allocations": [],
        "duties": [],
        "admin_graphql_api_id": "gid://shopify/LineItem/8894418354374",
        "tax_lines": [
          {
            "title": "VAT",
            "price": "380",
            "rate": 0.19,
            "price_set": {
              "shop_money": {
                "amount": "380",
                "currency_code": "CLP"
              },
              "presentment_money": {
                "amount": "380",
                "currency_code": "CLP"
              }
            }
          }
        ]
      }
    ],
    "fulfillments": [
      {
        "id": 2882652963014,
        "order_id": 3076878401734,
        "status": "success",
        "created_at": "2020-11-23T14:43:19-05:00",
        "service": "manual",
        "updated_at": "2020-11-23T14:43:19-05:00",
        "location_id": 57954697414,
        "line_items": [
          {
            "id": 8894418354374,
            "variant_id": 37639502069958,
            "title": "Banana",
            "quantity": 1,
            "sku": "02",
            "vendor": "Test Beetrack Shop",
            "fulfillment_service": "manual",
            "product_id": 6104659034310,
            "requires_shipping": True,
            "taxable": True,
            "gift_card": False,
            "name": "Banana",
            "variant_inventory_management": "shopify",
            "properties": [],
            "product_exists": True,
            "fulfillable_quantity": 0,
            "grams": 200,
            "price": "2000",
            "total_discount": "0",
            "fulfillment_status": "fulfilled",
            "price_set": {
              "shop_money": {
                "amount": "2000",
                "currency_code": "CLP"
              },
              "presentment_money": {
                "amount": "2000",
                "currency_code": "CLP"
              }
            },
            "total_discount_set": {
              "shop_money": {
                "amount": "0",
                "currency_code": "CLP"
              },
              "presentment_money": {
                "amount": "0",
                "currency_code": "CLP"
              }
            },
            "discount_allocations": [],
            "duties": [],
            "admin_graphql_api_id": "gid://shopify/LineItem/8894418354374",
            "tax_lines": [
              {
                "title": "VAT",
                "price": "380",
                "rate": 0.19,
                "price_set": {
                  "shop_money": {
                    "amount": "380",
                    "currency_code": "CLP"
                  },
                  "presentment_money": {
                    "amount": "380",
                    "currency_code": "CLP"
                  }
                }
              }
            ]
          }
        ],
        "tracking_numbers": [],
        "tracking_urls": [],
        "receipt": {},
        "name": "#1003.1",
        "admin_graphql_api_id": "gid://shopify/Fulfillment/2882652963014"
      }
    ],
    "refunds": [],
    "total_tip_received": "0.0",
    "admin_graphql_api_id": "gid://shopify/Order/3076878401734",
    "shipping_lines": [],
    "billing_address": {
      "first_name": "Agustin",
      "address1": "Las Pircas",
      "phone": "56482486",
      "city": "Santiago",
      "zip": "7690000",
      "province": "Santiago",
      "country": "Chile",
      "last_name": "Di Prospero",
      "address2": "01",
      "company": "Beetrack",
      "name": "Agustin Di Prospero",
      "country_code": "CL",
      "province_code": "RM"
    },
    "shipping_address": {
      "first_name": "Agustin",
      "address1": "Las Pircas",
      "phone": "56482486",
      "city": "Santiago",
      "zip": "7690000",
      "province": "Santiago",
      "country": "Chile",
      "last_name": "Di Prospero",
      "address2": "01",
      "company": "Beetrack",
      "name": "Agustin Di Prospero",
      "country_code": "CL",
      "province_code": "RM"
    },
    "customer": {
      "id": 4464336437446,
      "email": "email@email.com",
      "accepts_marketing": False,
      "created_at": "2020-11-23T11:07:48-05:00",
      "updated_at": "2020-11-23T14:41:57-05:00",
      "first_name": "Agustin",
      "last_name": "Di Prospero",
      "orders_count": 2,
      "state": "disabled",
      "total_spent": "7140.00",
      "last_order_id": 3076878401734,
      "verified_email": True,
      "tax_exempt": False,
      "tags": "",
      "last_order_name": "#1003",
      "currency": "CLP",
      "accepts_marketing_updated_at": "2020-11-23T11:07:48-05:00",
      "admin_graphql_api_id": "gid://shopify/Customer/4464336437446",
      "default_address": {
        "id": 5467322843334,
        "customer_id": 4464336437446,
        "first_name": "Agustin",
        "last_name": "Di Prospero",
        "company": "Beetrack",
        "address1": "Las Pircas",
        "address2": "01",
        "city": "Santiago",
        "province": "Santiago",
        "country": "Chile",
        "zip": "7690000",
        "phone": "56482486",
        "name": "Agustin Di Prospero",
        "province_code": "RM",
        "country_code": "CL",
        "country_name": "Chile",
        "default": True
      }
    }
  }
}

def integrate(event):
  domain = event.get("headers").get("x-shopify-shop-domain")
  user_uuid = event.get("headers").get("user_uuid")
  body = event.get("body") # Solo para ambiente de prueba

  if domain:
    
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