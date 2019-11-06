import boto3

client = boto3.client('rds')

response = client.list_tags_for_resource(
    ResourceName='',
    # Filters=[
    #     {
    #         'Name': 'workload-type',
    #         'Values': [
    #             'production',
    #         ]
    #     },
    # ]
)
print(response)
