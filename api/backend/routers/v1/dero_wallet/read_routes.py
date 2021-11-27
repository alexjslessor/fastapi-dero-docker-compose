from fastapi import APIRouter
# from typing import Dict, List, Optional, Tuple
# from enum import Enum
import os
from ....rpc import Dero
from ....config.config import get_settings

settings = get_settings()
router = APIRouter()


# def get_all_data():
#     data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getalldata", "params": [0] }'
#     response = requests.post('http://blockchain:45453/', 
#                             headers=headers, 
#                             data=data, 
#                             auth=(settings.PIRATE_USER, 
#                                 settings.PIRATE_PASSWORD))
#     return response

# url2 = 'http://localhost:20209/json_rpc'
# url2 = 'http://blockchain:20209/json_rpc'
url2 = 'http://dero:20209/json_rpc'
# url4 = 'http://localhost:20209/json_rpc'

deroAPI = Dero(rpc_url=url2)

@router.get("/get_info")
def dero_get_info():
    try:
        resp = deroAPI.get_info()
        print('get_info()  ', resp)
        return resp
    except Exception as e:
        return e

@router.get("/get_height")
def get_dero_height():
    try:
        resp = deroAPI.get_height()
        print('get_height()  ', resp)
        return resp
    except Exception as e:
        return e


@router.get("/get_block_count")
def get_dero_block_count():
    try:
        resp = deroAPI.get_block_count()
        print('get_block_count()  ', resp)
        return resp
    except Exception as e:
        return e




# @router.get("/getinfo")
# async def z_getinfo():
#     try:
#         # p = os.popen(f"{settings.KOMODO_CLI} -ac_name=PIRATE getinfo")
#         # print(p)
#         # p = os.popen('/home/hauwei/komodo/src/komodo-cli -ac_name=PIRATE getinfo')
#         # p = p.read()
#         p = get_all_data()
#         print(p)
#         return {'command': p}

#     except Exception as e:
#         print('Exception: ', e)
#         return {'error': 'z_getinfo failed'}































# @router.get("/read/product/{id}", response_model=ReadProduct)
# async def get_product(product: ReadProduct = Depends(get_product_or_404)
#                       ) -> ReadProduct:
#     return product

# @router.get("/read/single_product/{id}", response_description="Get a single product", 
#             response_model=ReadProduct)
# async def single_product(id: str,
#                          current_user: User = Depends(fastapi_users.current_user())):
#     '''Query by sku '''
#     if (p := await db["Products"].find_one({"sku": id})) is not None:
#         return p

#     return exception_400(
#         settings.READ_SINGLE_PROD_ERR, 'red')




# @router.get("/read/single_shipto/{id}", response_description="Read a single shipping address", 
#             response_model=ReadShippingAddress)
# async def single_shipto(id: str, 
#                         current_user: User = Depends(fastapi_users.current_user())):

#     '''Query by _id aka id '''
#     if not ObjectId.is_valid(id):
#         return exception_400(settings.OID_ERROR, 'red')

#     if (p := await db["ShipTo"].find_one({"_id": ObjectId(id)})) is not None:
#         return p

#     return exception_400(
#         settings.READ_SINGLE_SHIPTO_ERR, 'red')


# @router.get("/read/all_shipto", response_description="Read all shipping addresses", 
#             response_model=List[ReadShippingAddress])
# async def all_shipto(
#     current_user: User = Depends(fastapi_users.current_user())):

#     p = await db["ShipTo"].find().to_list(100000)
#     if len(p) > 0:
#         return p

#     return exception_400(
#         settings.READ_ALL_SHIPTO_ERR, 'red')




# @router.get("/read/all_orders/{id}", response_model=List[ReadOrder])
# async def all_orders(id: str,
#                     current_user: User = Depends(fastapi_users.current_user())
#                     ):
#     lst = []
#     for d in await db['Order'].find(
#         {
#             'product_id': ObjectId(id),
#             'status': {'$nin': ['Cancelled', 'Complete', 'Reconcile', 'Shipped']}
#             # 'status': {'$in': ['Pending', 'In Production', 'Acknowledged', 'Back-Ordered']}
#         }).to_list(1000):
#         # print('d: ', d)
#         lst.append(d)
#     return lst


# # @app.post("/posts", response_model=PostDB, status_code=status.HTTP_201_CREATED)
# # async def create_post(
# #     post: PostCreate, database: AsyncIOMotorDatabase = Depends(get_database)
# # ) -> PostDB:
# #     post_db = PostDB(**post.dict())
# #     await database["posts"].insert_one(post_db.dict(by_alias=True))

# #     post_db = await get_post_or_404(post_db.id, database)

# #     return post_db


# # @app.patch("/posts/{id}", response_model=PostDB)
# # async def update_post(
# #     post_update: PostPartialUpdate,
# #     post: PostDB = Depends(get_post_or_404),
# #     database: AsyncIOMotorDatabase = Depends(get_database),
# # ) -> PostDB:
# #     await database["posts"].update_one(
# #         {"_id": post.id}, {"$set": post_update.dict(exclude_unset=True)}
# #     )

# #     post_db = await get_post_or_404(post.id, database)

# #     return post_db


# # @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# # async def delete_post(
# #     post: PostDB = Depends(get_post_or_404),
# #     database: AsyncIOMotorDatabase = Depends(get_database),
# # ):
# #     await database["posts"].delete_one({"_id": post.id})