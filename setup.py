from setuptools import setup, find_packages

name = 'inouk.recipe.odoo_cmd'
version = '0.2'


long_description = (
    '\nDetailed Documentation\n'
    '######################\n'
    + '\n' +
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '############\n'
    + '\n' +
    open('contributors.txt').read()
    + '\n' +
    'Change history\n'
    '##############\n'
    + '\n' +
    open('changes.txt').read()
    + '\n'
)

setup(
    name=name,
    version=version,
    packages=find_packages('src'),
    namespace_packages=['inouk', 'inouk.recipe'],
    package_dir={'': 'src'},
    url='https://github.com/cmorisse/inouk.recipe.odoo_cmd',
    license='MIT',
    author='Cyril MORISSE',
    author_email='cmorisse@boxes3.net',
    description='Add odoo.py command to odoo appserver generated by anybox.recipe.odoo.',
    long_description=long_description,
    keywords="openerp odoo recipe command",
    include_package_data=True,
    install_requires=['setuptools',],
    classifiers=[
        'Framework :: Buildout :: Recipe',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python',
        'Natural Language :: English',
    ],
    entry_points="""

    [console_scripts]
    odoo_cmd = inouk.recipe.odoo_cmd:buildout_entry_point
    """
)
