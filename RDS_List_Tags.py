import boto3

client = boto3.client('rds')

response = client.list_tags_for_resource(
    ResourceName='arn:aws:rds:eu-west-1:378457291432:db:afrprdcst01',
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