from pkg.shopify_webhook import ShopifyWebhookHandler
from pkg.shopify_handler import create_shopify_dispatch
import json, requests
import ipdb

evento = {
  "method": "POST",
  "path": "/",
  "query": {},
  "headers": {
    "x-forwarded-for": "35.190.140.166",
    "x-forwarded-proto": "https",
    "x-forwarded-port": "443",
    "host": "c3173cae7300aa5864da751d2ce20d1d.m.pipedream.net",
    "x-amzn-trace-id": "Root=1-5fbbde89-0627b05517bec0842c51bb1a",
    "content-length": "6742",
    "user-agent": "Shopify-Captain-Hook",
    "accept": "*/*",
    "accept-encoding": "gzip;q=1.0,deflate;q=0.6,identity;q=0.3",
    "content-type": "application/json",
    "x-shopify-api-version": "2020-10",
    "x-shopify-hmac-sha256": "JPbFsi0LuVdjLnTv9W74+8vkUJTteVrv+i8eqDzK0iI=",
    "x-shopify-order-id": "3076447011014",
    "x-shopify-shop-domain": "test-beetrack-shop.myshopify.com",
    "x-shopify-test": "false",
    "x-shopify-topic": "orders/fulfilled"
  },
  "bodyRaw": "{\"id\":3076447011014,\"email\":\"email@email.com\",\"closed_at\":\"2020-11-23T11:08:27-05:00\",\"created_at\":\"2020-11-23T11:08:10-05:00\",\"updated_at\":\"2020-11-23T11:08:27-05:00\",\"number\":2,\"note\":\"Hola Agustin\",\"token\":\"58d5120a95b84b0407f08e9d4c29f0b4\",\"gateway\":\"manual\",\"test\":false,\"total_price\":\"4760\",\"subtotal_price\":\"4000\",\"total_weight\":400,\"total_tax\":\"760\",\"taxes_included\":false,\"currency\":\"CLP\",\"financial_status\":\"paid\",\"confirmed\":true,\"total_discounts\":\"0\",\"total_line_items_price\":\"4000\",\"cart_token\":null,\"buyer_accepts_marketing\":false,\"name\":\"#1002\",\"referring_site\":null,\"landing_site\":null,\"cancelled_at\":null,\"cancel_reason\":null,\"total_price_usd\":\"6.23\",\"checkout_token\":null,\"reference\":null,\"user_id\":67468394694,\"location_id\":null,\"source_identifier\":null,\"source_url\":null,\"processed_at\":\"2020-11-23T11:08:10-05:00\",\"device_id\":null,\"phone\":null,\"customer_locale\":\"en\",\"app_id\":1354745,\"browser_ip\":null,\"client_details\":{},\"landing_site_ref\":null,\"order_number\":1002,\"discount_applications\":[],\"discount_codes\":[],\"note_attributes\":[],\"payment_gateway_names\":[\"manual\"],\"processing_method\":\"manual\",\"checkout_id\":null,\"source_name\":\"shopify_draft_order\",\"fulfillment_status\":\"fulfilled\",\"tax_lines\":[{\"price\":\"760\",\"rate\":0.19,\"title\":\"VAT\",\"price_set\":{\"shop_money\":{\"amount\":\"760\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"760\",\"currency_code\":\"CLP\"}}}],\"tags\":\"Beetrack\",\"contact_email\":\"email@email.com\",\"order_status_url\":\"https:\\/\\/test-beetrack-shop.myshopify.com\\/51526041798\\/orders\\/58d5120a95b84b0407f08e9d4c29f0b4\\/authenticate?key=e01ad1b4884154474e9cc6ec60755401\",\"presentment_currency\":\"CLP\",\"total_line_items_price_set\":{\"shop_money\":{\"amount\":\"4000\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"4000\",\"currency_code\":\"CLP\"}},\"total_discounts_set\":{\"shop_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"}},\"total_shipping_price_set\":{\"shop_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"}},\"subtotal_price_set\":{\"shop_money\":{\"amount\":\"4000\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"4000\",\"currency_code\":\"CLP\"}},\"total_price_set\":{\"shop_money\":{\"amount\":\"4760\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"4760\",\"currency_code\":\"CLP\"}},\"total_tax_set\":{\"shop_money\":{\"amount\":\"760\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"760\",\"currency_code\":\"CLP\"}},\"line_items\":[{\"id\":8893307093190,\"variant_id\":37639502069958,\"title\":\"Banana\",\"quantity\":2,\"sku\":\"02\",\"variant_title\":null,\"vendor\":\"Test Beetrack Shop\",\"fulfillment_service\":\"manual\",\"product_id\":6104659034310,\"requires_shipping\":true,\"taxable\":true,\"gift_card\":false,\"name\":\"Banana\",\"variant_inventory_management\":\"shopify\",\"properties\":[],\"product_exists\":true,\"fulfillable_quantity\":0,\"grams\":200,\"price\":\"2000\",\"total_discount\":\"0\",\"fulfillment_status\":\"fulfilled\",\"price_set\":{\"shop_money\":{\"amount\":\"2000\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"2000\",\"currency_code\":\"CLP\"}},\"total_discount_set\":{\"shop_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"}},\"discount_allocations\":[],\"duties\":[],\"admin_graphql_api_id\":\"gid:\\/\\/shopify\\/LineItem\\/8893307093190\",\"tax_lines\":[{\"title\":\"VAT\",\"price\":\"760\",\"rate\":0.19,\"price_set\":{\"shop_money\":{\"amount\":\"760\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"760\",\"currency_code\":\"CLP\"}}}]}],\"fulfillments\":[{\"id\":2882125496518,\"order_id\":3076447011014,\"status\":\"success\",\"created_at\":\"2020-11-23T11:08:27-05:00\",\"service\":\"manual\",\"updated_at\":\"2020-11-23T11:08:27-05:00\",\"tracking_company\":null,\"shipment_status\":null,\"location_id\":57954697414,\"line_items\":[{\"id\":8893307093190,\"variant_id\":37639502069958,\"title\":\"Banana\",\"quantity\":2,\"sku\":\"02\",\"variant_title\":null,\"vendor\":\"Test Beetrack Shop\",\"fulfillment_service\":\"manual\",\"product_id\":6104659034310,\"requires_shipping\":true,\"taxable\":true,\"gift_card\":false,\"name\":\"Banana\",\"variant_inventory_management\":\"shopify\",\"properties\":[],\"product_exists\":true,\"fulfillable_quantity\":0,\"grams\":200,\"price\":\"2000\",\"total_discount\":\"0\",\"fulfillment_status\":\"fulfilled\",\"price_set\":{\"shop_money\":{\"amount\":\"2000\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"2000\",\"currency_code\":\"CLP\"}},\"total_discount_set\":{\"shop_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"0\",\"currency_code\":\"CLP\"}},\"discount_allocations\":[],\"duties\":[],\"admin_graphql_api_id\":\"gid:\\/\\/shopify\\/LineItem\\/8893307093190\",\"tax_lines\":[{\"title\":\"VAT\",\"price\":\"760\",\"rate\":0.19,\"price_set\":{\"shop_money\":{\"amount\":\"760\",\"currency_code\":\"CLP\"},\"presentment_money\":{\"amount\":\"760\",\"currency_code\":\"CLP\"}}}]}],\"tracking_number\":null,\"tracking_numbers\":[],\"tracking_url\":null,\"tracking_urls\":[],\"receipt\":{},\"name\":\"#1002.1\",\"admin_graphql_api_id\":\"gid:\\/\\/shopify\\/Fulfillment\\/2882125496518\"}],\"refunds\":[],\"total_tip_received\":\"0.0\",\"original_total_duties_set\":null,\"current_total_duties_set\":null,\"admin_graphql_api_id\":\"gid:\\/\\/shopify\\/Order\\/3076447011014\",\"shipping_lines\":[],\"billing_address\":{\"first_name\":\"Agustin\",\"address1\":\"Las Pircas\",\"phone\":\"56482486\",\"city\":\"Santiago\",\"zip\":\"7690000\",\"province\":\"Santiago\",\"country\":\"Chile\",\"last_name\":\"Di Prospero\",\"address2\":\"01\",\"company\":\"Beetrack\",\"latitude\":null,\"longitude\":null,\"name\":\"Agustin Di Prospero\",\"country_code\":\"CL\",\"province_code\":\"RM\"},\"shipping_address\":{\"first_name\":\"Agustin\",\"address1\":\"Las Pircas\",\"phone\":\"56482486\",\"city\":\"Santiago\",\"zip\":\"7690000\",\"province\":\"Santiago\",\"country\":\"Chile\",\"last_name\":\"Di Prospero\",\"address2\":\"01\",\"company\":\"Beetrack\",\"latitude\":null,\"longitude\":null,\"name\":\"Agustin Di Prospero\",\"country_code\":\"CL\",\"province_code\":\"RM\"},\"customer\":{\"id\":4464336437446,\"email\":\"email@email.com\",\"accepts_marketing\":false,\"created_at\":\"2020-11-23T11:07:48-05:00\",\"updated_at\":\"2020-11-23T11:08:11-05:00\",\"first_name\":\"Agustin\",\"last_name\":\"Di Prospero\",\"orders_count\":1,\"state\":\"disabled\",\"total_spent\":\"4760.00\",\"last_order_id\":3076447011014,\"note\":null,\"verified_email\":true,\"multipass_identifier\":null,\"tax_exempt\":false,\"phone\":null,\"tags\":\"\",\"last_order_name\":\"#1002\",\"currency\":\"CLP\",\"accepts_marketing_updated_at\":\"2020-11-23T11:07:48-05:00\",\"marketing_opt_in_level\":null,\"admin_graphql_api_id\":\"gid:\\/\\/shopify\\/Customer\\/4464336437446\",\"default_address\":{\"id\":5467322843334,\"customer_id\":4464336437446,\"first_name\":\"Agustin\",\"last_name\":\"Di Prospero\",\"company\":\"Beetrack\",\"address1\":\"Las Pircas\",\"address2\":\"01\",\"city\":\"Santiago\",\"province\":\"Santiago\",\"country\":\"Chile\",\"zip\":\"7690000\",\"phone\":\"56482486\",\"name\":\"Agustin Di Prospero\",\"province_code\":\"RM\",\"country_code\":\"CL\",\"country_name\":\"Chile\",\"default\":true}}}",
  "body": {
    "id": 3076447011014,
    "email": "email@email.com",
    "closed_at": "2020-11-23T11:08:27-05:00",
    "created_at": "2020-11-23T11:08:10-05:00",
    "updated_at": "2020-11-23T11:08:27-05:00",
    "number": 2,
    "note": "Hola Agustin",
    "token": "58d5120a95b84b0407f08e9d4c29f0b4",
    "gateway": "manual",
    "test": False,
    "total_price": "4760",
    "subtotal_price": "4000",
    "total_weight": 400,
    "total_tax": "760",
    "taxes_included": False,
    "currency": "CLP",
    "financial_status": "paid",
    "confirmed": True,
    "total_discounts": "0",
    "total_line_items_price": "4000",
    "buyer_accepts_marketing": False,
    "name": "#1002",
    "total_price_usd": "6.23",
    "user_id": 67468394694,
    "processed_at": "2020-11-23T11:08:10-05:00",
    "customer_locale": "en",
    "app_id": 1354745,
    "client_details": {},
    "order_number": 1002,
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
        "price": "760",
        "rate": 0.19,
        "title": "VAT",
        "price_set": {
          "shop_money": {
            "amount": "760",
            "currency_code": "CLP"
          },
          "presentment_money": {
            "amount": "760",
            "currency_code": "CLP"
          }
        }
      }
    ],
    "tags": "Beetrack",
    "contact_email": "email@email.com",
    "order_status_url": "https://test-beetrack-shop.myshopify.com/51526041798/orders/58d5120a95b84b0407f08e9d4c29f0b4/authenticate?key=e01ad1b4884154474e9cc6ec60755401",
    "presentment_currency": "CLP",
    "total_line_items_price_set": {
      "shop_money": {
        "amount": "4000",
        "currency_code": "CLP"
      },
      "presentment_money": {
        "amount": "4000",
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
        "amount": "4000",
        "currency_code": "CLP"
      },
      "presentment_money": {
        "amount": "4000",
        "currency_code": "CLP"
      }
    },
    "total_price_set": {
      "shop_money": {
        "amount": "4760",
        "currency_code": "CLP"
      },
      "presentment_money": {
        "amount": "4760",
        "currency_code": "CLP"
      }
    },
    "total_tax_set": {
      "shop_money": {
        "amount": "760",
        "currency_code": "CLP"
      },
      "presentment_money": {
        "amount": "760",
        "currency_code": "CLP"
      }
    },
    "line_items": [
      {
        "id": 8893307093190,
        "variant_id": 37639502069958,
        "title": "Banana",
        "quantity": 2,
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
        "admin_graphql_api_id": "gid://shopify/LineItem/8893307093190",
        "tax_lines": [
          {
            "title": "VAT",
            "price": "760",
            "rate": 0.19,
            "price_set": {
              "shop_money": {
                "amount": "760",
                "currency_code": "CLP"
              },
              "presentment_money": {
                "amount": "760",
                "currency_code": "CLP"
              }
            }
          }
        ]
      }
    ],
    "fulfillments": [
      {
        "id": 2882125496518,
        "order_id": 3076447011014,
        "status": "success",
        "created_at": "2020-11-23T11:08:27-05:00",
        "service": "manual",
        "updated_at": "2020-11-23T11:08:27-05:00",
        "location_id": 57954697414,
        "line_items": [
          {
            "id": 8893307093190,
            "variant_id": 37639502069958,
            "title": "Banana",
            "quantity": 2,
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
            "admin_graphql_api_id": "gid://shopify/LineItem/8893307093190",
            "tax_lines": [
              {
                "title": "VAT",
                "price": "760",
                "rate": 0.19,
                "price_set": {
                  "shop_money": {
                    "amount": "760",
                    "currency_code": "CLP"
                  },
                  "presentment_money": {
                    "amount": "760",
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
        "name": "#1002.1",
        "admin_graphql_api_id": "gid://shopify/Fulfillment/2882125496518"
      }
    ],
    "refunds": [],
    "total_tip_received": "0.0",
    "admin_graphql_api_id": "gid://shopify/Order/3076447011014",
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
      "updated_at": "2020-11-23T11:08:11-05:00",
      "first_name": "Agustin",
      "last_name": "Di Prospero",
      "orders_count": 1,
      "state": "disabled",
      "total_spent": "4760.00",
      "last_order_id": 3076447011014,
      "verified_email": True,
      "tax_exempt": False,
      "tags": "",
      "last_order_name": "#1002",
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

  if domain:

    body = event.get("body") # Solo para ambiente de prueba
    shopify_webhook_handler = ShopifyWebhookHandler()
    shopify_fulfilled = shopify_webhook_handler.check_for_fulfilled_order(body)
    beetrack_tagged = shopify_webhook_handler.check_for_beetrack_tag(body)

    if shopify_fulfilled == True and beetrack_tagged == True:

        shopify_costumer_info = shopify_webhook_handler.get_shopify_costumer_info(body)
        shopify_items = shopify_webhook_handler.get_shopify_items(body)
        creating_shopify_dispatch = create_shopify_dispatch(domain, shopify_costumer_info, shopify_items)
        print("Response guide creation: {}").format(creating_shopify_dispatch)

  elif: user_uuid:

  else:
    print("Webhook doesn't belong")



integrate(evento)