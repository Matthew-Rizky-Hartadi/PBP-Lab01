from django.test import TestCase

# Create your tests here.

def test_show_wishlist_ajax_ok(self):
    response = self.client.get("/wishlist/ajax")
    self.assertEquals(200, response.status_code)
    self.assertTemplateUsed(response, "whishlist_ajax.html")