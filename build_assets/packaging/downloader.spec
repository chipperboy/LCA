# -*- mode: python ; coding: utf-8 -*-

import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

block_cipher = None

# PySide6 插件路径
import sys
if hasattr(sys, '_MEIPASS'):
    pyside6_path = os.path.join(sys._MEIPASS, 'PySide6')
else:
    import PySide6
    pyside6_path = os.path.dirname(PySide6.__file__)
pyside6_plugins = os.path.join(pyside6_path, 'plugins')

a = Analysis(
    [os.path.join(project_root, 'online_downloader.py')],
    pathex=[project_root],
    binaries=[],
    datas=[
        # PySide6 Qt平台插件 - 修复"no Qt platform plugin could be initialized"错误
        (pyside6_plugins + '/platforms', 'PySide6/plugins/platforms'),
        # 图标文件
        (os.path.join(project_root, 'resources', 'icon.ico'), 'resources'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # 排除大型库
        'matplotlib', 'numpy', 'pandas', 'PIL', 'opencv', 'torch', 'tensorflow',
        'scipy', 'sklearn', 'IPython', 'notebook', 'jupyter',
        # 排除不需要的PySide6模块
        'PySide6.QtWebEngineCore', 'PySide6.QtWebEngineWidgets',
        'PySide6.QtWebChannel', 'PySide6.Qt3DCore', 'PySide6.Qt3DRender',
        'PySide6.QtDataVisualization', 'PySide6.QtCharts', 'PySide6.QtQuick',
        'PySide6.QtQml', 'PySide6.QtMultimedia', 'PySide6.QtMultimediaWidgets',
        'PySide6.QtPrintSupport', 'PySide6.QtSvg', 'PySide6.QtSvgWidgets',
        'PySide6.QtTest', 'PySide6.QtDesigner', 'PySide6.QtHelp',
        'PySide6.QtNetwork', 'PySide6.QtOpenGL', 'PySide6.QtOpenGLWidgets',
        'PySide6.QtPositioning', 'PySide6.QtSensors', 'PySide6.QtSerialPort',
        'PySide6.QtSql', 'PySide6.QtXml', 'PySide6.QtBluetooth', 'PySide6.QtNfc',
        # 排除其他不需要的模块（保留email，urllib需要）
        'tkinter', 'test', 'unittest', 'distutils', 'setuptools',
        'http.server', 'xmlrpc', 'pydoc',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# 进一步过滤二进制文件（保留必需的Qt DLL和插件）
excluded_binaries = []
for x in a.binaries:
    # 排除不需要的Qt模块DLL
    if x[0].startswith('PySide6\\Qt'):
        # 保留Core、Gui、Widgets及其依赖
        if any(keep in x[0] for keep in ['Core', 'Gui', 'Widgets', 'plugins\\platforms']):
            continue
        else:
            excluded_binaries.append(x)

a.binaries = [x for x in a.binaries if x not in excluded_binaries]

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='护肝小助手下载器',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=['qwindows.dll', 'qwindowsvistastyle.dll'],  # 排除Qt平台插件DLL的UPX压缩
    runtime_tmpdir=None,
    console=False,  # 无控制台窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(project_root, 'resources', 'icon.ico'),  # 使用项目图标
)
