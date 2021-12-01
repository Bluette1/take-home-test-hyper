# pet-profile-web-app

This is a pet registration and tracking application for pets where pet owners can sign up and register their pets.


## Built with
- Javascript
- Javascript design patterns
- Node.js
- React.js
- Redux
- JSON Web Token (JWT)

## Live Demo link
- [Deployed frontend site on Heroku](https://pet-profile-app.herokuapp.com/)
- [Deployed backend site on Heroku](https://pet-profile-api.herokuapp.com/)

## Getting Started

To get a local copy up and running follow these simple example steps.

## Prerequisites

- Install node.

## Set up Locally

```
cd frontend
```

- Create a `.env.development` file in the root repository of the project and paste the following:

```
REACT_APP_REQUEST_OPTIONS_HOST=localhost

REACT_APP_REQUEST_OPTIONS_PORT=8080

REACT_APP_REQUEST_OPTIONS_HTTP_PROTOCOL=http

PORT=8081

```

Run the following commands to start the react front end application:

```
yarn install
yarn start

```


Open a new terminal and run backend Nodejs express server: 


```
cd backend && yarn install
node server.js
```

Open [http://localhost:8081](http://localhost:8081) to view it in the browser.

### Login
The user can login in and create an account. 

 ## Features
- The user can access the following functions application: 
  
  - Display a list of registered pets
  - A logged in user can add a pet to their list of owned pets


This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).


### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)
#### Heroku Deployment with Docker
- Instructions can be found [here]( 
 https://betterprogramming.pub/how-to-containerize-and-deploy-apps-with-docker-and-heroku-b1c49e5bc070).
- [Container Registry and Runtime(Docker Deploys)](https://devcenter.heroku.com/articles/container-registry-and-runtime)
- You may have to [disable the eslint plugin](https://stackoverflow.com/questions/67364108/react-app-failed-to-load-config-airbnb-in-deploying-to-heroku)

## 📝 License

This project is [MIT](https://opensource.org/licenses/MIT) licensed.
