## Running
The project is built and run using Docker. For your convenience docker-compose files have been provided to start the project with along with all dependencies. Install `docker` and `docker-compose` using the usual method of your operating system then in the directory issue the command `docker-compose up`. The project will be available at `localhost:4000`.

## Structure
The project consists of two executables: a Pyramid API server and a thin Node.js SPA server. The API server uses postgres as its data store.

## Considerations
### Server-Side Rendering
Given the nature of the application server-side rendering would be preferred over the SPA style done here. SPA was done purely to reduce development time to fit within the 8-hour alotted time.
### Asynchronous Code
Python has good support for asynchronous code with asyncio but in this required slightly more setup that I had time to do. Unlike e.g. Node.js most Python things default to synchronous and must be wrapped. This is particularly true right now with database access. Since there won't be any real network calls in this demonstration the use of asyncio doesn't make a practical difference here. Were this to become a production application I would take the time to set up asyncio.


## Notes for self
fix js dependencies
docker-compose
clean up unecessary create-react-app stuff if I have time
