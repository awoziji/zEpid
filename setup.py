from setuptools import setup

exec(compile(open('zepid/version.py').read(),
             'zepid/version.py', 'exec'))


with open("README.md") as f:
    descript = f.read()


setup(name='zepid',
      version=__version__,
      description='Tool package for epidemiologic analyses',
      keywords='epidemiology inverse-probability-weights risk-ratio g-computation g-formula IPW AIPW TMLE',
      packages=['zepid',
                'zepid.calc',
                'zepid.graphics',
                'zepid.sensitivity_analysis',
                'zepid.causal.ipw',
                'zepid.causal.gformula',
                'zepid.causal.doublyrobust',
                'zepid.causal.generalize',
                'zepid.causal.snm',
                'zepid.datasets'],
      include_package_data=True,
      license='MIT',
      author='Paul Zivich',
      author_email='zepidpy@gmail.com',
      url='https://github.com/pzivich/zepid',
      classifiers=['Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7'],
      install_requires=['pandas>=0.18',
                        'numpy',
                        'statsmodels>=0.7.0',
                        'matplotlib>=2.0,<3.1; python_version<"3.6"',
                        'matplotlib>=2.0; python_version>="3.6"',
                        'scipy',
                        'tabulate',
                        'patsy'],
      long_description=descript,
      long_description_content_type="text/markdown",
      )
