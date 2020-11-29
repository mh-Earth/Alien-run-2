# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Alien Run2.py'],
             pathex=['C:\\Users\\speed\\Desktop\\python game-20201104T144037Z-001\\python game\\python game\\Alien Run2'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Alien Run2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='D:\\We4ponx-Dead-Space-3-Dead-Space-3-3.ico')
