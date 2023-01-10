import json
from secrets import choice
from drf_yasg import openapi
from core_movie.serializers import ResponeSuccessSerializer
from core_movie.utils.apicodes import ApiCode
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class SwaggerSchema():

    token = openapi.Parameter("Authorization", in_=openapi.IN_HEADER, type=openapi.TYPE_STRING, required=True)
    movie_id = openapi.Parameter("movie_id", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=False)
    movie_category_id = openapi.Parameter("movie_category_id", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=False)
    date_required = openapi.Parameter("date", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True)

    @staticmethod
    def success():
        return openapi.Response(
            description="Successful",
            schema=ResponeSuccessSerializer,
            examples={
                "application/json": ApiCode.success()
            }
        )

def get_example(name):
    f = open(dir_path+'/examples/'+name+'.json', encoding="utf8")
    data = "hello"
    # print(data)
    return {
        "get": openapi.Response(
                description="Successful",
                examples={
                    "application/json": ApiCode.success(data=data)
                    }),
        "list": openapi.Response(
                description="Successful",
                examples={
                    "application/json": ApiCode.success_list(lst=[data])
                    }),
    }


token = openapi.Response(
    description="Successful",
    examples={
        "application/json": ApiCode.success(data={
            "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NiwicGhvbmUiOiIwMzY5NDYyMzA4In0.h1V-mVuoJgWQuPJzrx-miA6mo_f8QECSE8f1UCHxzY0",
            "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwMTA0NTE2LCJpYXQiOjE2Njc1MTI1MTYsImp0aSI6ImM5MmZjOTY5NzNlYTRiNWM5NzhjYTUyNTVmOTBiOWY2IiwiaWQiOjYsInBob25lIjoiMDM2OTQ2MjMwOCJ9.NMOIQgi9ZHWp_T4EbpLFHdKgRgs_YbXJcNGoC8QIi9M"
        })
    })

movie_info = get_example("info")
movie_sub = get_example("subs")



