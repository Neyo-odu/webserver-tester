# WebServer Tester

An HTTP testing and deployment system for CS 531 (Web Server Design) course projects.

## Test Locally

To test your server, run your server first, note down the host and port of the server (which can be on the local machine or on a remote machine), then execute the tester script against that `<host>` and `<port>`.

```
$ git clone https://github.com/ibnesayeed/webserver-tester.git
$ cd webserver-tester
$ pip install -r requirements.txt
$ ./tester.py -h

Usage:
./tester.py [[<host>]:[<port>] [<test-id>|<assignment-numbers>]]

<host>               : Hostname or IP address of the server to be tested (e.g., 'localhost')
<port>               : Port number of the server to be tested (default: '80')
<test-id>            : ID of an individual test function (e.g., 'test_0_healthy_server')
<assignment-numbers> : Comma separated list of assignment numbers (default: all assignments)
```

Alternatively, build a Docker image from the source to ensure all the dependencies are available and run tester script inside.

```
$ docker image build -t webserver-tester .
$ docker container run --rm -it webserver-tester ./tester.py -h
```

Be aware that the `localhost` inside of the container refers to the container itself and not the host machine, so use a host that is reachable from inside of the container.

Alternatively, the web interface can be used to test the server. The web interface can be deployed both on the host machine or in a Docker container. Here is how to run it in a container.

```
$ docker container run --rm -it -p 5000:5000 webserver-tester
```

Then access it from http://localhost:5000 and provide the `<host>:<port>` information in the appropriate form then run tests.

## Deploy and Test on Course's Test Machine

A machine is configured to build Docker images from students' private GitHub repositories that contain a `Dockerfile`. Go to http://cs531.cs.odu.edu/ and provide your CS ID in the appropriate form field then click "Deploy the Web Server" button. Depending on the network speed and complexity of the image, it might take some time to pull the source code and build an image. If an image is built successfully then it will automatically remove any existing containers of the corresponding student and deploy a new one. This newly deployed server will be accessible from `http://<cs-id>.cs531.cs.odu.edu/`.

**It is important that your `Dockerfile` is setup in a way that it runs the server on the network interface `0.0.0.0` and port `80` by default.**

Once your server is deployed, you can test it from the http://cs531.cs.odu.edu/ page using the appropriate form.

Alternatively, you can use command line to both deploy and test your server on the testing machine.

To deploy your instance:

```
$ curl -i http://cs531.cs.odu.edu/servers/<cs-id>
```

To deploy your instance with a specific code version:

```
$ curl -i http://cs531.cs.odu.edu/servers/<cs-id>/<git-ref>
```

To list available tests:

```
$ curl -i http://cs531.cs.odu.edu/tests
```

To run a specific test:

```
$ curl -i http://cs531.cs.odu.edu/tests/<host>:<port>/<test-id>
```

To run all tests in an assignment:

```
$ curl -i http://cs531.cs.odu.edu/tests/<host>:<port>/<assignment-number>
```

To run all tests:

```
$ curl -i http://cs531.cs.odu.edu/tests/<host>:<port>
```

## Contribute

To add more test cases, first create an issue describing the test scenario. To avoid duplicate efforts, claim the ticket if you want to work on it. Fork the repository and submit a PR when done.

Adding a test case is quite simple. First, check the `messages` director to see if any existing HTTP Request messages are suitable for your scenario. If not, then create a new Request message file and name it appropriately. You can use `<HOST>`, `<PORT>`, and `<HOSTPORT>` placeholders that will be replaced with the corresponding values of the server being tested. The latter is a combination of the other two in the form of `<HOST>:<PORT>`, but it does not include the port number if it is the default `80`. Another special placeholder `<PIPELINE>` is used in messages where multiple messages are supposed to be sent as one. This is replaced with an empty string before making the request. The purpose of this placeholder is to distinguish separator of payload from another HTTP message. Apart from these special placeholders, any number of other placeholders can be used that are specified when defining a test case (e.g., `PATH`).

In the `tester.py` file locate where existing test cases are present, then define a new method using the `test_<assignment-number>_<descriptive_name>` naming convention. Add a sentence or two to describe the test in the form of doc string. Add the `@make_request(<request-message-file.http>, [PLACEHOLDER1="VALUE1", ...])` decorator above your method. This will perform the request, parse the response, and execute your test conditions if no connection or syntactic errors are found. Your test method will receive the request and response objects. They contain various raw and parsed attributes to perform your test assertions on.

```py
req = {
    "raw": ""
}
res = {
    "raw_headers": "",
    "http_version": "",
    "status_code": 0,
    "status_text": "",
    "headers": {},
    "payload": None,
    "payload_size": 0,
    "connection": "closed"
}
```

We can have more than one assertions in a single test case, but the first one that fails will be reported otherwise the test will pass. Assertions take the following form:

```py
assert <test-condition>[, <optional-failure-message>]
```

We have included a number of helper methods for various common assertions. Check the `tester.py` file for method names using the `check_<helper_name>` format. Using these helpers is preferred when possible as they make the test case more readable. For example, if we want to test whether a server returns `400 Bad Request` response when the request has a malformed header, we can create a message file named `message/malformed-header.http`:

```http
GET /foo HTTP/1.1
Host: <HOSTPORT>
Header with missing colon

```

Then add a test case as following:

```py
@make_request("malformed-header.http")
def test_0_bad_request_header(self, req, res):
    """Test whether the server recognizes malformed headers"""
    assert res["status_code"] == 400, f"Status expected '400', returned '{res['status_code']}'"
```

Alternatively, utilize an included assertion helper as following:

```py
@make_request("malformed-header.http")
def test_0_bad_request_header(self, req, res):
    """Test whether the server recognizes malformed headers"""
    self.check_status_is(res, 400)
```

Let's write another test case with a custom placeholder. In this case we will utilize the `messages/get-path.http` file and supply the `<PATH>` placeholder to a file that does not exist. We will expect a `404` response with HTTP version as `HTTP/1.1` that also includes a `Date` header.

```http
GET <PATH> HTTP/1.1
Host: <HOSTPORT>
Connection: close

```

With the above template message, add the following test case:

```py
@make_request("messages/get-path.http", PATH="/file-does-not-exist.html")
def test_0_bad_request_header(self, req, res):
    """Test HTTP version, inclusion of Date header, and 404 Not Found"""
    self.check_version_is(res, "HTTP/1.1")
    self.check_date_valid(res)
    self.check_status_is(res, 404)
```


That's it! We got a couple of brand new test cases in place.
