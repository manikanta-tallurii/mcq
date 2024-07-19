from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='manikanta',
    author_email='manikanta.talluii@gmail.com',
    packages=['openai', 'langchain', 'streamlit', 'python-dotenv', 'pyPDF2']
)