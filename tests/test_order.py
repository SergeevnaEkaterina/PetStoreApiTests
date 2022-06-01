from clients.order_client import OrderClient
from checkers import checkers as check


class TestOrder:

    def test_create_order(self, generated_order):
        create_order_response = OrderClient().get_order_endpoints().create(generated_order)
        check.validate_order(create_order_response, 200, generated_order)

    def test_find_order_by_id(self, existing_order):
        create_order_response = OrderClient().get_order_endpoints().find(existing_order)
        check.validate_order(create_order_response, 200, existing_order)

    def test_find_order_by_invalid_id(self, existing_order):
        existing_order.id = -1
        create_order_response = OrderClient().get_order_endpoints().find_invalid(existing_order)
        check.check_default_response(create_order_response, 404, 'error', 'order not found')

    def test_find_order_by_not_existing_id(self, generated_order):
        create_order_response = OrderClient().get_order_endpoints().find_invalid(generated_order)
        check.check_default_response(create_order_response, 404, 'error', 'order not found')

    def test_delete_order(self, existing_order):
        create_order_response = OrderClient().get_order_endpoints().delete(existing_order)
        check.check_default_response(create_order_response, 200, 'unknown', str(existing_order.id))

    def test_delete_not_existing_order(self, generated_order):
        create_order_response = OrderClient().get_order_endpoints().delete(generated_order)
        check.check_default_response(create_order_response, 404, 'unknown', 'order not found')

    def test_delete_order_with_invalid_id(self, existing_order):
        existing_order.id = -1
        create_order_response = OrderClient().get_order_endpoints().delete(existing_order)
        check.check_default_response(create_order_response, 404, 'unknown', 'order not found')
