import gnupg
import os
import shutil
import getpass

unenc_file_name='my-unencrypted.txt'
enc_file_name='my-encrypted.gpg'
passphrase = getpass.getpass("Input passphrase: ")
gpg_home = 'gpg_data'
open(unenc_file_name, 'w').write('You need to Google Venn diagram.\n')

def encr_file():

	if os.path.exists(gpg_home):
		shutil.rmtree(gpg_home)
	gpg = gnupg.GPG(homedir=gpg_home)
	key_settings = gpg.gen_key_input(key_type='RSA', key_usage='ESCA', key_length=1024, passphrase=passphrase)
	key = gpg.gen_key(key_settings)
	with open(unenc_file_name, 'rb') as uenc:
	  with open(enc_file_name, 'wb') as enc:
		status = gpg.encrypt(uenc, key.fingerprint, output=enc)
		if status.ok:
			print('encryption status : {}'.format(status.ok))
		else:
			print('encryption status: {}'.format(status.ok))
			print('status: {}'.format(status.status))
			print('stderr: {}'.format(status.stderr))
	os.remove(unenc_file_name)

def decr_file(enc_file, output_file):
	gpg = gnupg.GPG(homedir=gpg_home)
	if os.path.exists(output_file):
		os.remove(output_file)
	with open(enc_file, 'rb') as enc:
		with open(output_file, 'w') as decr:
			status = gpg.decrypt_file(enc, passphrase=passphrase)
			if status.ok:
				decr.write(str(status))
				print('decryption status : {}'.format(status.ok))
				print('Output File :{}'.format(output_file))			
			else:
				print('status: {}'.format(status.status))
				print('stderr: {}'.format(status.stderr))

if __name__ == '__main__':
	#encr_file()
	decr_file(enc_file_name, unenc_file_name)	

