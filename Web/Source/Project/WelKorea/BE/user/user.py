class User:
    def __init__(self, no, email, name, password_hash, provider, social_id, created_at):
        self.no = no
        self.email = email
        self.name = name
        self.password_hash = password_hash
        self.provider = provider
        self.social_id = social_id
        self.created_at = created_at