import hashlib as hs
import random as rand
import numpy as np


class Certificate:
    name = ""
    email = ""
    student_id = ""
    certificate_name = ""
    certificate_hash = ""
    

    def __init__(self, name, email, student_id, certificate_name):
        self.name = name
        self.email = email
        self.student_id = student_id
        self.certificate_name = certificate_name
        self.certificate_hash = self.generate_certificate_hash()


    def __repr__(self):
        return f"Certificate name: {self.certificate_name}\nName: {self.name}\nCertificate hash: {self.certificate_hash}\n"

    
    """ Generate a hash value for the certificate and returns it's hexadecimal string"""
    def generate_certificate_hash(self):
        text_byte = str(self).encode('utf-8')
        salt_byte = np.int8(rand.randint(0, 100)).tobytes()
        merge_byte = text_byte + salt_byte

        return hs.sha256(merge_byte).hexdigest()
    
    
    def get_certificate_hash(self):
        return self.certificate_hash

    
    
sampleStudent = Certificate("Juan Dela Cruz", "jd@gmail.com", "CO2021-12345", "NSTP Immersion Certificate")
print(sampleStudent)