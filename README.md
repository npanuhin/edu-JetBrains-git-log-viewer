<h1 align="center">Git Log Viewer</h1>

This simple web application displays the Git log retrieved from the server

Demo is avaliable here: https://gitlog.jb.npanuhin.me

## Features

- Displays the Git log in a browser window
- Preserves the original formatting and tabulation
- All traffic is fully encrypted with HTTPS

## Technologies used

- HTML + CSS + JavaScript for the client
- Python (Flask) for the server

## How it works

This repository contains both the [client](client) and the [server](server) parts. The client part is [deployed](https://github.com/npanuhin/edu-Git-log-server/actions/workflows/pages.yml) to GitHub Pages, while the server part is deployed to my own server.

1) When you open the [demo page](https://gitlog.jb.npanuhin.me), first the HTML page is loded. Then CSS and JavaScript files are loaded asynchroniously. The JavaScript file contains the code that immediately sends a request to the server.

2) Server runs on Python and is accessible at https://npanuhin.me:2096. When it receives a request, it executes the `git log` command in the system shell and returns the result in plain text.

3) JavaScript receives the response and puts it into the `pre` tag.

## Potential improvements

- Many more customization options can be added to `git log` and the request to the server, like filtering, sorting, etc.

- While I don't see any obvious security issues with this implementation, I doubt that the approach of running a shell command from Python in a web application is very secure, so in my opinion it should not be used in a production environment.

- For each request the server runs `git log` command, which is not very efficient. It would be better to run it only once and then cache the result (just store in some file or even memory).

   For the sake of simplicity, I didn't implement this feature.

#### Implementaion limitations

- Server part of this project is not updated automatically, so `git` will not show the latest commits until I manually do `git pull` on the server.

   This limitation will not be present in the real production environment, like the one described in the task. (From the problem statement I assume, that the server on which the application is running is also the one on which the Git repository is located)
