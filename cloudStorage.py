import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BH_6hvNvyisB-DcnwszjvGjw7BKE7dBGEeM2S5QbGFKQOwhh7lKiNEH7mfEqajzwFk1eSaLym1FjF91PqmL8si6u8m5zv2sw13R3UcmjYYgNcTIOLed3_dYDbCKQ6MI3__4_7_3RXgc'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("file has been moved!")

main()