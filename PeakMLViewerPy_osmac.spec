# -*- mode: python ; coding: utf-8 -*-

import os
spec_root = os.path.abspath(SPECPATH)

block_cipher = None

a = Analysis(['PeakMLViewerPy.py'],
             pathex=[spec_root],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='PeakMLViewerPy',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='favicon.png')
app = BUNDLE(exe,
             name='PeakMLViewerPy.app',
             icon='favicon.png',
             bundle_identifier=None)
