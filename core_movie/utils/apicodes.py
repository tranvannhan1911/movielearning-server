class ApiCode():
    def toDict(total, count=1, message="", data=None):
        return {
            "total": total,
            "count":count,
            "message": message,
            "data": data
        }

    def success(total=1, count=1, message="success", data=None):
        return ApiCode.toDict(total, count, message, data)

    def success_list(total=1, count=1, message="success", lst=None):
        return ApiCode.toDict(total, message, data={
            "count": count,
            "results": lst
        })

    def error(total=0, message="error", data=None):
        return ApiCode.toDict(total, message, data)

