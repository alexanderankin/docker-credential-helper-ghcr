#!/usr/bin/env python3

import json
import os
import subprocess
import sys

VERSION = "__version__"

SUPPORTED_HOSTS = {
    "ghcr.io",
    "docker.pkg.github.com",
}


def run(*args: str) -> str:
    result = subprocess.run(
        args,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=5,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"{' '.join(args)} failed with exit code {result.returncode}: "
            f"{result.stderr.strip()}"
        )

    return result.stdout.strip()


def get() -> None:
    docker_login_host = sys.stdin.read().strip()

    host = docker_login_host
    if host.startswith("https://"):
        host = host[len("https://"):]

    host = host.rstrip("/")

    if host not in SUPPORTED_HOSTS:
        raise RuntimeError(f"{host!r} is not a supported host")

    if os.getenv("GITHUB_ACTIONS") == "true":
        print_credentials(os.getenv("GITHUB_ACTOR"), os.getenv("GITHUB_TOKEN"))
    else:
        print_gh_credentials()


def print_gh_credentials() -> None:
    token = run(
        "gh",
        "auth",
        "token",
        "--hostname",
        "github.com",
    )

    if not token:
        raise RuntimeError("GitHub token is blank")

    username = run(
        "gh",
        "api",
        "user",
        "--jq",
        ".login",
    )
    print_credentials(username, token)


def print_credentials(username: str, password: str) -> None:
    print(json.dumps({
        "Username": username,
        "Secret": token,
    }))


def main() -> None:
    command = sys.argv[1] if len(sys.argv) >= 2 else None

    try:
        match command:
            case "get":
                get()

            case "store" | "erase":
                # Consume Docker's input, although we deliberately don't persist
                # anything because gh is the source of truth.
                sys.stdin.read()

            case "-v" | "-V" | "--version":
                print(VERSION)

            case "-h" | "--help":
                print("""docker-credential-ghcr

Docker credential helper backed by the GitHub CLI.

requirements:
  gh auth login

troubleshooting:
  gh auth status

For classic PAT/OAuth authentication you may need package scopes:
  gh auth refresh --scopes=read:packages,write:packages
""")

            case _:
                sys.exit(1)

    except Exception as exc:
        if os.getenv("DEBUG", "").strip():
            raise

        print(str(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
