import hashlib as hs
import random as rand
import numpy as np


class Certificate:
    name = ""
    email = ""
    student_id = ""


    def __init__(self, name, email, student_id):
        self.name = name
        self.email = email
        self.student_id = student_id


    def __repr__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.student_id}"


    """ Generate a hash value for the certificate and returns it's hexadecimal string"""
    def generate_certificate_hash(self):
        text_byte = str(self).encode('utf-8')
        salt_byte = np.int8(rand.randint(0, 100)).tobytes()
        merge_byte = text_byte + salt_byte

        return hs.sha256(merge_byte).hexdigest()

print("CEVAS Certificate Generator")