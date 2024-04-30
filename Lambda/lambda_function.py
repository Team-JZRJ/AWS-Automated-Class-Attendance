import boto3

DATABASE = "newdatatest"
TABLE = "test_table1"


output = "s3://jrjztestbucketeast2/athena_dump_test/"


def lambda_handler(event, context):

    query = "SELECT * FROM %s.%s limit 10;" % (DATABASE, TABLE)

    client = boto3.client("athena")
    s3 = boto3.resource("s3")

    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={"Database": DATABASE},
        ResultConfiguration={"OutputLocation": output},
    )

    queryID = response["QueryExecutionId"]

    queryLocation = f"athena_dump_test/{queryID}.csv"

    source_bucket_name = "jrjztestbucketeast2"
    source_file_key = queryLocation

    destination_bucket_name = "jrjztestbucketcapstone2024"
    destination_file_key = "outputTest.csv"

    # Copy the file
    s3.Object(destination_bucket_name, destination_file_key).copy_from(
        CopySource={"Bucket": source_bucket_name, "Key": source_file_key}
    )

    return
