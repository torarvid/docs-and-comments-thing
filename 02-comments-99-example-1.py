# Check if input is valid
def is_valid(request):
    if (
        not isinstance(request.query_params["first_name"], str)
        or not isinstance(request.query_params["last_name"], str)
        or not isinstance(request.query_params["age"], str)
    ):
        return False
    return True







###### could instead drop the comment:


def check_if_input_is_valid(request):
    if (
        not isinstance(request.query_params["first_name"], str)
        or not isinstance(request.query_params["last_name"], str)
        or not isinstance(request.query_params["age"], str)
    ):
        return False
    return True








###### code could also be more self-documenting:


def check_if_input_is_valid_2(request: starlette.Request):
    first_name_is_string = isinstance(request.query_params["first_name"], str)
    last_name_is_string = isinstance(request.query_params["last_name"], str)
    age_is_string = isinstance(request.query_params["age"], str)
    return first_name_is_string and last_name_is_string and age_is_string
