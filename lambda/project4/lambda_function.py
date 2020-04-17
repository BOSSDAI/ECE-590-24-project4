# import json

# def lambda_handler(event, context):
#     print(f"Got an event: {event}")
#     print(f"This is the context: {context}")
#     new_payload = {"hello": event}
#     return_statement = f"Hello from Lambda! {new_payload}"
#     return {
#         'statusCode': 200,
#         'body': json.dumps(return_statement)
#     }
import json
import wikipedia

print('Loading function')


def lambda_handler(event, context):
    """Wikipedia Summarizer"""
    
    if 'body' in event:
        event = json.loads(event["body"])
    entity = event["entity"]
    res = wikipedia.summary(entity, sentences=1)
    print(f"context: {context}, event: {event}")
    print(f"Response from wikipedia API: {res}")
    response = {
    "statusCode": "200",
    "headers": { "Content-type": "application/json" },
    "body": json.dumps({"message": res})
    }
    return response  
