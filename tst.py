import boto3
from tabulate import tabulate
tabulate.PRESERVE_WHITESPACE = True
# import datetime
client = boto3.client('backup')
response = client.list_backup_jobs()
for resp in response['BackupJobs']:
    # print(resp)
    id=resp['BackupJobId']
    Arn=resp['ResourceArn']
    created_date=resp['CreationDate']
    status=resp['State']
    start_time=resp['StartBy']
    # msg = resp['StatusMessage']
    # Completed_date=resp['CompletionDate']
    x=(f"Backup job id is {id}, creation time is {created_date}, Resource Arn is {Arn} and status is{status}, start_time is{start_time}")
    # print(list(tabulate(x)))
    print(x)