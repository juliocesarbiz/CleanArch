from src.infra.db.repositories.user_repository import UserRepository
from src.data.use_case.user_finder import UserFinder
from src.presentation.controlles.user_finder_controller import UserFinderController

def user_register_composer()
    repository = UserReposi()
    user_case = UserRegister(repository)
    controller = UserRegisterController(user_case)

    return controller.handle

