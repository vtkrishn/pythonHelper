from setuptools import setup, find_packages
setup(
	name='vtkrishn',
	version='0.1.0',
	description='Simple Project',
	url='https://github.com/vtkrishn/pythonHelper',
	author='Vinod Krishnan',
	author_email='vin.sinin@gmail.com',
	license='MIT',
	classifiers=['Development Status :: 3 - Alpha',
	'Intended Audience :: Developers',
	'Topic :: Software Development :: Build Tools',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 2.7'
	],
	entry_points={
    'console_scripts': [
        'vtkrishn=vtkrishn:main',
    ],
	},
)