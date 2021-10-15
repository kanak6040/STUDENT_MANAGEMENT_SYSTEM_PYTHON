from cx_Freeze import *
includefiles = ['profile.ico']
excludes= []
packages= []
base = None

shortcut_table = [
    ("Desktop Shortcut",
    "Desktop Folder",
    "StudentManagementSystem",
    "TARGETDIR",
    "[TARGETDIR]\StudentManagementSystem.exe",
    None,
    None,
    None,
    None,
    None,
    None,
    "TARGETDIR")
]

msi_data = {"Shortcut": shortcut_table}

bdlist_msi_options = {'data': msi_data}
setup(
    version = "0.1",
    description = "Student Management System",
    author = "Kanak Agrawal",
    name = "Student Management System",
    options={'build.exe': {'include_files': includefiles}, 'bdlist_msi': bdlist_msi_options, },
    executables=[
        Executable(
            script="studentmanagementsystem.py",
            base=base,
            icon='profile.ico',
        )
    ]
)