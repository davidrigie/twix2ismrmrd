from setuptools import setup

setup(      name='converter',
            version='0.1',
            description='convert twix folder to h5',
            author='David Rigie',
            license='MIT',
            python_requires='>3.0.0',
            packages=['converter'],
            entry_points = {
                  'console_scripts': ['twixconvert=converter.command_line:main'],
            },
            zip_safe=False
    )