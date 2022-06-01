from clients.user_client import UserClient
from checkers import checkers as check


class TestUser:

    def test_create_user(self, generated_user):
        create_user_response = UserClient().get_user_endpoints().create(generated_user)
        check.check_default_response(create_user_response, 200, 'unknown', str(generated_user.id))

    def test_get_user(self, existing_user):
        create_user_response = UserClient().get_user_endpoints().find(existing_user)
        check.validate_user(create_user_response, 200, existing_user)

    def test_get_not_existing_user(self, existing_user):
        existing_user.username = 'invalid name'
        create_user_response = UserClient().get_user_endpoints().find_invalid(existing_user)
        check.check_default_response(create_user_response, 404, 'error', 'user not found')

    def test_update_user(self, existing_user, generated_user):
        generated_user.id = existing_user.id
        create_user_response = UserClient().get_user_endpoints().update(existing_user, generated_user)
        check.check_default_response(create_user_response, 200, 'unknown', str(generated_user.id))
        create_user_response = UserClient().get_user_endpoints().find(generated_user)
        check.validate_user(create_user_response, 200, generated_user)

    def test_delete_user(self, existing_user):
        create_user_response = UserClient().get_user_endpoints().delete(existing_user)
        check.check_default_response(create_user_response, 200, 'unknown', str(existing_user.username))
        create_user_response = UserClient().get_user_endpoints().find_invalid(existing_user)
        check.check_default_response(create_user_response, 404, 'error', 'user not found')

    def test_delete_not_existing_user(self, generated_user):
        create_user_response = UserClient().get_user_endpoints().delete(generated_user)
        assert create_user_response.status_code == 404

    def test_login_valid_user(self, existing_user):
        create_user_response = UserClient().get_user_endpoints().login(existing_user)
        check.check_login_response(create_user_response, 200, 'unknown', 'logged in user session')
