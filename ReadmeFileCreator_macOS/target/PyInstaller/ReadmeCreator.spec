# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['/Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/src/main/python/main.py'],
             pathex=['/Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/venv/lib/python3.7/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/target/PyInstaller/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='ReadmeCreator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='/Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='ReadmeCreator')
app = BUNDLE(coll,
             name='ReadmeCreator.app',
             icon='/Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/target/Icon.icns',
             bundle_identifier=None)
