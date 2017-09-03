import os
import shutil
import gnupg
if os.path.exists("doctests"):
    shutil.rmtree("doctests")
gpg = gnupg.GPG(homedir="doctests")
key_settings = gpg.gen_key_input(key_type='RSA',
    key_length=1024,
    key_usage='ESCA',
    passphrase='foo')
key = gpg.gen_key(key_settings)
message = "The crow flies at midnight."
encrypted = str(gpg.encrypt(message, key.fingerprint))
#assert encrypted != message
#assert not encrypted.isspace()
print(encrypted)

decrypted = str(gpg.decrypt(encrypted, passphrase='foo'))
print(decrypted)
#assert not decrypted.isspace()

