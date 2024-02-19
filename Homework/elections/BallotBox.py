import  petek
class BallotBox():
    def __init__(self, num_of_ballot):
        self.num_of_ballot = num_of_ballot
        self.ptakim = [None] * 100
        self.count = 0

    def get_num_of_ballot(self):
        return self.num_of_ballot

    def set_num_of_ballot(self, num):
        self.num_of_ballot = num

    def get_ptakim(self):
        return self.ptakim

    def add_petek(self, petek):
        if self.count <= len(self.ptakim):
            for index in range(len(self.ptakim)):
                if self.ptakim[index] == None:
                    self.ptakim[index] = petek
                    self.count += 1
                    break


def get_details(ballotbox):
    A = 0
    B = 0
    L = 0
    Y = 0

    for petek in ballotbox.get_ptakim():
        if petek is not None:
            if petek.party_char == "A":
                A += 1
            elif petek.party_char == "B":
                B += 1
            elif petek.party_char == "L":
                L += 1
            elif petek.party_char == "Y":
                Y += 1
    return f"A = {A}\nB = {B}\nL = {L}\nY = {Y}"

mmm = BallotBox(12)
mmm.add_petek(petek.Petek("A", "mendy"))
mmm.add_petek(petek.Petek("A", "mendy"))
mmm.add_petek(petek.Petek("A", "mendy"))
mmm.add_petek(petek.Petek("A", "mendy"))
mmm.add_petek(petek.Petek("A", "mendy"))
mmm.add_petek(petek.Petek("A", "mendy"))
mmm.add_petek(petek.Petek("A", "mendy"))
mmm.add_petek(petek.Petek("A", "mendy"))
mmm.add_petek(petek.Petek("A", "mendy"))
mmm.add_petek(petek.Petek("A", "mendy"))
mmm.add_petek(petek.Petek("Y", "mendy"))

print(get_details(mmm))
