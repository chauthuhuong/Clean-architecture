from Entities.Category import Category
from Infrastructure.CategoryRepository import CategoryRepository

class CreateCategoryUseCase:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def execute(self, name: str, description: str) -> str:
        existing_category = self.category_repository.find_by_name(name)
        if existing_category:
            return "Category already exists."

        new_category = Category(name=name, description=description)
        self.category_repository.save(new_category)
        return "Category created successfully."
