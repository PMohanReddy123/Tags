{
    "Reservations": [{"Instances": [
        {
            "InstanceId": "id-target1",
            "Tags": [
                {"Key": "Data", "Value": "foo=yes,bar=no"},
                {"Key": "Name", "Value": "target"}
            ]
        },
        {
            "InstanceId": "id-target2",
            "Tags": [
                {"Key": "Data", "Value": "foo=yes,bar=yes"},
                {"Key": "Name", "Value": "target"}
            ]
        },
        {
            "InstanceId": "id-invalid1",
            "Tags": [
                {"Key": "Data", "Value": "foo=no,bar=no"},
                {"Key": "Name", "Value": "invalid"}
            ]
        },
        {
            "InstanceId": "id-invalid2",
            "Tags": [
                {"Key": "Data", "Value": "foo=no,bar=yes"},
                {"Key": "Name", "Value": "invalid"}
            ]
        }
    ]}]
}