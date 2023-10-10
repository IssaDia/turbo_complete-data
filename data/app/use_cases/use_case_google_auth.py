class AuthenticationUseCase:
    def __init__(self, auth_provider):
        self.auth_provider = auth_provider

    def login(self, user_credentials):
        self.auth_provider.authenticate(user_credentials)

    def logout(self):
        self.auth_provider.sign_out()