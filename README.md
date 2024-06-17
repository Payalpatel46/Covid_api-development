# Covid_api-development


# Introduction

This API provides the information regarding '2019 Novel Coronavirus (covid-19)'. It contains a number of confirmed, death, and recovered cases based on the data provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE).

## Applications

* [Coronavirus App by YaseenAbdullah](https://github.com/YaseenAbdullah/coronavirus)
* [Covid 19 App - Map, info & help by DavidBarbaran](https://github.com/DavidBarbaran/Covid19App)
* [COVID-19 Visual Explorer by FitnessAI](https://www.fitnessai.com/covid-19-charts-coronavirus-growth-rate-visual-explorer)


### References

https://github.com/CSSEGISandData/COVID-19

## Branches

|  Branch           |     Feature                      |              Description                                     |
| ----------------- | -------------------------------- |  ----------------------------------------------------------- |
| master            | Docker + Web API                 | For deploying to a server                                    |
| development       | Docker + Web API                 | For testing before merging to Master                         |

## Features

1. The current data (daily updated)
2. Confirmed, Deaths, Recovered
3. The affected countries
4. Individual affected country
5. Timeseries

## How to install

* Run the following command in your command line to run the server

```console
uvicorn main:app
```

## How to install (Docker-compose)

* Run the following command in your command line to run the server

```console
docker-compose up
```

* Or run the server in the background

```console
docker-compose up -d
```

* The port can be changed at <b>docker-compose.override.yml</b>

```yml
version: '3'
services:
  web:
    container_name: "covid19_api_web_container"
    volumes:
      - ./app:/app
    ports:
      - "80:80"
    environment:
      - 'RUN=uvicorn main:app'
```

## How to install (from Dockerhub)

* Download the latest image

```console
docker pull nat236919/covid19-api:latest
```

* Create a container and run

```console
docker run nat236919/covid19-api
```

## How to use API (v2)

Check it out [here](./app/docs/api_docs/v2.md)

## How to use API (v1)

Check it out [here](./app/docs/api_docs/v1.md)

