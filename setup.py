from setuptools import setup

setup(name='ndasynapse',
      version='0.1',
      description='NDA to Synapse sync',
      url='http://github.com/bsmn/ndasynapse',
      author='Kenneth Daily',
      author_email='kenneth.daily@sagebase.org',
      license='MIT',
      packages=['ndasynapse'],
      install_requires=['synapseclient>=1.7.2',
                        'numpy==1.13.1',
                        'pandas>=0.20.3',
                        'boto3>=1.4.2',
                        'boto>=2.46.1',
                        'requests>=2.18.1'],
      dependency_links=['https://github.com/NDAR/nda_aws_token_generator/tarball/master/#egg=nda-aws-token-generator&subdirectory=python'],
      scripts=['bin/nda_to_synapse_manifest.py'],
      zip_safe=False)
