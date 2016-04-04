#encoding:utf8

from distutils.core import setup

setup(
	name="Flask-WeChat",
	packages=["flask_wechat"],
	version="0.0.2",
	author="Xavier-Lam",
    author_email="lam.xavier@hotmail.com",
	description="a simple flask module implement wechat api",
	url="https://github.com/Xavier-Lam/flask-wechat",
	install_requires=[
		"Flask==0.10.1",
		"requests==2.9.1",
	],
    tests_require=["blinker"],
	keywords=["flask", "wechat", "weixin", "micromessage"],
	classifiers=[
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3 :: Only",
		"Programming Language :: Python :: Implementation",
		"Development Status :: 1 - Planning",
        "Environment :: Web Environment",
		"Framework :: Flask",
		"Intended Audience :: Developers",
		"Operating System :: OS Independent",
		"Natural Language :: Chinese (Simplified)",
		"Natural Language :: English",
		"Topic :: Internet :: WWW/HTTP :: Dynamic Content",
		"Topic :: Software Development :: Libraries :: Python Modules",
	]
)