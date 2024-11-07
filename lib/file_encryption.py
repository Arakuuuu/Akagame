import os
import base64
from hashlib import sha256
from hmac import compare_digest

class FileEncryption:
    def __init__(self):
        self.chunk_size = 64 * 1024
        
    def derive_key(self, password):
        """Derive encryption key from password."""
        return sha256(password.encode()).digest()
        
    def encrypt_file(self, filename, password):
        """Encrypt a file using XOR cipher (for demonstration)."""
        key = self.derive_key(password)
        key_length = len(key)
        
        with open(filename, 'rb') as f_in:
            with open(f"{filename}.encrypted", 'wb') as f_out:
                i = 0
                while chunk := f_in.read(self.chunk_size):
                    encrypted = bytes(b ^ key[i % key_length] 
                                   for i, b in enumerate(chunk))
                    f_out.write(encrypted)
                    i += len(chunk)
                    
    def decrypt_file(self, filename, password):
        """Decrypt a file using XOR cipher (for demonstration)."""
        if not filename.endswith('.encrypted'):
            raise ValueError("File must have .encrypted extension")
            
        key = self.derive_key(password)
        key_length = len(key)
        output_filename = filename[:-10] + '.decrypted'
        
        with open(filename, 'rb') as f_in:
            with open(output_filename, 'wb') as f_out:
                i = 0
                while chunk := f_in.read(self.chunk_size):
                    decrypted = bytes(b ^ key[i % key_length] 
                                    for i, b in enumerate(chunk))
                    f_out.write(decrypted)
                    i += len(chunk)