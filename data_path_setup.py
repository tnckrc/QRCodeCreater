import os
import pandas as pd
import qrcode
import openpyxl



CURRENT_DIR = os.getcwd()
QR_DIR = "QRCodes"


class DatasetPathSetUp:
    
    def __init__(self, data_path, qr_path=None):

        # Veri yolu (data_path) ve QR kodu yolu (qr_path) parametreleri alır.
        # Eğer veri yolu belirtilmemişse, geçerli çalışma dizinini kullanır.
        self.data_path = data_path if data_path else CURRENT_DIR
        self.qr_path = (
            os.path.join(qr_path, QR_DIR)
            if qr_path
            else os.path.join(self.data_path, QR_DIR)
        )


    def create_folder(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

    def create_qr(self, limit=None):
        # data_path'daki tüm veriler listelenir
        for dirpath, dirnames, filenames in os.walk(self.data_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                
                if filename.endswith('.xlsx'):
                    dataset = pd.read_excel(file_path,engine="openpyxl")
                    
                    dataset_row_size = len(dataset.iloc[:, 0])

                    limit_size = limit if limit else dataset_row_size
                    
                    
                    for index in range(limit_size):
                        first_name = dataset["first_name"][index]
                        last_name = dataset["last_name"][index]

                        data = f"First Name: {first_name}\nLast Name: {last_name}"
                        

                        qr = qrcode.make(data)
                        self.create_folder(self.qr_path)
                        qr.save(f'{self.qr_path}/{first_name}_{last_name}.png')


path_setup = DatasetPathSetUp(data_path="C:\qr")
#gereksiz işlem olmaması için veri sayısına göre limit belirledim
print(path_setup.create_qr(limit=6)) 