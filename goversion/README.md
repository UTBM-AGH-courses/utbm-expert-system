# Expert system
Little expert system developed in Go

## Config

Edit facts and rules in the `config.json` file.
There's already a filled `config.json` so just use the same pattern.

## Run

### With Docker

Will run with using the `config.json` at the root of the repo.

- `docker pull docker.pkg.github.com/vareversat/expert-system/goexpert:latest`
- `docker run -it docker.pkg.github.com/vareversat/expert-system/goexpert:latest`


### With Go
After cloning the repo (and installing Go of course):

- `cd expert-system/goversion`
- `go install primitivo.fr/applinh/expert_system` (might not be necessary)
- `go run main.go config.json`

