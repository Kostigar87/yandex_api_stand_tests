import configuration
import requests
import data
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["first_name"] = first_name
    return current_body

def test_crate_user_2_letter_in_first_name_get_success_response():
    user_body = get_user_body("Aa")
    user_response =
