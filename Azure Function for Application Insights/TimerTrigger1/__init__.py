import datetime
import logging
import azure.functions as func
from azure.data.tables import TableServiceClient,TableEntity,TableClient
from azure.core.credentials import AzureNamedKeyCredential
import requests
import json
from azure.core.credentials import AzureNamedKeyCredential
from azure.core.exceptions import  ResourceExistsError

connection_string = "DefaultEndpointsProtocol=https;AccountName=websiteacesslogs;AccountKey=IKG18LB+gBnds6fcVgypk2DXfvRCSHIy2zwU9tkr5ERZd4CuSqG2glORRsueOo9+/R+71RX5vdSkReEo35I3Rw==;EndpointSuffix=core.windows.net"
table_service_client = TableServiceClient.from_connection_string(conn_str=connection_string)
table_client = table_service_client.get_table_client(table_name="testtable")
account_name = 'websiteacesslogs'
access_key = 'IKG18LB+gBnds6fcVgypk2DXfvRCSHIy2zwU9tkr5ERZd4CuSqG2glORRsueOo9+/R+71RX5vdSkReEo35I3Rw=='
endpoint = 'https://websiteacesslogs.table.core.windows.net/'
table_name = 'testtable'
credential = AzureNamedKeyCredential(account_name, access_key)

def main(mytimer: func.TimerRequest) -> None:
    if mytimer.past_due:
        print("step 1")
        logging.info("step 1")
    r1 =requests.get('https://api.applicationinsights.io/v1/apps/67a8c5fe-f4f5-41bc-8341-008fecb33561/events/$all?timespan=PT2M', headers={'X-API-Key':"m2svqdhawnt0wi0kksemmnfs4oohyqhhz4qnfsxa"})
    x=r1.content.decode("utf-8")
    xtest=json.loads(x)
    #logging.info(xtest["value"])
    for index in range(len(xtest["value"])):
        if(xtest["value"][index]["type"]=="pageView"):
            my_entity = TableEntity(RowKey=xtest["value"][index]["user"]["id"], PartitionKey=xtest["value"][index]["timestamp"],websiteurl=xtest["value"][index]["pageView"]["url"] , appname=xtest["value"][index]["ai"]["appName"])
            table_client = TableClient.from_connection_string(
            conn_str=connection_string,
            table_name="trial"
        )  
            try:
                resp = table_client.create_entity(entity=my_entity)
            except ResourceExistsError:
                print("Entry already exists")
                logging.info("Entry already exists")
    r2 =requests.get('https://api.applicationinsights.io/v1/apps/6c69b87f-1dfa-4f3d-a9c9-17561fbac0e1/events/$all?timespan=PT2M', headers={'X-API-Key':"lsp0wgd14mszv8grv15zi4x3i8pbaoybxx3idcfm"})
    x=r2.content.decode("utf-8")
    xtest=json.loads(x)
    #logging.info(xtest["value"])
    for index in range(len(xtest["value"])):
        if(xtest["value"][index]["type"]=="pageView"):
            my_entity = TableEntity(RowKey=xtest["value"][index]["user"]["id"], PartitionKey=xtest["value"][index]["timestamp"],websiteurl=xtest["value"][index]["pageView"]["url"] , appname=xtest["value"][index]["ai"]["appName"])
            table_client = TableClient.from_connection_string(
            conn_str=connection_string,
            table_name="trial"
        )  
            #r=str(xtest["value"][0]["user"])
            #r2=str(xtest["value"][0]["timestamp"])
            #my_entity = TableEntity(RowKey="1", PartitionKey="1")
            #my_entity = TableEntity(RowKey=r, PartitionKey=r2)

            try:
            #   table_item = table_client.create_table()
            #   print("Created table {}!".format(table_item.table_name))
                resp = table_client.create_entity(entity=my_entity)
            except ResourceExistsError:
                print("Entry already exists")
                logging.info("Entry already exists")
