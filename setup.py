from setuptools import setup
setup(
        name="merzbow",
        version="0.1",
        py_modules=["merzbow"],
        install_requires=[
            "Click",
        ],
        entry_points='''
            [console_scripts]
            merzbow=merzbow:merzbow
        ''',
)
