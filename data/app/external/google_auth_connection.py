from app.interfaces.auth_provider_interface import AuthenticationProvider

class GoogleAuthProvider(AuthenticationProvider):
    def authenticate(self, user_credentials):
        # Implement Google Authentication logic here
        pass

    def sign_out(self):
        # Implement sign-out logic here
        pass