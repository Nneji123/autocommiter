# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(['main.py'],
             pathex=['.'],
             binaries=[],
             datas=[('logo.ico', '.'), ('requirements.txt', '.'), ('utils.py', '.')],
             ...
             # Add any additional options or configurations you need
             )

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          a.pure,
          a.pure,
          ...
          # Add any additional options or configurations you need
          )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               [],
               ...
               # Add any additional options or configurations you need
               )

app = BUNDLE('Autocommiter',
             ...
             # Add any additional options or configurations you need
             )
