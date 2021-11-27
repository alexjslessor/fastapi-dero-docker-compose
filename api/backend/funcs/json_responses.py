from fastapi.responses import JSONResponse
from fastapi import HTTPException, status

def error_400(message, color):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, 
                        content={"message": f"{message}", 
                                 "color": f"{color}"})

def exception_400(message, color):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                        detail={"message": f"{message}", 
                                 "color": f"{color}"})


def json_resp_success_200(message, color):
    '''returns status 204_NO_CONTENT'''
    # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    return JSONResponse(status_code=status.HTTP_200_OK, 
                        content={"message": f"{message}", 
                                 "color": f"{color}"})

