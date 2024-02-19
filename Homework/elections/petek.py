class Petek():

    def __init__(self, party_char, party_name):
        party_chars = ["A", "B", "L", "Y"]

        if party_char in party_chars and party_name == str(party_name):
            self.party_char = party_char
            self.party_name = party_name
        else:
            self.party_char = None
            self.party_name = None

    def get_party_char(self):
        return self.party_char

    def set_party_char(self, party_char):
        self.party_char = party_char

    def get_party_name(self):
        return self.party_name

    def set_party_name(self, party_name):
        self.party_name = party_name
