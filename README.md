# Getting Started with MCP

## Installation

To get started with MCP, first, install `uv`, an extremely fast Python package and project manager written in Rust:

```sh
pip install uv
```

## Setting Up Your Environment

Create a virtual environment using `uv`:

```sh
uv venv
```

Initialize the project structure:

```sh
uv init
```

Add MCP CLI to your project:

```sh
uv add "mcp[cli]"
```

## Installing Required Libraries

Install all necessary libraries by running:

```sh
uv install
```

## Creating an MCP Server

Let's create a simple MCP server that exposes a calculator tool and some data.

Create a file `server.py` and install the MCP server:

```sh
mcp install server.py
```

### Running the MCP Server

You can install this server in Claude Desktop and interact with it immediately by running:

```sh
mcp dev server.py
```

Alternatively, you can test it with the MCP Inspector for debugging and validation.

---

This guide covers the basic setup and installation of an MCP server. Happy coding!




