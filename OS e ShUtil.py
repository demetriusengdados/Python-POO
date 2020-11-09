import os
import shutil

caminho_original = '/media/demetrius/Externo/serie'
caminho_novo = '/media/demetrius/Externo/serie2'

try:
  os.mkdir(caminho_novo)
except FileExistsError as e:
  print(f'pasta{caminho_novo} já existe')
  
for root, dirs, files in os.walk(caminho_novo):
  for file in files:
    old_file_path = os.path.join(root, file)
    new_file_path = os.path.join(caminho_novo, file)
    
    print(new_file_path)
    
    if '.srt' in file:
      os.remove(new_file_path)
    
    if '.srt' in file:
      shutil.move(old_file_path, new_file_path)
      print(f'Arquivo {file} movido com sucsso')
    