class ApiCode():
    def toDict(message="", data=None):
        return {
            "message": message,
            "data": data
        }

    def success(total=1, count=1, message="success", data=None):
        return ApiCode.toDict(message, data)

    def success_list(total=1, count=1, message="success", lst=None):
        return ApiCode.toDict(message=message, data={
            "count": count,
            "results": lst
        })

    def error(total=0, message="error", data=None):
        return ApiCode.toDict(message=message, data=data)

