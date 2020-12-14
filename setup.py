from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'dpy_helper',
    version = '0.0.1',
    description = 'discord.py를 이용한 봇개발에 도움을 주는 코드입니다!',
    author = 'Bainble0211',
    author_email = 'bainble0211@bainble.ga',
    url = 'https://github.com/Bainble0211-6109/Discord_Helper',
    project_urls={
        "Homepage": "https://pp.bainble.ga",
        "Source":"https://github.com/Bainble0211-6109/Discord_Helper",
        "Tracker":"https://github.com/Bainble0211-6109/Discord_Helper/issues"
    },
    install_requires =  ['aiohttp', 'asyncio', 'discord.py'],
    keywords = ['discord', 'discord.py', 'discord_helper', 'discord-helper', 'DiscordHelper'],
    license='GPL-3.0',
    long_description = long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ]
)
