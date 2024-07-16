from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeSearchViewTest(RecipeTestBase):
    def test_recipe_search_uses_correct_view_function(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?search=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    #criando teste para exibir page 404, caso procure algo que não existe
    def test_recipe_search_raises_404_if_no_term(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
