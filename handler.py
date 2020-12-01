from pkg.shopify_to_beetrack import ShopifyToBeetrack
from pkg.beetrack_to_shopify import BeetrackToShopify
import datetime
import json, requests
import ipdb

evento_beetrack = {
   "resource":"/shopify_handler/integrate",
   "path":"/shopify_handler/integrate",
   "httpMethod":"POST",
   "headers":{
      "Accept":"*/*",
      "Accept-Encoding":"gzip, deflate",
      "CloudFront-Forwarded-Proto":"https",
      "CloudFront-Is-Desktop-Viewer":"true",
      "CloudFront-Is-Mobile-Viewer":"false",
      "CloudFront-Is-SmartTV-Viewer":"false",
      "CloudFront-Is-Tablet-Viewer":"false",
      "CloudFront-Viewer-Country":"US",
      "Content-Type":"application/json",
      "Host":"7mfmofytje.execute-api.us-west-2.amazonaws.com",
      "User-Agent":"rest-client/2.0.2 (linux-gnu x86_64) ruby/2.4.5p335",
      "User_uuid":"3cef408e-7cbf-4a63-bf3e-1f384564d8d7",
      "Via":"1.1 4e4146a38d6d3f79964fdb06a05f26cf.cloudfront.net (CloudFront)",
      "X-Amz-Cf-Id":"4zTdDekLg4OOLIxU4M9hD7dHzDJZEXvnv_wJmLLrhOGfcsrFNXjAxw==",
      "X-Amzn-Trace-Id":"Root=1-5fc53ac6-239485f30cde17f80d1a4629",
      "X-Forwarded-For":"34.216.68.127, 130.176.100.151",
      "X-Forwarded-Port":"443",
      "X-Forwarded-Proto":"https",
      "X-Newrelic-Id":"UwQBWVVaGwQGXFFaBgU=",
      "X-Newrelic-Transaction":"PxQDV1UGDFFUUFRTB1VSVVNTFB8EBw8RVU4aVg4LUQZRAQ1UAFFXB1cBVUNKQQ9RVlZUAFZSFTs="
   },
   "multiValueHeaders":{
      "Accept":[
         "*/*"
      ],
      "Accept-Encoding":[
         "gzip, deflate"
      ],
      "CloudFront-Forwarded-Proto":[
         "https"
      ],
      "CloudFront-Is-Desktop-Viewer":[
         "true"
      ],
      "CloudFront-Is-Mobile-Viewer":[
         "false"
      ],
      "CloudFront-Is-SmartTV-Viewer":[
         "false"
      ],
      "CloudFront-Is-Tablet-Viewer":[
         "false"
      ],
      "CloudFront-Viewer-Country":[
         "US"
      ],
      "Content-Type":[
         "application/json"
      ],
      "Host":[
         "7mfmofytje.execute-api.us-west-2.amazonaws.com"
      ],
      "User-Agent":[
         "rest-client/2.0.2 (linux-gnu x86_64) ruby/2.4.5p335"
      ],
      "User_uuid":[
         "3cef408e-7cbf-4a63-bf3e-1f384564d8d7"
      ],
      "Via":[
         "1.1 4e4146a38d6d3f79964fdb06a05f26cf.cloudfront.net (CloudFront)"
      ],
      "X-Amz-Cf-Id":[
         "4zTdDekLg4OOLIxU4M9hD7dHzDJZEXvnv_wJmLLrhOGfcsrFNXjAxw=="
      ],
      "X-Amzn-Trace-Id":[
         "Root=1-5fc53ac6-239485f30cde17f80d1a4629"
      ],
      "X-Forwarded-For":[
         "34.216.68.127, 130.176.100.151"
      ],
      "X-Forwarded-Port":[
         "443"
      ],
      "X-Forwarded-Proto":[
         "https"
      ],
      "X-Newrelic-Id":[
         "UwQBWVVaGwQGXFFaBgU="
      ],
      "X-Newrelic-Transaction":[
         "PxQDV1UGDFFUUFRTB1VSVVNTFB8EBw8RVU4aVg4LUQZRAQ1UAFFXB1cBVUNKQQ9RVlZUAFZSFTs="
      ]
   },
   "queryStringParameters":"None",
   "multiValueQueryStringParameters":"None",
   "pathParameters":"None",
   "stageVariables":"None",
   "requestContext":{
      "resourceId":"1n0709",
      "resourcePath":"/shopify_handler/integrate",
      "httpMethod":"POST",
      "extendedRequestId":"W1Ye-GeDvHcFzxw=",
      "requestTime":"30/Nov/2020:18:32:38 +0000",
      "path":"/staging/shopify_handler/integrate",
      "accountId":"821745794127",
      "protocol":"HTTP/1.1",
      "stage":"staging",
      "domainPrefix":"7mfmofytje",
      "requestTimeEpoch":1606761158173,
      "requestId":"b7591989-cffc-46a7-a569-3ddde6936826",
      "identity":{
         "cognitoIdentityPoolId":"None",
         "accountId":"None",
         "cognitoIdentityId":"None",
         "caller":"None",
         "sourceIp":"34.216.68.127",
         "principalOrgId":"None",
         "accessKey":"None",
         "cognitoAuthenticationType":"None",
         "cognitoAuthenticationProvider":"None",
         "userArn":"None",
         "userAgent":"rest-client/2.0.2 (linux-gnu x86_64) ruby/2.4.5p335",
         "user":"None"
      },
      "domainName":"7mfmofytje.execute-api.us-west-2.amazonaws.com",
      "apiId":"7mfmofytje"
   },
   "body": {
   "resource":"dispatch",
   "event":"update",
   "account_name":"Bianca Barría",
   "account_id":2290,
   "guide":"1001",
   "identifier":"1001",
   "route_id":"null",
   "dispatch_id":182349637,
   "truck_identifier":"null",
   "status":3,
   "substatus":"null",
   "substatus_code":"null",
   "estimated_at":"null",
   "contact_identifier":"null",
   "contact_phone":"988293632",
   "contact_name":"Bianca Barria",
   "contact_email":"null",
   "contact_address":"Av. Kennedy 5436, Santiago, Santiago, Chile",
   "tags":[
      {
         "name":"id_fulfilled",
         "value":"2705207394469"
      },
      {
         "name":"id_order_shopify",
         "value":"2888984723621"
      }
   ],
   "is_pickup":"false",
   "is_trunk":"false",
   "locked":"false",
   "items":[
      {
         "id":291226821,
         "name":"Top Shop Jeans",
         "description":"Top Shop Jeans",
         "quantity":1,
         "original_quantity":1,
         "delivered_quantity":1,
         "code":"6258729320613",
         "extras":[
            
         ]
      },
      {
         "id":291226822,
         "name":"Top Shop Shirt",
         "description":"Top Shop Shirt",
         "quantity":1,
         "original_quantity":1,
         "delivered_quantity":1,
         "code":"6258729353381",
         "extras":[
            
         ]
      }
   ],
   "groups":[
      
   ],
   "arrived_at":"2020-11-30 15:31:34-0300",
   "evaluation_answers":[
      
    ]
   },
   "isBase64Encoded": False
}
evento_shopify = {
   "resource":"/shopify_handler/integrate",
   "path":"/shopify_handler/integrate",
   "httpMethod":"POST",
   "headers":{
      "Accept":"*/*",
      "Accept-Encoding":"gzip;q=1.0,deflate;q=0.6,identity;q=0.3",
      "CloudFront-Forwarded-Proto":"https",
      "CloudFront-Is-Desktop-Viewer":"true",
      "CloudFront-Is-Mobile-Viewer":"false",
      "CloudFront-Is-SmartTV-Viewer":"false",
      "CloudFront-Is-Tablet-Viewer":"false",
      "CloudFront-Viewer-Country":"US",
      "Content-Type":"application/json",
      "Host":"7mfmofytje.execute-api.us-west-2.amazonaws.com",
      "User-Agent":"Shopify-Captain-Hook",
      "Via":"1.1 9ef84cf4cc2ba519912977f9e63d129e.cloudfront.net (CloudFront)",
      "X-Amz-Cf-Id":"duekrKOtKXNkM9M6ICMBADTzjk_tana-w98YpjJrByE_AkaMhYIvEw==",
      "X-Amzn-Trace-Id":"Root=1-5fc524aa-094521e74291375869219541",
      "X-Forwarded-For":"35.227.9.14, 130.176.151.152",
      "X-Forwarded-Port":"443",
      "X-Forwarded-Proto":"https",
      "X-Shopify-Api-Version":"2020-10",
      "X-Shopify-Hmac-Sha256":"rFjzyHCHE5F0bmzeXru8/R7BvAl2ZMJzdd/oSNn2gSM=",
      "X-Shopify-Order-Id":"2888984723621",
      "X-Shopify-Shop-Domain":"comparaonline.myshopify.com",
      "X-Shopify-Test":"false",
      "X-Shopify-Topic":"orders/fulfilled"
   },
   "multiValueHeaders":{
      "Accept":[
         "*/*"
      ],
      "Accept-Encoding":[
         "gzip;q=1.0,deflate;q=0.6,identity;q=0.3"
      ],
      "CloudFront-Forwarded-Proto":[
         "https"
      ],
      "CloudFront-Is-Desktop-Viewer":[
         "true"
      ],
      "CloudFront-Is-Mobile-Viewer":[
         "false"
      ],
      "CloudFront-Is-SmartTV-Viewer":[
         "false"
      ],
      "CloudFront-Is-Tablet-Viewer":[
         "false"
      ],
      "CloudFront-Viewer-Country":[
         "US"
      ],
      "Content-Type":[
         "application/json"
      ],
      "Host":[
         "7mfmofytje.execute-api.us-west-2.amazonaws.com"
      ],
      "User-Agent":[
         "Shopify-Captain-Hook"
      ],
      "Via":[
         "1.1 9ef84cf4cc2ba519912977f9e63d129e.cloudfront.net (CloudFront)"
      ],
      "X-Amz-Cf-Id":[
         "duekrKOtKXNkM9M6ICMBADTzjk_tana-w98YpjJrByE_AkaMhYIvEw=="
      ],
      "X-Amzn-Trace-Id":[
         "Root=1-5fc524aa-094521e74291375869219541"
      ],
      "X-Forwarded-For":[
         "35.227.9.14, 130.176.151.152"
      ],
      "X-Forwarded-Port":[
         "443"
      ],
      "X-Forwarded-Proto":[
         "https"
      ],
      "X-Shopify-Api-Version":[
         "2020-10"
      ],
      "X-Shopify-Hmac-Sha256":[
         "rFjzyHCHE5F0bmzeXru8/R7BvAl2ZMJzdd/oSNn2gSM="
      ],
      "X-Shopify-Order-Id":[
         "2888984723621"
      ],
      "X-Shopify-Shop-Domain":[
         "comparaonline.myshopify.com"
      ],
      "X-Shopify-Test":[
         "false"
      ],
      "X-Shopify-Topic":[
         "orders/fulfilled"
      ]
   },
   "queryStringParameters":"None",
   "multiValueQueryStringParameters":"None",
   "pathParameters":"None",
   "stageVariables":"None",
   "requestContext":{
      "resourceId":"1n0709",
      "resourcePath":"/shopify_handler/integrate",
      "httpMethod":"POST",
      "extendedRequestId":"W1KqnHR0vHcFnIQ=",
      "requestTime":"30/Nov/2020:16:58:18 +0000",
      "path":"/staging/shopify_handler/integrate",
      "accountId":"821745794127",
      "protocol":"HTTP/1.1",
      "stage":"staging",
      "domainPrefix":"7mfmofytje",
      "requestTimeEpoch":1606755498295,
      "requestId":"00bff22d-f615-4833-9cd5-818a7ef656b2",
      "identity":{
         "cognitoIdentityPoolId":"None",
         "accountId":"None",
         "cognitoIdentityId":"None",
         "caller":"None",
         "sourceIp":"35.227.9.14",
         "principalOrgId":"None",
         "accessKey":"None",
         "cognitoAuthenticationType":"None",
         "cognitoAuthenticationProvider":"None",
         "userArn":"None",
         "userAgent":"Shopify-Captain-Hook",
         "user":"None"
      },
      "domainName":"7mfmofytje.execute-api.us-west-2.amazonaws.com",
      "apiId":"7mfmofytje"
   },
   "body":{
   "id":2888984723621,
   "email":"bianca.barria@beetrack.com",
   "closed_at":"2020-11-30T11:58:04-05:00",
   "created_at":"2020-11-30T11:38:37-05:00",
   "updated_at":"2020-11-30T11:58:04-05:00",
   "number":1,
   "note":"",
   "token":"9905cddf66119183fa24b9998935af1e",
   "gateway":"manual",
   "test":"false",
   "total_price":"17850",
   "subtotal_price":"15000",
   "total_weight":300,
   "total_tax":"2850",
   "taxes_included":"false",
   "currency":"CLP",
   "financial_status":"paid",
   "confirmed":"true",
   "total_discounts":"0",
   "total_line_items_price":"15000",
   "cart_token":"null",
   "buyer_accepts_marketing":"true",
   "name":"#1001",
   "referring_site":"null",
   "landing_site":"null",
   "cancelled_at":"null",
   "cancel_reason":"null",
   "total_price_usd":"23.22",
   "checkout_token":"null",
   "reference":"null",
   "user_id":66303000741,
   "location_id":"null",
   "source_identifier":"null",
   "source_url":"null",
   "processed_at":"2020-11-30T11:38:37-05:00",
   "device_id":"null",
   "phone":"null",
   "customer_locale":"en",
   "app_id":1354745,
   "browser_ip":"null",
   "landing_site_ref":"null",
   "order_number":1001,
   "discount_applications":[
      
   ],
   "discount_codes":[
      
   ],
   "note_attributes":[
      
   ],
   "payment_gateway_names":[
      "manual"
   ],
   "processing_method":"manual",
   "checkout_id":"null",
   "source_name":"shopify_draft_order",
   "fulfillment_status":"fulfilled",
   "tax_lines":[
      {
         "price":"2850",
         "rate":0.19,
         "title":"VAT",
         "price_set":{
            "shop_money":{
               "amount":"2850",
               "currency_code":"CLP"
            },
            "presentment_money":{
               "amount":"2850",
               "currency_code":"CLP"
            }
         }
      }
   ],
   "tags":"Beetrack",
   "contact_email":"bianca.barria@beetrack.com",
   "order_status_url":"https://comparaonline.myshopify.com/50819432613/orders/9905cddf66119183fa24b9998935af1e/authenticate?key=0fa542f1abce2d74a368de3069b93fe3",
   "presentment_currency":"CLP",
   "total_line_items_price_set":{
      "shop_money":{
         "amount":"15000",
         "currency_code":"CLP"
      },
      "presentment_money":{
         "amount":"15000",
         "currency_code":"CLP"
      }
   },
   "total_discounts_set":{
      "shop_money":{
         "amount":"0",
         "currency_code":"CLP"
      },
      "presentment_money":{
         "amount":"0",
         "currency_code":"CLP"
      }
   },
   "total_shipping_price_set":{
      "shop_money":{
         "amount":"0",
         "currency_code":"CLP"
      },
      "presentment_money":{
         "amount":"0",
         "currency_code":"CLP"
      }
   },
   "subtotal_price_set":{
      "shop_money":{
         "amount":"15000",
         "currency_code":"CLP"
      },
      "presentment_money":{
         "amount":"15000",
         "currency_code":"CLP"
      }
   },
   "total_price_set":{
      "shop_money":{
         "amount":"17850",
         "currency_code":"CLP"
      },
      "presentment_money":{
         "amount":"17850",
         "currency_code":"CLP"
      }
   },
   "total_tax_set":{
      "shop_money":{
         "amount":"2850",
         "currency_code":"CLP"
      },
      "presentment_money":{
         "amount":"2850",
         "currency_code":"CLP"
      }
   },
   "line_items":[
      {
         "id":6258729320613,
         "variant_id":37301201076389,
         "title":"Top Shop Jeans",
         "quantity":1,
         "sku":"12345",
         "variant_title":"M",
         "vendor":"ComparaOnline",
         "fulfillment_service":"manual",
         "product_id":5956129390757,
         "requires_shipping":"true",
         "taxable":"true",
         "gift_card":"false",
         "name":"Top Shop Jeans - M",
         "variant_inventory_management":"shopify",
         "properties":[
            
         ],
         "product_exists":"true",
         "fulfillable_quantity":0,
         "grams":200,
         "price":"10000",
         "total_discount":"0",
         "fulfillment_status":"fulfilled",
         "price_set":{
            "shop_money":{
               "amount":"10000",
               "currency_code":"CLP"
            },
            "presentment_money":{
               "amount":"10000",
               "currency_code":"CLP"
            }
         },
         "total_discount_set":{
            "shop_money":{
               "amount":"0",
               "currency_code":"CLP"
            },
            "presentment_money":{
               "amount":"0",
               "currency_code":"CLP"
            }
         },
         "discount_allocations":[
            
         ],
         "duties":[
            
         ],
         "admin_graphql_api_id":"gid://shopify/LineItem/6258729320613",
         "tax_lines":[
            {
               "title":"VAT",
               "price":"1900",
               "rate":0.19,
               "price_set":{
                  "shop_money":{
                     "amount":"1900",
                     "currency_code":"CLP"
                  },
                  "presentment_money":{
                     "amount":"1900",
                     "currency_code":"CLP"
                  }
               }
            }
         ]
      },
      {
         "id":6258729353381,
         "variant_id":37301261402277,
         "title":"Top Shop Shirt",
         "quantity":1,
         "sku":"12348",
         "variant_title":"L",
         "vendor":"ComparaOnline",
         "fulfillment_service":"manual",
         "product_id":5956140466341,
         "requires_shipping":"true",
         "taxable":"true",
         "gift_card":"false",
         "name":"Top Shop Shirt - L",
         "variant_inventory_management":"shopify",
         "properties":[
            
         ],
         "product_exists":"true",
         "fulfillable_quantity":0,
         "grams":100,
         "price":"5000",
         "total_discount":"0",
         "fulfillment_status":"fulfilled",
         "price_set":{
            "shop_money":{
               "amount":"5000",
               "currency_code":"CLP"
            },
            "presentment_money":{
               "amount":"5000",
               "currency_code":"CLP"
            }
         },
         "total_discount_set":{
            "shop_money":{
               "amount":"0",
               "currency_code":"CLP"
            },
            "presentment_money":{
               "amount":"0",
               "currency_code":"CLP"
            }
         },
         "discount_allocations":[
            
         ],
         "duties":[
            
         ],
         "admin_graphql_api_id":"gid://shopify/LineItem/6258729353381",
         "tax_lines":[
            {
               "title":"VAT",
               "price":"950",
               "rate":0.19,
               "price_set":{
                  "shop_money":{
                     "amount":"950",
                     "currency_code":"CLP"
                  },
                  "presentment_money":{
                     "amount":"950",
                     "currency_code":"CLP"
                  }
               }
            }
         ]
      }
   ],
   "fulfillments":[
      {
         "id":2705207394469,
         "order_id":2888984723621,
         "status":"success",
         "created_at":"2020-11-30T11:58:04-05:00",
         "service":"manual",
         "updated_at":"2020-11-30T11:58:04-05:00",
         "tracking_company":"null",
         "shipment_status":"null",
         "location_id":57040732325,
         "line_items":[
            {
               "id":6258729320613,
               "variant_id":37301201076389,
               "title":"Top Shop Jeans",
               "quantity":1,
               "sku":"12345",
               "variant_title":"M",
               "vendor":"ComparaOnline",
               "fulfillment_service":"manual",
               "product_id":5956129390757,
               "requires_shipping":"true",
               "taxable":"true",
               "gift_card":"false",
               "name":"Top Shop Jeans - M",
               "variant_inventory_management":"shopify",
               "properties":[
                  
               ],
               "product_exists":"true",
               "fulfillable_quantity":0,
               "grams":200,
               "price":"10000",
               "total_discount":"0",
               "fulfillment_status":"fulfilled",
               "price_set":{
                  "shop_money":{
                     "amount":"10000",
                     "currency_code":"CLP"
                  },
                  "presentment_money":{
                     "amount":"10000",
                     "currency_code":"CLP"
                  }
               },
               "total_discount_set":{
                  "shop_money":{
                     "amount":"0",
                     "currency_code":"CLP"
                  },
                  "presentment_money":{
                     "amount":"0",
                     "currency_code":"CLP"
                  }
               },
               "discount_allocations":[
                  
               ],
               "duties":[
                  
               ],
               "admin_graphql_api_id":"gid://shopify/LineItem/6258729320613",
               "tax_lines":[
                  {
                     "title":"VAT",
                     "price":"1900",
                     "rate":0.19,
                     "price_set":{
                        "shop_money":{
                           "amount":"1900",
                           "currency_code":"CLP"
                        },
                        "presentment_money":{
                           "amount":"1900",
                           "currency_code":"CLP"
                        }
                     }
                  }
               ]
            },
            {
               "id":6258729353381,
               "variant_id":37301261402277,
               "title":"Top Shop Shirt",
               "quantity":1,
               "sku":"12348",
               "variant_title":"L",
               "vendor":"ComparaOnline",
               "fulfillment_service":"manual",
               "product_id":5956140466341,
               "requires_shipping":"true",
               "taxable":"true",
               "gift_card":"false",
               "name":"Top Shop Shirt - L",
               "variant_inventory_management":"shopify",
               "properties":[
                  
               ],
               "product_exists":"true",
               "fulfillable_quantity":0,
               "grams":100,
               "price":"5000",
               "total_discount":"0",
               "fulfillment_status":"fulfilled",
               "price_set":{
                  "shop_money":{
                     "amount":"5000",
                     "currency_code":"CLP"
                  },
                  "presentment_money":{
                     "amount":"5000",
                     "currency_code":"CLP"
                  }
               },
               "total_discount_set":{
                  "shop_money":{
                     "amount":"0",
                     "currency_code":"CLP"
                  },
                  "presentment_money":{
                     "amount":"0",
                     "currency_code":"CLP"
                  }
               },
               "discount_allocations":[
                  
               ],
               "duties":[
                  
               ],
               "admin_graphql_api_id":"gid://shopify/LineItem/6258729353381",
               "tax_lines":[
                  {
                     "title":"VAT",
                     "price":"950",
                     "rate":0.19,
                     "price_set":{
                        "shop_money":{
                           "amount":"950",
                           "currency_code":"CLP"
                        },
                        "presentment_money":{
                           "amount":"950",
                           "currency_code":"CLP"
                        }
                     }
                  }
               ]
            }
         ],
         "tracking_number":"null",
         "tracking_numbers":[
            
         ],
         "tracking_url":"null",
         "tracking_urls":[
            
         ],
         "receipt":{
            
         },
         "name":"#1001.1",
         "admin_graphql_api_id":"gid://shopify/Fulfillment/2705207394469"
      }
   ],
   "refunds":[
      
   ],
   "total_tip_received":"0.0",
   "original_total_duties_set":"null",
   "current_total_duties_set":"null",
   "admin_graphql_api_id":"gid://shopify/Order/2888984723621",
   "shipping_lines":[
      
   ],
   "billing_address":{
      "first_name":"Bianca",
      "address1":"Av. Kennedy 5436",
      "phone":"988293632",
      "city":"Santiago",
      "zip":"7630845",
      "province":"Santiago",
      "country":"Chile",
      "last_name":"Barria",
      "address2":"46",
      "company":"null",
      "latitude":"null",
      "longitude":"null",
      "name":"Bianca Barria",
      "country_code":"CL",
      "province_code":"RM"
   },
   "shipping_address":{
      "first_name":"Bianca",
      "address1":"Av. Kennedy 5436",
      "phone":"988293632",
      "city":"Santiago",
      "zip":"7630845",
      "province":"Santiago",
      "country":"Chile",
      "last_name":"Barria",
      "address2":"46",
      "company":"null",
      "latitude":"null",
      "longitude":"null",
      "name":"Bianca Barria",
      "country_code":"CL",
      "province_code":"RM"
   },
   "customer":{
      "id":4233766568101,
      "email":"bianca.barria@beetrack.com",
      "accepts_marketing":"true",
      "created_at":"2020-11-30T11:37:52-05:00",
      "updated_at":"2020-11-30T11:38:38-05:00",
      "first_name":"Bianca",
      "last_name":"Barria",
      "orders_count":1,
      "state":"disabled",
      "total_spent":"17850.00",
      "last_order_id":2888984723621,
      "note":"null",
      "verified_email":"true",
      "multipass_identifier":"null",
      "tax_exempt":"false",
      "phone":"null",
      "tags":"Beetrack",
      "last_order_name":"#1001",
      "currency":"CLP",
      "accepts_marketing_updated_at":"2020-11-30T11:37:52-05:00",
      "marketing_opt_in_level":"single_opt_in",
      "admin_graphql_api_id":"gid://shopify/Customer/4233766568101",
      "default_address":{
         "id":5080084185253,
         "customer_id":4233766568101,
         "first_name":"Bianca",
         "last_name":"Barria",
         "company":"",
         "address1":"Av. Kennedy 5436",
         "address2":"46",
         "city":"Santiago",
         "province":"Santiago",
         "country":"Chile",
         "zip":"7630845",
         "phone":"988293632",
         "name":"Bianca Barria",
         "province_code":"RM",
         "country_code":"CL",
         "country_name":"Chile",
         "default":"true"
      }
   }
   },
   "isBase64Encoded": False
}

def integrate(event):
  shopify_event = event.get("headers").get("X-Shopify-Shop-Domain")
  beetrack_event = event.get("headers").get("User_uuid")
  body = event.get("body") # Solo para ambiente de prueba

  if shopify_event:
    print(shopify_event)
    verify_order = ShopifyToBeetrack(body).verify_order()
    #Verify if a user put the tags after the fulfilled will we get a WH
    if verify_order:
      url = "http://localhost:5000/shopify_credentials/" + str(shopify_event)
      print(url)
      beetrack_credentials = requests.get(url).json()
      print (beetrack_credentials)
      creating_shopify_dispatch = ShopifyToBeetrack(body).create_shopify_dispatch(beetrack_credentials)
      print("Response guide creation: ",creating_shopify_dispatch) # Reparar print.
    else:
      print ("Order doensn't belong to Beetrack")

  elif beetrack_event:
    print({"Event": "This is a Beetrack Event"})
    resource = body.get("resource")
    event = body.get("event")
    if resource == "dispatch" and event == "update":
      url = "http://localhost:5000/beetrack_credentials/" + str(beetrack_event)
      shopify_credentials = requests.get(url).json()
      beetrack_to_shopify = BeetrackToShopify(body, shopify_credentials).send_to_shopify()
      print(beetrack_to_shopify)
  else:
    print("Webhook doesn't belong")

integrate(evento_beetrack)