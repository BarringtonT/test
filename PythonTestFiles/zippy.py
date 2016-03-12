import zipfile

print( "Creating a Zip File.....")

zf = zipfile.ZipFile("Python_zipfile.zip", mode='w')
try:
    # Add file to our zip.
    zf.write('user.py')
finally:
    print('closing')
    zf.close()
