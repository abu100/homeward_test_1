from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


class QualiaClient:
    def __init__(self):
        transport = RequestsHTTPTransport(url='https://qa-connect.qualia.io/api/partner/graphql',
                                          headers={"Authorization": "Basic INSERT_YOUR_CREDENTIALS_HERE"})
        self.client = Client(transport=transport)

    def get_all_order_ids(self):
        size = 1
        limit = 1
        offset = 0
        while size != 0:
            query = gql(f"""
                        query GetOrder {{
                          orders(input: {{limit: {limit}, offset: {offset}}}) {{
                            orders {{
                              _id
                              cash_only
                              close_date
                              external_reference_number
                              loan_amount
                              loan_type
                              order_number
                              orderer_id
                              open_date
                              parties {{
                                borrowers {{
                                  _id
                                  first_name
                                  last_name
                                  cell_phone
                                  email
                                }}
                                sellers {{
                                  _id
                                  first_name
                                  last_name
                                  cell_phone
                                  email
                                }}
                                lender_contacts {{
                                  _id
                                  first_name
                                  last_name
                                  cell_phone
                                  email
                                  organization_name
                                }}
                                listing_agents {{
                                  _id
                                  first_name
                                  last_name
                                  cell_phone
                                  email
                                  organization_name
                                }}
                                selling_agents {{
                                  _id
                                  first_name
                                  last_name
                                  cell_phone
                                  email
                                  organization_name
                                }}
                              }}
                              progress {{
                                current_stage
                                current_stage_key
                                borrower_opening_package_sent {{
                                  complete
                                  completion_date
                                }}
                                commitment_generated {{
                                  complete
                                  completion_date
                                }}
                                confirmation_of_order_received {{
                                  complete
                                  completion_date
                                }}
                                cpl_issued {{
                                  complete
                                  completion_date
                                }}
                                deed_mortgage_recorded {{
                                  complete
                                  completion_date
                                }}
                                earnest_money_received {{
                                  complete
                                  completion_date
                                }}
                                estimated_closing_statement_sent_seller {{
                                  complete
                                  completion_date
                                }}
                                estimated_closing_statement_sent_borrower {{
                                  complete
                                  completion_date
                                }}
                                final_fees_sent {{
                                  complete
                                  completion_date
                                }}
                                funds_disbursed {{
                                  complete
                                  completion_date
                                }}
                                order_accepted {{
                                  complete
                                  completion_date
                                }}
                                preliminary_fees_sent {{
                                  complete
                                  completion_date
                                }}
                                preliminary_report_ordered {{
                                  complete
                                  completion_date
                                }}
                                preliminary_report_received {{
                                  complete
                                  completion_date
                                }}
                                seller_opening_package_sent {{
                                  complete
                                  completion_date
                                }}
                                settlement_statement_generated {{
                                  complete
                                  completion_date
                                }}
                                signing_scheduled {{
                                  complete
                                  completion_date
                                }}
                                signing_scheduled_borrower {{
                                  complete
                                  completion_date
                                }}
                                signing_scheduled_seller {{
                                  complete
                                  completion_date
                                }}
                                title_insurance_issued {{
                                  complete
                                  completion_date
                                }}
                              }}
                              properties {{
                                address_line_1
                                address_line_2
                                city
                                state
                                zipcode
                                county
                              }}
                              purchase_price
                              settlement_agency_name
                              settlement_agency_id
                              status
                              message_threads {{
                                _id
                                subject
                                parties_on_thread {{
                                  name
                                  role
                                }}
                                messages {{
                                  created_date
                                  from_name
                                  from_email
                                  text
                                  attachments {{
                                    name
                                    url
                                    expiry
                                  }}
                                }}
                              }}
                              information_requests {{
                                _id
                                recipient_id
                                request_type
                                created_date
                                status
                              }}
                              activities {{
                                activity_type
                                created_date
                                description
                              }}
                            }}
                          }}
                        }}
                    """)

            data = self.client.execute(query, variable_values={"limit": 1, "offset": offset})
            size = len(data.get("orders").get("orders"))
            print(data)
            offset += size


client = QualiaClient()
client.get_all_order_ids()