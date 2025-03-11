# Getting Started with MCP

## Table of Contents

1. [What is MCP?](#what-is-mcp)
2. [File Structure](#file-structure)
3. [Installation](#installation)
4. [Setting Up Your Environment](#setting-up-your-environment)
5. [Installing Required Libraries](#installing-required-libraries)
6. [Creating an MCP Server](#creating-an-mcp-server)
   - [Running the MCP Server](#running-the-mcp-server)
7. [Contributing](#contributing)


## What is MCP?

The Model Context Protocol (MCP) is a standardized framework designed to securely expose data and functionality to LLM applications. It functions similarly to a web API but is specifically tailored for interactions with large language models (LLMs). MCP servers provide three key capabilities:

- **Resources**: These act like GET endpoints, allowing the LLM to retrieve and load relevant data into its context.
- **Tools**: Comparable to POST endpoints, tools enable the execution of code or actions that produce side effects.
- **Prompts**: Reusable templates that define structured interaction patterns for the LLM.


## File Structure

The repository follows this structure:

```
Getting-Started-with-MCP/
│── .gitignore              # Specifies untracked files to ignore
│── .python-version         # Indicates the Python version used
│── README.md               # Main project documentation
│── pyproject.toml          # Project configuration and dependencies
│── requirements.txt        # List of required Python packages
│── server.py               # Main script to run the MCP server
│── uv.lock                 # Lock file for dependency management
```


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

Let's create a simple MCP server that exposes a tool for printing "Hello, World!".

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

## Output 

Using the Inspector Mode to test the code.


## Contributing

If you'd like to contribute to this project, follow these steps:

1. **Fork the Repository**: Click the 'Fork' button at the top right of this repository.
2. **Clone the Repository**: Clone your forked repo to your local machine.
   ```sh
   git clone https://github.com/your-username/mcp-project.git
   ```
3. **Create a Branch**: Create a new branch for your feature or bug fix.
   ```sh
   git checkout -b feature-branch-name
   ```
4. **Make Changes**: Implement your changes and commit them.
   ```sh
   git commit -m "Description of changes"
   ```
5. **Push to GitHub**: Push your changes to your forked repository.
   ```sh
   git push origin feature-branch-name
   ```
6. **Create a Pull Request**: Open a pull request on the original repository.


### We appreciate all contributions! Feel free to suggest new features, improvements, or bug fixes.





