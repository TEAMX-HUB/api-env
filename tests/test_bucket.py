# def upload_to_bucket(supabase, database_connection):
#     if supabase.storage.list_buckets():
#         storage = supabase.storage.get_bucket(id=bucket_name)

#         with open(filename, "rb") as f:
#             storage.upload(path="data.png", file=f)
#     else:
#         return "Not Buckets Founds"

#     return storage


def list_buckets(supabase):
    assert supabase.storage.list_buckets()
