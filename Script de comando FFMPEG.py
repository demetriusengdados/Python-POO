import os
import fnmatch
import sys

if sys.platform == 'linux':
  comando_ffmpeg = 'ffmpeg'
else:
  comando_ffmpeg = r'ffmpeg\ffmpeg.exe'
  
codec_video = 'libx264'
crf = '-crf23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 - to 00:00:10'

caminho_origem = '/home/demetrius/Desktop/videos'
caminho_destino = '/home/demetrius/Desktop/saida'

for raiz, pastas, arquivos in os.walk(caminho_origem):
  for arquivo in arquivos:
    if not fnmatch.fnmatch(arquivo, '*mp4'):
      continue
    
    caminho_completo = os.path.join(raiz, arquivo)
    nome_arquivo, extensão_arquivo = os.path.splitext(caminho_completo)
    caminho_legenda = nome_arquivo + '.srt'
    
    if os.path.isfile(caminho_legenda):
      input_legenda = f'-i "{caminho_legenda}"'
      map_legenda = '-c:s srt -map v:0 -map a - map 1:0'
    else:
      input_legenda = ''
      map_legenda = ''
      
    nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
      
    arquivo_saida = f'{caminho_destino}/{nome_arquivo} novo.mp4'
      
    comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} '\
      f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
      f'{debug} "{arquivo_saida}"'
     
      
    os.system(comando)  
    print(comando)
    