from runnerly import create_app
from runnerly.forms import UserForm
import pytest


# Check if route is present
# Check if list of users returns
# check if UserForm exists
# check if UserForm has all fields

def test_userform_is_complete():
    testapp = create_app()
    fields = ['email', 'firstname', 'lastname', 'password', 'age', 'weight',
            'max_hr', 'rest_hr', 'vo2max', 'csrf_token']
    with testapp.test_request_context() as ctx:
        form = UserForm()
        for field in form._fields:
            assert field in fields, f"Unexpected {field} in UserForm"
            fields.pop(fields.index(field))
        assert fields == 0, f"{fields} are not implemented yet"


