import PyInstaller.__main__


PyInstaller.__main__.run([
	'bvc_timer_version2.0.py',
        '--onedir',
        '--onefile',
        '--windowed',
        '-n' 'BVC Timer',
        '-i' 'icon_for_program.ico'
    ])
