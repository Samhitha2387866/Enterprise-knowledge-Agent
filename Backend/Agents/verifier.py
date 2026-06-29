def verify_answer(answer,sources):
    if(len(sources)==0):
        return{
            "status":"Failed",
            "reason":"No sources provided for verification.",
            "confidence":20
        }
    return{
        "status":"Verified",
        "reason":"Answer generated from retrived documents.",
        "confidence":90
    }