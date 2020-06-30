# Expert-System

Expert system written with two languages : Python and Golang.
Using OOP paradigm

<div align="center">
<img src="./ClassDiagram.png" />
</div>

# How do I use it 

## Python 

Have a look at the `Readme.md` in the `pythonversion` folder.

## Golang

### Config

Edit facts and rules in the `config.json` file.
There's already a filled `config.json` so just use the same pattern.

### Run

After cloning the repo (and installing Go of course):

- `cd expert-system/goversion`
- `go install primitivo.fr/applinh/expert_system` (might not be necessary)
- `go run main.go config.json`

### Improve

- [ ] Docker image