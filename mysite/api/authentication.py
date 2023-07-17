from rest_framework.authentication import TokenAuthentication as Base


class TokenAuthentication(Base):
    keyword = "Bearer"
