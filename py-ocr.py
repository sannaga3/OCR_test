import os
from PIL import Image
import pyocr
import re
import csv

# pyocrで使うOCRエンジンをTesseractに指定。
tools = pyocr.get_available_tools()
tool = tools[0]

img_file = input('読み込む画像ファイルを入力してください: ')

# 画像ファイル読み込み
img = Image.open(img_file)

# 画像から文字の読み込み。精度は一番高い6に設定。
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img, lang="jpn", builder=builder)

# 空白の削除
txt = re.sub('([あ-んア-ン一-龥ー、。]) +((?=[あ-んア-ン一-龥ー、。]))',
      r'\1\2', text)

output_file = input('出力ファイルの名前を入力してください（拡張子不要）: ')

# csvファイルに出力
with open(output_file + '.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerow([txt])
