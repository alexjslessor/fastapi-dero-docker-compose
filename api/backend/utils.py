# import os
# import six
# from json import loads
# from os import environ
# from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
# from fastapi_mail.email_utils import DefaultChecker
# from datetime import date

# def get_base64_encoded_image(image_path):
#     with open(image_path, "rb") as img_file:
#         img_bytes = base64.b64encode(img_file.read()).decode('utf-8')
#         return str(img_bytes)

# class ORJSONEncoder:
#     def default(self, obj):
#         if isinstance(obj, datetime):
#             return obj.__str__()
#         elif isinstance(obj, Decimal):
#             return str(obj)
#         # elif isinstance(obj, ApiQuerySet):
#             # return str(obj)
#         else:
#             return str(obj)
#         raise TypeError

# def loads_encoder(obj):
#     if isinstance(obj, datetime):
#         return obj.__str__()
#     elif isinstance(obj, Decimal):
#         return str(obj)
#     else:
#         return str(obj)
#     raise TypeError