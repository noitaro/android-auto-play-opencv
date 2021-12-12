from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(path.join(here, '../README.md'), encoding='utf-8_sig') as f:
    long_description = f.read()

setup(
    name='android_auto_play_opencv',  # パッケージ名(プロジェクト名)
    packages=['android_auto_play_opencv'],  # パッケージ内(プロジェクト内)のパッケージ名をリスト形式で指定

    version='1.0.6',  # バージョン

    license='MIT',  # ライセンス

    # pip installする際に同時にインストールされるパッケージ名をリスト形式で指定
    install_requires=['opencv-python', 'numpy'],

    author='noita',  # パッケージ作者の名前
    author_email='noitalog.tokyo@gmail.com',  # パッケージ作者の連絡先メールアドレス

    # パッケージに関連するサイトのURL(GitHubなど)
    url='https://github.com/noitaro/android-auto-play-opencv',

    description='Operate Android using OpenCV.',  # パッケージの簡単な説明
    long_description=long_description,  # PyPIに'Project description'として表示されるパッケージの説明文
    # long_descriptionの形式を'text/plain', 'text/x-rst', 'text/markdown'のいずれかから指定
    long_description_content_type='text/markdown',
    keywords='android auto play opencv',  # PyPIでの検索用キーワードをスペース区切りで指定

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],  # パッケージ(プロジェクト)の分類。https://pypi.org/classifiers/に掲載されているものを指定可能。
)

# python -m venv env1
# pip install wheel twine 
# python setup.py bdist_wheel
# twine upload --repository pypi dist/*
# https://pypi.org/project/android-auto-play-opencv/