from ..base.httptester import HTTPTester


class CS531A4(HTTPTester):
    """CS531A4 is a special purpose HTTPTester with test cases for Assignment 4 of the CS531 (Web Server Design) course"""

    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/limited1/protected", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_basic_auth_realm(self, report):
        """Test whether files are protected with HTTP Basic auth and return configured realm"""
        self.check_status_is(report, 401)
        self.check_header_is(report, "WWW-Authenticate", 'Basic realm="Fried Twice"')


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_2(self, report):
        """Test case 2"""
        assert False, "Yet to be implemented!"
        self.check_status_is(report, 200)


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/limited2/foo/bar.txt", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_nested_digest_auth(self, report):
        """Test whether files in nested directories are protected with HTTP Digest auth"""
        self.check_status_is(report, 401)
        self.check_header_begins(report, "WWW-Authenticate", "Digest")


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_4(self, report):
        """Test case 4"""
        assert False, "Yet to be implemented!"
        self.check_status_is(report, 200)


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_5(self, report):
        """Test case 5"""
        assert False, "Yet to be implemented!"
        self.check_status_is(report, 401)


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_6(self, report):
        """Test case 6"""
        assert False, "Yet to be implemented!"
        self.check_status_is(report, 401)


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_7(self, report):
        """Test case 7"""
        assert False, "Yet to be implemented!"
        self.check_status_is(report, 200)


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_8(self, report):
        """Test case 8"""
        assert False, "Yet to be implemented!"
        self.check_status_is(report, 401)


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/limited1/1/protected2", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_nested_basic_auth(self, report):
        """Test whether files in nested directories are protected with HTTP Basic auth"""
        self.check_status_is(report, 401)
        self.check_header_is(report, "WWW-Authenticate", 'Basic realm="Fried Twice"')


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_10(self, report):
        """Test case 10"""
        assert False, "Yet to be implemented!"
        self.check_status_is(report, 200)


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_11(self, report):
        """Test case 11"""
        assert False, "Yet to be implemented!"
        self.check_status_is(report, 401)


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_12(self, report):
        """Test case 12"""
        assert False, "Yet to be implemented!"
        self.check_status_is(report, 401)


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_13(self, report):
        """Test case 13"""
        assert False, "Yet to be implemented!"
        self.check_status_is(report, 400)


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_14(self, report):
        """Test case 14"""
        assert False, "Yet to be implemented!"
        self.check_status_is(report, 401)


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_15(self, report):
        """Test case 15"""
        assert False, "Yet to be implemented!"
        self.check_status_is(report, 401)


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_16(self, report):
        """Test case 16"""
        assert False, "Yet to be implemented!"
        self.check_status_is(report, 416)


    @HTTPTester.request("get-url-ua.http", PATH="/a4-test/", USERAGENT="CS 531-f18 A4 automated Checker")
    def test_17(self, report):
        """Test case 17"""
        assert False, "Yet to be implemented!"
        self.check_status_is(report, 416)
