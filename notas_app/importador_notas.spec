# -*- mode: python ; coding: utf-8 -*-

import sys
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

a = Analysis(
    ['main.py'],  # seu arquivo principal
    pathex=[],
    binaries=[],
    datas=[
        ('ui/**/*', 'ui'),
        ('utils/**/*', 'utils'),
        ('xmls/**/*', 'xmls'),
        ('config.py', '.'),
        ('icone.png', '.'),
        ('icone.ico', '.'),
        ('Nota_Devolucao.xlsx', '.'),  # sua planilha
    ],
    hiddenimports=collect_submodules('ui') + collect_submodules('utils'),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ImportadorNotas',  # nome do .exe
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Oculta console
    icon='icone.ico',  # Ícone do executável
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ImportadorNotas'
)
