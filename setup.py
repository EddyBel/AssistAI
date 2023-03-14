from setuptools import setup


setup(
    # Nombre del proyecto
    name="Chat-Terminal",
    # Versión del proyecto
    version="1.0.0",
    # Descripción breve del proyecto
    description="Chatbot uses Chatgpt API to offer a natural conversation experience. The user interacts with the chatbot through the command terminal, allowing a simple and fast interaction. The chatbot is designed to answer common questions and offer assistance on different topics.",
    # Descripción larga del proyecto
    long_description="""
Chatbot uses Chatgpt API to offer a natural conversation experience. The user interacts with the chatbot through the command terminal, allowing a simple and fast interaction. The chatbot is designed to answer common questions and offer assistance on different topics.

The project is built in Python programming language and uses the Chatgpt API library for integration with chatbot. The application also makes use of other Python libraries to handle interaction with the user and operations in the command terminal.

Chatbot is designed for anyone looking for a natural and easy -to -use conversation experience, and can be customized to adapt to different needs and purposes.

In general, the project offers an efficient and convenient chatbot solution that can be used in a wide variety of situations.""",
    # Nombre del autor del proyecto
    author="Eduardo Antonio Rangel Serrano",
    # Correo electrónico del autor del proyecto
    author_email="kratos61918@gmail.com",
    # URL del sitio web del proyecto
    url="https://github.com/EddyBel/Chat-Terminal",
    # URL de descarga del proyecto
    download_url="https://github.com/EddyBel/Chat-Terminal/archive/refs/heads/main.zip",
    # Licencia del proyecto
    license="MIT",
    # Palabras clave que usa el programa
    keywords=["Python", "ChatGPT", "Openai", "Chatbot", "Terminal"],
    # Paquetes incluidos en el proyecto
    packages=[""],
    # Clasificadores para el proyecto, por ejemplo, para qué versión de Python es compatible
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    # Versión mínima de Python necesaria para el proyecto
    python_requires=">=3.6",  
    # Dependencias necesarias para el proyecto
    install_requires=[  
        "aiohttp == 3.8.4",
        "aiosignal == 1.3.1",
        "async-timeout == 4.0.2",
        "asynctest == 0.13.0",
        "attrs == 22.2.0",
        "autopep8 == 2.0.2",
        "certifi == 2022.12.7",
        "charset-normalizer == 3.1.0",
        "colorama == 0.4.6",
        "frozenlist == 1.3.3",
        "idna == 3.4",
        "markdown-it-py == 2.2.0",
        "mdurl == 0.1.2",
        "multidict == 6.0.4",
        "openai == 0.27.2",
        "pycodestyle == 2.10.0",
        "Pygments == 2.14.0",
        "requests == 2.28.2",
        "rich == 13.3.2",
        "tomli == 2.0.1",
        "tqdm == 4.65.0",
        "typing-extensions == 4.5.0",
        "urllib3 == 1.26.15",
        "yarl == 1.8.2"
    ],
)
