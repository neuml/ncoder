# 💫 ncoder 

<p align="center">
    <img src="https://raw.githubusercontent.com/neuml/ncoder/master/images/overview.png"/>
</p>

<p align="center">
    <a href="https://github.com/neuml/ncoder/releases">
        <img src="https://img.shields.io/github/release/neuml/ncoder.svg?style=flat&color=success" alt="Version"/>
    </a>
    <a href="https://github.com/neuml/ncoder">
        <img src="https://img.shields.io/github/last-commit/neuml/ncoder.svg?style=flat&color=blue" alt="GitHub last commit"/>
    </a>
    <a href="https://github.com/neuml/ncoder/issues">
        <img src="https://img.shields.io/github/issues/neuml/ncoder.svg?style=flat&color=success" alt="GitHub issues"/>
    </a>
</p>

`ncoder` is an open-source AI coding agent that integrates with Jupyter Notebooks. This project uses the OpenAI API client to connect to any OpenAI-compatible endpoint and enable collaborative coding with AI. 

`ncoder` provides a [base Docker image](https://hub.docker.com/r/neuml/ncoder) that supports coding with [OpenCode](https://opencode.ai/) in [server mode](https://opencode.ai/docs/server/), a [quantized Qwen3-Coder 30B model](https://huggingface.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF) for lightweight local inference and/or any other [txtai process](https://github.com/neuml/txtai).

## Quickstart

Install the Jupyter Notebook extension on your local machine.

```
pip install ncoder
```

`ncoder` provides a default server as a Docker image. Run one of the following.

```
# DEFAULT: Run with opencode backend, sends data to `opencode serve` endpoint
docker run -p 8000:8000 --gpus all --rm -it neuml/ncoder

# ALTERNATIVE 1: Run with qwen3-coder, keeps all data local
docker run -p 8000:8000 -e CONFIG=qwen3-coder.yml -gpus all --rm -it neuml/ncoder

# ALTERNATIVE 2: Run with a custom txtai workflow
docker run -p 8000:8000 -v config:/config -e CONFIG=/config/config.yml --gpus all --rm -it neuml/ncoder
```

Jupyter Notebooks can be created in [Visual Studio Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) or your preferred notebook platform. Add the following two sections to test.

```
# Load ncoder extension
%load_ext ncoder
```

```
# Test it out
%ncoder Write a Python Hello World Example
```

An [example notebook](https://github.com/neuml/ncoder/blob/master/examples.ipynb) is also available.

If you already have a LLM API you'd like to integrate with, it's simply a matter of setting the correct environment variables.

```
%env OPENAI_BASE_URL=LLM API URL (e.g. https://api.openai.com/v1)
%env OPENAI_API_KEY=api-key
%env API_MODEL=gpt-5.2
%load_ext ncoder
```

## Demo

The short video clip below gives a brief overview on how to use `ncoder`.

<p align="center">
    <img src="https://raw.githubusercontent.com/neuml/ncoder/master/images/demo.gif"/>
</p>
