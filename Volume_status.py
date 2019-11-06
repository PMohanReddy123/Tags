import boto3

client = boto3.client('ec2')
response = client.describe_volumes(
    Filters=[
#         {
#             'Name': 'status',
#             'Values': [ #'Name'
#                 'available' #'in-use',
#             ]
#         },
#     ]
# )
        {
            'Name': 'tag-key',
            'Values': ['Name'
                # 'available','in-use',
            ]
        },
        {
            'Name': 'tag-key',
            'Values': ['Cost Center'
            ]
        },
{
            'Name': 'tag-key',
            'Values': ['Department'
            ]
        },
        {
            'Name': 'tag-key',
            'Values': ['Environment'
            ]
        },
        {
            'Name': 'tag-key',
            'Values': ['Application'
            ]
        }
    ],
)
for resp in response['Volumes']:
    tags=resp['Tags']
    state=resp['State']
    vol_id=resp['VolumeId']
    print("vol id is {} and its state is {}, tags are {}".format(vol_id,state,tags))
