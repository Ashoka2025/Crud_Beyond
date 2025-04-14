from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException
from fastapi import status, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
# from .routes import AccessTokenBearer
from src.books.schemas import BookDetail
from typing import List, Any

# from src.auth.service import user_service
from src.auth.dependencies import get_session
from .models import User
from src.auth.utils import get_token_payload



class AccessTokenBearer(HTTPBearer):
    async def get_current_user(
            token_details: dict = Depends(AccessTokenBearer()),
            session: AsyncSession = Depends(get_session),
    ):
            user_email = token_details["user"]["email"]

            user = await user_service.get_user_by_email(user_email, session)

            return user
    
class RoleChecker:
      def __init__(self, allowed_roles: List[str]) -> None:
            self.allwed_roles = allowed_roles

      def __call__(self, current_user: User = Depends(get_current_user)) -> Any:
            if current_user.role in self.allwed_roles:
                  return True
            raise HTTPException(
                  status_code = status.HTTP_403_FORBIDDEN,
                  detail = "You are not allowed to perform this action."
            )
