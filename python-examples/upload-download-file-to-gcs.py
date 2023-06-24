from google.cloud import storage

# Prerequisites:
# pip install google.cloud.storage
# export GOOGLE_APPLICATION_CREDENTIALS with the file path of service account that has cloud storage access.
# Or follow some other menthod here for authentication:- https://cloud.google.com/docs/authentication/provide-credentials-adc

def uploadBlob(bucketName, sourceFileName, destinationBlobName):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucketName = "your-bucket-name"
    # The path to your file to upload
    # sourceFileName = "local/path/to/file"
    # The ID of your GCS object
    # destinationBlobName = "storage-object-name"

    storageClient = storage.Client()
    bucket = storageClient.bucket(bucketName)
    blob = bucket.blob(destinationBlobName)

    # Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to upload is aborted if the object's
    # generation number does not match your precondition. For a destination
    # object that does not yet exist, set the if_generation_match precondition to 0.
    # If the destination object already exists in your bucket, set instead a
    # generation-match precondition using its generation number.
    generation_match_precondition = 0

    blob.upload_from_filename(sourceFileName, if_generation_match=generation_match_precondition)

    print(
        f"File {sourceFileName} uploaded to {destinationBlobName}."
    )

def downloadBlob(bucketName, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # The ID of your GCS bucket
    # bucketName = "your-bucket-name"

    # The ID of your GCS object
    # source_blob_name = "storage-object-name"

    # The path to which the file should be downloaded
    # destination_file_name = "local/path/to/file"

    storageClient = storage.Client()

    bucket = storageClient.bucket(bucketName)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Downloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucketName, destination_file_name
        )
    )


if __name__ == "__main__":
    uploadBlob(bucketName="your-bucket-name", sourceFileName="local/path/to/file", destinationBlobName="storage-object-name")
    downloadBlob(bucketName="your-bucket-name", source_blob_name="storage-object-name", destination_file_name="local/path/to/file")
